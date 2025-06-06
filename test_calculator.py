# https://github.com/MMacLean305/lab10-MM-KC
# Partner 1: Matthew Maclean
# Partner 2: Kevin Chang

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(3, 1), 4)
        self.assertEqual(add(9, 5), 14)
        self.assertEqual(add(4, 3), 7)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(subtract(6, 2), 4)
        self.assertEqual(subtract(8, 3), 5)
        self.assertEqual(subtract(10, 4), 6)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(1,2), 2)
        self.assertEqual(mul(2,2), 4)
        self.assertEqual(mul(3, 3), 9)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(1, 5), 5)
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(3,9), 3)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):  # 3 assertions
        self.assertAlmostEqual(logarithm(10, 1000), 3.0)
        self.assertAlmostEqual(logarithm(2, 8), 3.0)
        self.assertAlmostEqual(logarithm(10, 100), 2.0)

    def test_log_invalid_base(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(4, -2)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4),5.0)
        self.assertAlmostEqual(hypotenuse(6, 8), 10.0)
        self.assertAlmostEqual(hypotenuse(12, 5), 13.0)



    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-2)
        self.assertAlmostEqual(square_root(100), 10.0)
        self.assertAlmostEqual(square_root(9), 3.0)


# Do not touch this
if __name__ == "__main__":
    unittest.main()
