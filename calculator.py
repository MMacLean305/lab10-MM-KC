# https://github.com/MMacLean305/lab10-MM-KC
# Partner 1: Matthew Maclean
# Partner 2: Kevin Chang
# First example
import math
def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def mul(a, b):
    return a * b

def div(a, b): # raise ZeroDivisionError if a == 0
    if a == 0:
        raise ZeroDivisionError
    else:
        return b / a

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError()
    return math.log(b, a)

def exp(a, b):
    return a**b

def square_root(a):
    if a < 0:
        raise ValueError()
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)
