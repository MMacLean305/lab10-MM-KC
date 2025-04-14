import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

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
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4),5.0)
        self.assertAlmostEqual(hypotenuse(6, 8), 10.0)
        self.assertAlmostEqual(hypotenuse(12, 5), 13.0)



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