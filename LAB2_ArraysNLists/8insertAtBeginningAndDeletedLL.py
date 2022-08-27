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
            print(temp.data)
            temp = temp.next
        return

    def appendFirst(self, data):
        if(self.head == None):
            self.head = Node(data)
            self.tail = self.head
            return

        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        return
    
    def delatend(self):
        temp = self.head
        prev = temp
        while(temp.next != None):
            prev = temp
            temp = temp.next
        prev.next = None
        return


l = LinkedList()
l.appendFirst(1)
l.appendFirst(2)
l.appendFirst(3)
l.appendFirst(4)
l.appendFirst(5)
l.appendFirst(6)
l.delatend()
l.delatend()
l.delatend()
l.printList()
