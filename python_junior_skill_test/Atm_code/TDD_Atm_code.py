import unittest
from Atm_code import *

class Test_Atm(unittest.TestCase):
    def test_validDividend(self):
        self.assertEqual(Atm_code(652),'invalid amount')
    def test_negativeValue(self):
        self.assertEqual(Atm_code(-37),'invalid amount')
    def test_notes(self):
        self.assertEqual(Atm_code(555),['500*1 = 500', '100*0 = 0', '50*1 = 50', '10*0 = 0', '5*1 = 5'])
    
if __name__ == '__main__' :
    unittest.main
    