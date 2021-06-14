import unittest
from code import *

class Test_ExpVal(unittest.TestCase):
    def test_caseA(self):
        self.assertEqual(expression_validation('(){'),(3,'invalid expression'))
    def test_caseB(self):
		self.assertEqual(expression_validation('[(]'),(2,'invalid expression'))
    
    def test_caseD(self):
        self.assertEqual(expression_validation('()[{}]'),'valid')
    def test_caseE(self):
		self.assertEqual(expression_validation('[()]'),'valid')
        
    
if __name__ == '__main__' :
    unittest.main
    