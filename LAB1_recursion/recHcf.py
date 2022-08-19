'''

'''


def hcf(n: int, m: int) -> int:
    if (m == 0):
        return n
    return hcf(m, n % m)


n, m = map(int, input("Enter two Numbers: ").split())
if (n > m):
    print('Hcf of there two numbers is: ' + str(hcf(n, m)))
elif (m > n):
    print('Hcf of there two numbers is: ' + str(hcf(m, n)))
else:
    print('Hcf of there two numbers is: ' + str(n))
