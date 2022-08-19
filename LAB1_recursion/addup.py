from math import ceil, floor


def addup(n: int) -> int:
    if(n == 1):
        return 1
    return n + addup(n-1)


n = int(input('Enter a number: '))
assert n >= 0 and ceil(n) == floor(
    n), "Number Entered must be a positive integer"

print('The sum of numbers between one to %d is %d' % (n, addup(n)))
