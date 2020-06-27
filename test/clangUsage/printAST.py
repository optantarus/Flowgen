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
           'emptyFile':                                 'Test empty cpp file.',
           'emptyMainFunction':                         'Test empty main function.',
           'mainFunctionAnnotationWithoutLevel':        'Test annotation without level',
           'mainFunctionAnnotationWithLevel0':          'Test annotation with level 0',
           'mainFunctionAnnotationWithLevel1':          'Test annotation with level 1',
           'mainFunctionAnnotationsWithLevel0andLevel1':'Test annotations with level 0 and 1',
           'mainFunctionAnnotationsWithLevel0to2'      :'Test annotations with levels 0,1,2',
           'mainFunctionAnnotationsWithLevel0to3'      :'Test annotations with levels 0,1,2,3',
           'mainFunctionIfWithoutAnnotation'           :'Test if without annotation',
           'mainFunctionIfWithAnnotation'              :'Test if with annotation',
           'mainFunctionIfElseWithoutAnnotation'       :'Test if else without annotations',
           'mainFunctionIfElseWithAnnotation'          :'Test if else with annotations',
           'mainFunctionIfElseWithCondAnnotations'     :'Test if else with conditional and normal annotations',
           'mainFunctionIfElseWithCondAnnotation'      :'Test if else with conditional annotations',
           'mainFunctionIfWithCondAnnotation'          :'Test if with conditional annotation',
           'mainFunctionIfWithCondAnnotations'         :'Test if with conditional annotation and normal annotation',
           'mainFunctionIfElseIfWithCondAnnotations'   :'test if - elseif with conditional and normal annotations',
           'mainFunctionIfElseIfElseWithCondAnnotations':'Test if - elseif - else with conditional and normal annotations',
           'mainFunctionNestedIfWithAnnotation'        :'Test nested if with annotations',
           'mainFunctionNestedIfElseWithoutAnnotation' :'Test if else with annotation and nested if else without annotation',
           'mainFunctionNestedIfWithCondAnnotations'   :'Test nested ifs with conditional and normal annotations',
           'mainFunctionNestedIfElseIfWithAnnotation'  :'Test nested if elseif with annotations',
           'mainFunctionDoWhileLoopWithAnnotation'     :'Test do while loop with annotation',
           'mainFunctionDoWhileLoopWithCondAnnotations':'Test do while loop with conditional an normal annotations',
           'mainFunctionForLoopWithAnnotation'         :'Test for loop with annotation',
           'mainFunctionForLoopWithCondAnnotations'    :'Test for loop with conditonal and normal annotations',
           'mainFunctionWhileLoopWithAnnotation'       :'Test while loop with annotations',
           'mainFunctionWhileLoopWithCondAnnotations'  :'Test while loop with normal and conditional annotations',
           'mainFunctionForLoopIfWithCondAnnotations'  :'Test if within for loop with normal and conditional annotations',
           'functionsCallWithAnnotations'              :'Test function call in main with annotations',
           'functionsCallIfElseWithCondAnnotations'    :'Test functions calls within if - else with annotations',
           'functionCallsForLoopWithCondAnnotations'   :'Test function cal within for loop with annotations',
           'mainFunctionReturnCondAnnotations'         :'Test return with conditional annotation',
           'complex1'                                  :'Test combination of different structures'
           }

    def shortString(self, string, length):
        '''Shorts string to given length and add ... to indicate missing parts.
        
        @param[in]   string   string to check and shorten
        @param[in]   length   maximal length of string
        
        @return      resultString  string with a maximum size of length + 3 (if shortened, for trailing ...)
        '''
        resultString = ''
        
        if(len(string) > length):
            resultString = string[:(length)] + '...'
        else:
            resultString = string
            
        return resultString

    def printNode(self, node, indention):
        '''Creates a string with AST data of the node.
        
        It creates one row of a markdown table.
        
        @param[in]   node   node to get description string for
        @param[in]   indent string that is added to string in first colum
        @return      string with data from AST of node
        '''
        
        nodeDescription =     ' | ' +  indention + '  ' + node.kind.name
        nodeDescription +=    ' | ' + str(node.kind.value)
        
        if(node.spelling != None):
           nodeDescription += ' | ' + str(node.spelling.decode("utf8"))
        else:
           nodeDescription += ' | ' + str(node.spelling)
        
        
        nodeDescription +=    ' | ' + str(node.displayname.decode("utf8"))
        nodeDescription +=    ' | ' + str(node.get_usr().decode("utf8"))
        nodeDescription +=    ' | ' + str(node.kind.is_declaration())
        nodeDescription +=    ' | ' + str(node.extent.start.line) + ' | ' + str(node.extent.end.line)
        
        arguments = ''
        for argument in node.get_arguments():
            arguments += argument.spelling.decode("utf8")
        
        nodeDescription +=    ' | ' + arguments
        
        tokens = ''
        for token in node.get_tokens():
            tokens += str(token.spelling.decode("utf8"))
        
        nodeDescription +=     ' | ' + self.shortString(tokens.replace('\n', ''), 60) + ' | '
        
        
        return nodeDescription

    def walkAST(self, node, astFile, indent):
        '''Recursive function to walk through the whole AST.
        
        @param[in]   node     node from which AST output is started
        @param[in]   astFile  output file for AST
        @param[in]   indent   variable to give generated AST strings the correct indention
        '''
        children = node.get_children()
        
        astFile.write(self.printNode(node, indent) + '\n')
        
        if (children):
            indentNext = indent + '--'
            for child in children:
                self.walkAST(child, astFile, indentNext)
            
        

    def toFile(self):
        """Generate files with AST for all source files specified in testFiles.
        """
        
        for fileName, description in self.testFiles.items():
            # get clang translation unit and file path
            clangIndex = clang.cindex.Index.create()
            clangTu = clangIndex.parse('testFiles/test_' + fileName + '.cpp',self.clangStdArgs)
            clangTu = clangIndex.parse('testFiles/test_' + fileName + '.cpp',self.clangStdArgs)
            relevant_folder=os.path.dirname(clangTu.spelling)
            
            # create AST file
            astFile = open('clangUsage/astFiles/ast_' + fileName +'.txt',"w")
            print("'Write AST File: " + fileName)
            
            # write header for AST file
            astFile.write('Source folder: ' + str(relevant_folder.decode("utf8")) + '  \n')
            astFile.write('Description source file: ' + description + '  \n')
            astFile.write('AST symbols:  "#": node does not have this information   \n  \n')
            astFile.write('AST table:  \n  \n')
            
            # create AST table header
            astFile.write('| node.kind.name | node.kind.value | node.spelling | node.displayname | node.get_usr() | node.kind.is_declaration() | node.extent.start.line | node.extent.end.line | node.get_arguments() | node.get_tokens() | \n')
            astFile.write('| :------------------- | :---:  | :---:  | :---:  | :---:  | :---:  | :---:  | :---:  | :---: | :--- | \n')
            
            # write AST
            self.walkAST(clangTu.cursor, astFile, '')

            astFile.close()



if __name__ == "__main__":
    
    astPrint = printAST()
    astPrint.toFile()