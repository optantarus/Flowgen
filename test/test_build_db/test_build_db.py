"""Test Build database tool.

@file test_build_db.py
"""

import unittest
import os
import filecmp

import clang.cindex

import build_db


class build_db_test(unittest.TestCase):
    """Test cases for the build database tool.
    
    The tests only call build_db.find_functions, because of the complex structure of clang node type.
    Each test compares the created *flowdb file with a reference.
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
           'mainFunctionNestedIfWithCondAnnotations'   :'Test nested ifs with conditional and normal annotations',
           'mainFunctionDoWhileLoopWithAnnotation'     :'Test do while loop with annotation',
           'mainFunctionDoWhileLoopWithCondAnnotations':'Test do while loop with conditional an normal annotations',
           'mainFunctionForLoopWithAnnotation'         :'Test for loop with annotation',
           'mainFunctionForLoopWithCondAnnotations'    :'Test for loop with conditonal and normal annotations',
           'mainFunctionWhileLoopWithAnnotation'       :'Test while loop with annotations',
           'mainFunctionWhileLoopWithCondAnnotations'  :'Test while loop with normal and conditional annotations',
           'mainFunctionForLoopIfWithCondAnnotations'  :'Test if within for loop with normal and conditional annotations',
           'functionsCallWithAnnotations'              :'Test function call in main with annotations',
           'functionsCallIfElseWithCondAnnotations'    :'Test functions calls within if - else with annotations',
           'functionCallsForLoopWithCondAnnotations'   :'test function cal within for loop with annotations',
           'mainFunctionReturnCondAnnotations'         :'Test return with conditional annotation'
           }

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_refFiles(self):
        """Test tool with diferent input files and compare output with reference files.
        """
        
        for fileName, description in self.testFiles.items():
            # get clang translation unit and file path
            clangIndex = clang.cindex.Index.create()
            clangTu = clangIndex.parse('testFiles/test_' + fileName + '.cpp',self.clangStdArgs)
            relevant_folder=os.path.dirname(clangTu.spelling.decode("utf-8"))
            
            # execute function under test
            testFile = open('test_build_db/generatedFiles/test_' + fileName +'.flowdb',"w")
            build_db.find_functions(clangTu.cursor, testFile, relevant_folder)
            testFile.close()
            
            # compare generated file with reference
            self.assertTrue(filecmp.cmp('test_build_db/generatedFiles/test_' + fileName +'.flowdb', 'test_build_db/referenceFiles/ref_' + fileName +'.flowdb', False), description + ': Generated *.flowdb file differs from reference.')
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()