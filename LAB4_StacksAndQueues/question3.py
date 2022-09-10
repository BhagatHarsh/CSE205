from question1 import *

bracesOpen = ['{', '(', '[', '<']
bracesClosed = ['}', ')', ']', '>']

line = input("Enter the line to be Validated :")
stack = Stack()
valid = True

for i in line:
    if(i in bracesOpen):
        stack.push(i)
    elif(i in bracesClosed):
        if(not stack.isEmpty()):
            open = stack.peek()
            if(bracesClosed[bracesOpen.index(open)] == i):
                stack.pop()
            else:
                valid = False
                break
        else:
            valid = False
            break
    elif(i == '#'):
        if(not stack.isEmpty()):
            valid = False
            break
        else:
            break  
    # stack.printStack()

if(valid):
    print('Valid Expression')
else:
    print('Not a Valid Expression')
