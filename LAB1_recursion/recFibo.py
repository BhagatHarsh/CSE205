'''

'''
from math import ceil, floor


def fibo(n: int) -> int:
    if (n == 2):
        return 1
    if (n == 1):
        return 0

    return fibo(n - 1) + fibo(n - 2)


n = int(input('Enter a number: '))
assert n >= 0 and ceil(n) == floor(
    n), "Number Entered must be a positive integer"

print('Fibonacci of number is: ' + str(fibo(n)))
