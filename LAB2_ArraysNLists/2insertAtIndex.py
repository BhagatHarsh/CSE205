def insatind(l: list, pos: int, n: int) -> list:
    newL = []
    for i in range(pos):
        newL.append(l[i])
    newL.append(n)
    for i in range(pos,len(l)):
        newL.append(l[i])
    return newL


l = list(map(int, input("Enter the list: ").split()))
n = int(input("Enter the Number to be inserted: "))
pos = int(input("Enter the index: "))
assert pos >= 0 and pos < len(l), "index error"
print('new list is: ', insatind(l, pos, n))
