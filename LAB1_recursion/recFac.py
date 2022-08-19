'''

'''
from math import ceil, floor


def fac(n):
    if (n == 0):
        return 1
    print(n, "above return")
    # return n * fac(n - 1)
    return fac(n - 1) * n


n = float(input("Enter a Number: "))
assert n >= 0 and ceil(n) == floor(
    n), "Number Entered must be a positive integer"
print('Factorial of %d is %d' % (n, fac(n)))
