def add(x, y):
    return x + y


def subtract(x, y):
    return x-y


def divide(x, y):
    if y>0 or y<0:
        return x/y
    else:
        return "Invalid denominator!Don't divide by 0"


def multiply(x, y):
    return x*y


def square(x):
    return x**2


def power(x, y):
    return x**y

import math
def sqrt(x):
    return math.sqrt(x)
