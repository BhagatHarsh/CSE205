class Node:
    def __init__(self, data) -> None:
        self.next = None
        self.data = data
        return

# Implementation of the Queue ADT using a singly linked list.


class Queue:
    # Creates an empty queue.
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Returns True if the queue is empty.
    def isEmpty(self):
        return self.size == 0

    # Returns the number of items in the queue.
    def __len__(self):
        return self.size

    # Adds the given item to the queue.
    def enqueue(self, data):
        if(self.head == None):
            self.head = Node(data)
            self.tail = self.head
            self.size += 1
            return

        newNode = Node(data)
        self.tail.next = newNode
        self.tail = newNode
        self.size += 1
        return

    # Removes and returns the first item in the queue.
    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."
        tmp = self.head.data
        self.head = self.head.next
        self.size -= 1
        return tmp

    def printQueue(self):
        temp = self.head
        while (temp != None):
            print(temp.data, end=' ')
            temp = temp.next
        print()
        return

# queue = Queue()
# queue.enqueue(4)
# queue.enqueue(5)
# queue.enqueue(6)
# queue.dequeue()
# queue.dequeue()
# queue.enqueue(7)
# queue.printQueue()
