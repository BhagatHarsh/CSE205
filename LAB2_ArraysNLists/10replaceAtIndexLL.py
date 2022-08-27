class Node:
    def __init__(self, data) -> None:
        self.next = None
        self.data = data
        return


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        return

    def printList(self):
        temp = self.head
        while (temp != None):
            print(temp.data, end=' ')
            temp = temp.next
        print()
        return

    def append(self, data):
        if(self.head == None):
            self.head = Node(data)
            self.tail = self.head
            return

        newNode = Node(data)
        self.tail.next = newNode
        self.tail = newNode
        return

    def replatind(self, pos: int, n: int) -> int:
        if(self.head == None):
            return -1
        if(pos == 1):
            self.head.data = n
            return 1
        temp = self.head
        ind = 0
        while(temp != None):
            if(ind == pos-1):
                temp.data = n
                return 1
            ind+=1
            temp = temp.next
        return -1


l = list(map(int, input("Enter the list: ").split()))
n = int(input("Enter the Number to be inserted: "))
pos = int(input("Enter the index: "))
ll = LinkedList()
for i in l:
    ll.append(i)

result = ll.replatind(pos, n)
if(result == -1):
    print('Index issue')
else:
    print('New List is:')
    ll.printList()
