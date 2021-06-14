import unittest
from sum_string import *

class TestSumString(unittest.TestCase):

    def test_CaseA(self):
        self.assertEqual(input_validation("123123"), 6)
    def test_CaseB(self):
        self.assertEqual(input_validation("1538023"), 4)
    def test_CaseC(self):
        self.assertEqual(input_validation("45679023"), 0)
    def test_decimal(self):
        self.assertEqual(input_validation("3.14"), "please Enter Number" )
    def test_alphanumeric(self):
        self.assertEqual(input_validation("1adcfc56271"), "you have enter alphanumeric" )
    def test_emptyString(self):
        self.assertEqual(input_validation(""), "please Enter Number")


if __name__ == '__main__':
    unittest.main()