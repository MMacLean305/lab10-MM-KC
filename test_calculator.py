import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(3,1),5)
        self.assertEqual(add(9, 5), 14)
        self.assertEqual(add(4, 3), 7)
    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(6,2),4)
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
    def test_divide_by_zero(self): # 1 assertion
        self.assertEqual(div(5, 1), 5)
        with self.assertRaises(ZeroDivisionError):
            div(0,5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(2,3),8)
        self.assertEqual(log(6, 2), 36)
        self.assertEqual(log(1, 3), 1)

    def test_log_invalid_base(self): # 1 assertion
        self.assertEqual(log(5, 1), 5)
        with self.assertRaises(ValueError):
            log(4,-2)
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()