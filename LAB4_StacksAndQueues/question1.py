class Node:
    def __init__(self, data) -> None:
        self.next = None
        self.data = data
        return


class Stack:
    def __init__(self) -> None:
        self.head = None
        self.size = 0
        return

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def push(self, data):
        if(self.head == None):
            self.head = Node(data)
            self.size += 1
            return

        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        self.size += 1
        return

    def peek(self):
        assert not self.isEmpty(), "Cannot peek at an empty stack"
        return self.head.data

    def pop(self):
        if(not self.isEmpty()):
            tmp = self.head.data
            self.head = self.head.next
            self.size -= 1
            return tmp
        else:
            print('Stack is empty')
        return

    def printStack(self):
        temp = self.head
        while (temp != None):
            print(temp.data, end=' ')
            temp = temp.next
        print()
        return


# stack = Stack()
# stack.push(4)
# stack.push(5)
# stack.push(6)
# stack.printStack()
# stack.pop()
