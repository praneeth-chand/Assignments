import unittest
from code import *

class Test_ExpVal(unittest.TestCase):
    def test_caseA(self):
        self.assertEqual(validation('(){'),'invalid')
    def test_caseB(self):
		self.assertEqual(validation('[1+2(ab]'),'invalid')
    def test_caseC(self):
		self.assertEqual(validation('[1+2(ab])'),'invalid')
    def test_caseD(self):
        self.assertEqual(validation('(abc)[{123}]'),'valid')
    def test_caseE(self):
		self.assertEqual(validation('[1+2(ab)]'),'valid')
        
    
if __name__ == '__main__' :
    unittest.main
    