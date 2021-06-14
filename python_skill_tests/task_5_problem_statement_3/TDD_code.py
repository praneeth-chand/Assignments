import unittest
from code import *

class Test_MaxmimumSum(unittest.TestCase):
    def test_caseA(self):
        self.assertEqual( MaximumSum([-2, -3, 4, -1, -2, 1, 5, -3]),7)
    def test_caseB(self):
        self.assertEqual(MaximumSum([-2,1,-3,4,-1,2,1,-5,4]),6)
    def test_caseC(self):
        self.assertEqual(MaximumSum([5,4,-1,7,8]),23)

if __name__ == '__main__' :
    unittest.main