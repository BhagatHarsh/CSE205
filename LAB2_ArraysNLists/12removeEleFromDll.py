class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        return


class DoublyLinkedList:
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
    
    #to test if the prev works
    def printRev(self):
        temp = self.tail
        while (temp != None):
            print(temp.data, end=' ')
            temp = temp.prev
        print()
        return
    
    
    def append(self, data):
        if(self.head == None):
            self.head = DoubleNode(data)
            self.tail = self.head
            return

        newNode = DoubleNode(data)
        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode
        return
    
    def deleteNode(self, ele:int):
        if(self.head != None):
            if(self.head.data == ele):
                self.head = self.head.next
                return
            temp = self.head
            while(temp != None):
                if(temp.data == ele):
                    try:
                        temp.prev.next = temp.next
                        temp.next.prev = temp.prev
                    except:
                        break
                    break
                temp = temp.next
            return
        return
    
dll = DoublyLinkedList()
l = list(map(int, input("Enter the list: ").split()))
ele = int(input("Enter the element: "))
for i in l:
    dll.append(i)

result = dll.deleteNode(ele)
if(result == -1):
    print('Index issue')
else:
    print('New List is:')
    dll.printList()