def srch(l: list, n: int) -> int:
    for i in range(len(l)):
        if (l[i] == n):
            return i
    return -1


l = list(map(int, input("Enter the list: ").split()))
n = int(input("Enter the Number to be searched: "))
ind = srch(l, n)
if (ind == -1):
    print("Element not found")
else:
    print('Element found on index: ' + str(ind + 1))
