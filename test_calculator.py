# https://github.com/MMacLean305/lab10-MM-KC
# Partner 1: Matthew Maclean
# Partner 2: Kevin Chang

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(3, 1), 5)
        self.assertEqual(add(9, 5), 14)
        self.assertEqual(add(4, 3), 7)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(sub(6, 2), 4)
        self.assertEqual(sub(8, 3), 5)
        self.assertEqual(sub(10, 4), 6)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(1,2), 2)
        self.assertEqual(mul(2,2), 4)
        self.assertEqual(mul(3, 3), 9)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(5, 1), 5)
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(9,3), 3)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        self.assertEqual(div(5, 1), 5)
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):  # 3 assertions
        self.assertEqual(log(2, 3), 8)
        self.assertEqual(log(6, 2), 36)
        self.assertEqual(log(1, 3), 1)

    def test_log_invalid_base(self):  # 1 assertion
        self.assertEqual(log(5, 1), 5)
        with self.assertRaises(ValueError):
            log(4, -2)
    
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
