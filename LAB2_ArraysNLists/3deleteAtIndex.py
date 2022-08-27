def delatind(l: list, pos: int) -> list:
    newL = []
    for i in range(pos):
        newL.append(l[i])
    for i in range(pos+1,len(l)):
        newL.append(l[i])
    return newL


l = list(map(int, input("Enter the list: ").split()))
pos = int(input("Enter the index to be deleted: "))
assert pos >= 0 and pos < len(l), "index error"
print('new list is: ', delatind(l, pos))
