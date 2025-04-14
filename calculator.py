# https://github.com/MMacLean305/lab10-MM-KC
# Partner 1: Matthew Maclean
# Partner 2: Kevin Chang
# First example
import math
def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a * b

def div(a, b): # raise ZeroDivisionError if a == 0
    if a == 0:
        raise ZeroDivisionError
    else:
        return b / a

def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError()
    return math.log(b, a)

def exp(a, b):
    return a**b

def square_root(a):
    try:
        if a < 0:
            raise ValueError()
        return math.sqrt(a)

    except ValueError as e:
        print(f"Error: {e}")

def hypotenuse(a, b):
    return math.hypot(a, b)
