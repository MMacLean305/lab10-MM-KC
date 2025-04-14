"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

# First example
import math
def add(a, b):
    return a+b

import math
def square_root(a):
    try:
        if a < 0:
            raise ValueError()
        return math.sqrt(a)

    except ValueError as e:
        print(f"Error: {e}")

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): 
    return a + b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a * b



def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError()
    return math.log(b, a)

def exponent(a, b):
    return a ** b

def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b): # raise ZeroDivisionError if a == 0
    if a == 0:
        raise ZeroDivisionError
    else:
        return b / a
def log(a, b): # use math library + raise ValueError
    if a <= 0 and a != 1:
        raise ValueError
    else:
        return math.log(b, a)
def exp(a, b):
    return a**b