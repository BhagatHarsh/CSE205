def insatbeg(l: list, n: int) -> list:
    newL = [n]
    for i in range(len(l)):
        newL.append(l[i])
    return newL


l = list(map(int, input("Enter the list: ").split()))
n = int(input("Enter the Number to be inserted: "))
print('new list is: ', insatbeg(l, n))
