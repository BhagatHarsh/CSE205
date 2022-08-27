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
    
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.printList()
# dll.printRev() it works!!!