# using the question 1 XD
from question1 import *

'''
postfix notation

4 6 + 10 *
'''


def computeOperation(op: str, i: int, j: int) -> int:
    if(op == '+'):
        return i+j
    elif(op == '-'):
        return i-j
    elif(op == '*'):
        return i*j
    elif(op == '/'):
        return i//j
    return -1


def evaluatePostfix(exp: str) -> int:
    stack = Stack()
    for i in reversed(list(map(str, exp.split()))):
        stack.push(i)
    stack.printStack()
    exp1 = int(stack.pop())
    exp2 = int(stack.pop())
    op = stack.pop()
    print(op, exp1, exp2)
    val = computeOperation(op, exp1, exp2)
    if(not stack.isEmpty()):
        while(not stack.isEmpty()):
            exp1 = val
            exp2 = int(stack.pop())
            op = stack.pop()
            print(op, exp1, exp2)
            val = computeOperation(op, exp1, exp2)
    return val


inputStr = input("Enter a Postfix Expression: ")
getOutput = evaluatePostfix(inputStr)
print("The value of the Postfix expression %s is %d" % (inputStr, getOutput))
