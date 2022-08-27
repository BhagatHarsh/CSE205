def insatend(l: list, n: int) -> list:
    newL = l
    newL.append(n)
    return newL


l = list(map(int, input("Enter the list: ").split()))
n = int(input("Enter the Number to be inserted: "))
print('new list is: ', insatend(l, n))
