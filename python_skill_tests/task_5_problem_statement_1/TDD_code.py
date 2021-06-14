import unittest
from code import *

class Test_MinJumps(unittest.TestCase):
    def test_caseA(self):
        self.assertEqual(minJumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]),3)
    def test_caseB(self):
        self.assertEqual(minJumps([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),10)
     

if __name__ == '__main__' :
    unittest.main