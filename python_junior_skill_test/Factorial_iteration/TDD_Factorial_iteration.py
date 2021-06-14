import unittest
from Factorial_of_number_iteration import *

class Test_Factorial(unittest.TestCase):
    
    def test_zero(self):
        self.assertEqual(factorial(0),1)
    def test_nonzero(self):
        self.assertEqual(factorial(1),1)
        self.assertEqual(factorial(5),120)
        self.assertEqual(factorial(6),720)
    def test_negative(self):
        self.assertEqual(factorial(-10),-1)
      
if __name__ == '__main__' :
    unittest.main
    