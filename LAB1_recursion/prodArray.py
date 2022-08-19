def prodArray(l: list, n: int) -> int:
    if(n == -1):
        return 1
    return l[n] * prodArray(l, n-1)


l = list(map(int, input("Enter the list: ").split()))
print('the product of list is: ', prodArray(l, len(l)-1))
