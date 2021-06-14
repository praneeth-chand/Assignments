import unittest
from code import *

class Test_MinCost(unittest.TestCase):
    def test_caseA(self):
        self.assertEqual(removeNegativeweights(5,[20, 10, 4, 50, 100]),14)
    def test_caseB(self):
        self.assertEqual(removeNegativeweights(5,[1, 10, 4, 50, 100]),5)
    def test_caseC(self):
        self.assertEqual(removeNegativeweights(5,[1,2,3,4,5]),5)
    def test_caseD(self):
        self.assertEqual(removeNegativeweights(5,[-1, -1, 4, 5, -1]),-1)
        
if __name__ == '__main__' :
    unittest.main
    