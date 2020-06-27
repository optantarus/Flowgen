#!/usr/bin/env python

"""Build database tool.

@file build_db.py

This tool takes sourcefiles as input and create a *.flowdb file.
"""

import re
import sys
import clang.cindex
import os
import filecmp

#clang node types (CursorKind)
#21: CXX_METHOD
#205: if statement
#202: compound statement
#212: continue statement.
#213: A break statement.
#214: A return statement.
#207: A while statement.
#208: A do statement.
#209: A for statement.
#103: CALL_EXPR An expression that calls a function or method.
#101: DECL_REF_EXPR An expression that refers to some value declaration, such as a function, varible, or enumerator.  CursorKind.DECL_REF_EXPR = CursorKind(101)

#clang node properties
      #node.displayname: more info than .spelling
      #node.get_definition(): returns the defining node. 
      #node.location.line, node.location.column, node.location.filename
      #node.get_usr() Return the Unified Symbol Resultion (USR) for the entity referenced by the given cursor (or None).
             #A Unified Symbol Resolution (USR) is a string that identifies a particular entity (function, class, variable, etc.) within a program. USRs can be compared across translation units
      #node.get_referenced() Return the referenced object of a call
#additional feature for Cursors (nodes) that has to be added to clang python bindings
def get_referenced(self):
    return clang.cindex.conf.lib.clang_getCursorReferenced(self)

clang.cindex.Cursor.get_referenced = get_referenced


    
def lookfor_actionAnnotation_inNode(nodeIN,zoom):
    """Looks for an annotated action comment inside the extent of a given node (zoom level modifies the type of action comment).
    """

    if zoom==0:
      zoom=''  
    regextextActionComment=r'^\s*//\$'+str(zoom)+r'(?!\s+\[)\s+(?P<action>.+)$'
    regexToUse=re.compile(regextextActionComment)
    
    # get start and end line of node extend
    start_line=nodeIN.extent.start.line
    end_line=nodeIN.extent.end.line
    
    # save all file line in variable
    # TODO: why dump complete file and not from start to end line ?      
    infile_str=nodeIN.location.file.name
    infile= open(infile_str,'r')            
    enum_file=list(enumerate(infile,start=1))      
    infile.close()
   
    #loop over source code lines
    for i, line in enum_file:
      if i in range(start_line,end_line):
         if regexToUse.match(line):
             return True   
    return False 



def find_functions(node, writefunc, relevant_folder):
  """Search in node and its children for functions or methods.
  
  The function calls itself for every child node.
  Each found function is checked for annotated action comments.
  """
  
  if node.kind.is_declaration():
     #8 is a function and 21 is c++ class method
    if node.kind.value== 8 or node.kind.value==21:
       if os.path.dirname(node.location.file.name) == relevant_folder:
                
         if lookfor_actionAnnotation_inNode(node,0):
            zoom_str='0'
            if lookfor_actionAnnotation_inNode(node,1):
               zoom_str='1'  
               if lookfor_actionAnnotation_inNode(node,2):
                  zoom_str='2'
            classname = ''
            if node.kind.name=='CXX_METHOD':
               classname= str(node.semantic_parent.spelling)+'::'
            print('Found annotated method/function:', classname+node.displayname)
            writefunc.write(node.get_usr()+'\t'+zoom_str+'\t'+str(node.result_type.kind.name)+' '+classname+node.displayname+'\n')
       return

  # Recurse for children of this node
  for c in node.get_children():
      find_functions(c, writefunc, relevant_folder)



if __name__ == '__main__': # pragma: no cover
    """ main program
    """

    index = clang.cindex.Index.create()
    
    # comand line arguments
    args=["-Wall","-ansi"]
    if len(sys.argv)>=2:
       args+=sys.argv[2:]
    
    # parse file given by comand line with specified arguments   
    tu = index.parse(sys.argv[1],args)
    print ('Translation unit:', tu.spelling)
    
    relevant_folder=os.path.dirname(tu.spelling)
    for diagnostic in tu.diagnostics:
      print(diagnostic)
    infile_str=os.path.splitext(os.path.basename(sys.argv[1]))[0]
    
    if not os.path.exists('flowdoc/aux_files/'):
       print('CREATING FOLDER flowdoc/aux_files/')
       os.makedirs('flowdoc/aux_files/')
       
    writefunc = open('flowdoc/aux_files/'+infile_str+'.flowdb',"w")
    find_functions(tu.cursor, writefunc, relevant_folder)
    writefunc.close()

