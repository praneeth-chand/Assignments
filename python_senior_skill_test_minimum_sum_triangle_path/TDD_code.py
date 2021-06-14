import unittest
from code import *

class Test_MinSum(unittest.TestCase):
    def test_caseA(self):
        self.assertEqual(MinimumSumPathTriangle([[2],[3,4],[6,5,7],[4,1,8,3]]),11)
    def test_caseB(self):
        self.assertEqual(MinimumSumPathTriangle( [[3],[6,4],[5,2,7],[9,1,8,6]]),10)

if __name__ == '__main__' :
    unittest.main
    