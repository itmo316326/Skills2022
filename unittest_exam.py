import os
import unittest
import test_code
os.system("test_code.py")
class TestCalc(unittest.TestCase):
    def test_factors(self):
        result1 = test_code.factors(1)
        result2 = test_code.factors(2)
        result3 = test_code.factors(3)
        result4 = test_code.factors(6)
        self.assertEqual(False,len(result1) > 1)
        self.assertEqual(True,len(result4) < 1)

    def test_is_prime(self):
        self.assertEqual(True,test_code.is_prime(2))
        self.assertEqual(True,test_code.is_prime(3))
        self.assertEqual(True,test_code.is_prime(5))
        #self.assertEqual(True,test_code.is_prime(9))
    def test_vowels(self):
        self.assertEqual(True,len(test_code.vowels('a'))>=1)
        self.assertEqual(True,len(test_code.vowels('A'))>=1)
        self.assertEqual(True,len(test_code.vowels('E'))>=1)
        #self.assertEqual(True,len(test_code.vowels('B'))>=1)
if __name__ == '__main__':
    unittest.main()
