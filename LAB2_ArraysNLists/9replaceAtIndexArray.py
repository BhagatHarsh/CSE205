def replatind(l:list, pos:int, n:int) -> None:
    l[pos-1] = n
    return l

l = list(map(int, input("Enter the list: ").split()))
n = int(input("Enter the Number to be inserted: "))
pos = int(input("Enter the index: "))
assert pos >= 0 and pos < len(l), "index error"
print('new list is: ', replatind(l, pos, n))