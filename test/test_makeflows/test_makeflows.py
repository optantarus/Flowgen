"""Test makeflows tool.

@file test_makeflows.py
"""

import unittest
import os
import filecmp

import clang.cindex

import makeflows


class makeflows_test(unittest.TestCase):
    """Test cases for the makeflows tool.
    
    The tests only call makeflows.find_functions, because of the complex structure of clang node type.
    """

    clangStdArgs = ["-c", "-x", "c++", "-Wall", "-ansi"]
    
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
           'mainFunctionNestedIfElseWithoutAnnotation' :'Test if else with annotation and nested if else without annotation',
           'mainFunctionNestedIfWithAnnotation'        :'Test nested if with annotations',
           'mainFunctionNestedIfWithCondAnnotations'   :'Test nested ifs with conditional and normal annotations',
           'mainFunctionNestedIfElseIfWithAnnotation'  :'Test nested if elseif with annotations',
           'mainFunctionDoWhileLoopWithAnnotation'     :'Test do while loop with annotation',
           'mainFunctionDoWhileLoopWithCondAnnotations':'Test do while loop with conditional and normal annotations',
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

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_refFiles(self):
        """Test tool with diferent input files and compare output with reference files.
        """
        
        for fileName, description in self.testFiles.items():
            with self.subTest(description=description):
                # get clang translation unit and file path
                clangIndex = clang.cindex.Index.create()
                clangTu = clangIndex.parse('testFiles/test_' + fileName + '.cpp',self.clangStdArgs)
                relevantFolder=os.path.dirname(clangTu.spelling.decode("utf-8"))
                
                folderName = fileName + '/'
                flowDbFolder = 'test_makeflows/inputFiles/' + folderName
                outputFolder = 'test_makeflows/generatedFiles/' + folderName
                
                # execute function under test
                makeflows.find_functions(clangTu, clangTu.cursor, relevantFolder, flowDbFolder, outputFolder)
                
                # compare generated file with reference
                dirCompare = filecmp.dircmp(outputFolder, 'test_makeflows/referenceFiles/ref_' + folderName)
                
                self.assertFalse(dirCompare.diff_files, 'Generated files differs from reference.')
                self.assertFalse(dirCompare.left_only, 'Additional files generated.')
                self.assertFalse(dirCompare.right_only,'Missing files in generated.')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    