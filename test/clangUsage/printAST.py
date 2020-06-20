"""Print AST of files.

@file printAST.py
"""

import os
import filecmp

import clang.cindex


class printAST:
    """Tool to visualize clang AST.
    
    For given file the AST is generated and written to file.
    """

    clangStdArgs = ["-Wall","-ansi"]
    
    testFiles = {
           'mainFunctionIfWithAnnotation'              :'Test if with annotation',
           }

    def printNode(self, node):
        
        nodeDescription = node.kind.name
        nodeDescription += ' (' + str(node.kind.value) + '), '
        nodeDescription += ' ' + str(node.spelling) + ', '
        nodeDescription += ' ' + str(node.displayname) + ', '
        nodeDescription += ' ' + str(node.get_usr()) + ', '
        nodeDescription += str(node.kind.is_declaration()) + ' -- '
        nodeDescription += str(node.extent.start.line) + ', ' + str(node.extent.end.line) + ' -- '
        
        tokens = ''
        for token in node.get_tokens():
            tokens += token.spelling.decode("utf-8")
        
        nodeDescription += tokens
        
        
        return nodeDescription

    def walkAST(self, node, astFile, indent):
        children = node.get_children()
        
        astFile.write(indent + self.printNode(node) + '\n')
        
        if (children):
            indentNext = indent + '  '
            for child in children:
                self.walkAST(child, astFile, indentNext)
            
        

    def toFile(self):
        """Test tool with diferent input files and compare output with reference files.
        """
        
        for fileName, description in self.testFiles.items():
            # get clang translation unit and file path
            clangIndex = clang.cindex.Index.create()
            clangTu = clangIndex.parse('testFiles/test_' + fileName + '.cpp',self.clangStdArgs)
            clangTu = clangIndex.parse('testFiles/test_' + fileName + '.cpp',self.clangStdArgs)
            relevant_folder=os.path.dirname(clangTu.spelling.decode("utf-8"))
            
            # execute function under test
            astFile = open('clangUsage/astFiles/ast_' + fileName +'.txt',"w")
            print("'Write AST File: " + fileName)
            
            astFile.write('Source folder: ' + relevant_folder + '\n')
            astFile.write('Description source file: ' + description + '\n')
            astFile.write('AST infos: kind.name (kind.value), node.spelling, node.displayname,node.get_usr(), kind.is_declaration() -- extent.start.line, extent.end.line -- get_tokens \n')
            astFile.write('AST symbols:  "#": node does not have this information \n\n')
            astFile.write('AST:\n\n')
            
            self.walkAST(clangTu.cursor, astFile, '')

            astFile.close()



if __name__ == "__main__":
    
    astPrint = printAST()
    astPrint.toFile()