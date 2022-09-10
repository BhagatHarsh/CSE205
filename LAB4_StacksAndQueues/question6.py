class Node:
    def __init__(self, data) -> None:
        self.next = None
        self.data = data
        return

# Implementation of the Queue ADT using a singly linked list.


class Dequeue:
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
    def push_back(self, data):
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
    def pop_back(self):
        assert not self.isEmpty(), "Cannot pop from an empty dequeue."
        tmp = self.head
        prev = tmp
        while(tmp.next != None):
            prev = tmp
            tmp = tmp.next
        self.tail = prev
        self.tail.next = None
        self.size -= 1
        return tmp.data

    def push_front(self, data):
        if(self.head == None):
            self.head = Node(data)
            self.tail = self.head
            self.size += 1
            return

        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        self.size += 1
        return

    # Removes and returns the first item in the queue.
    def pop_front(self):
        assert not self.isEmpty(), "Cannot pop from an empty dequeue."
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


# queue = Dequeue()
# queue.push_back(4)
# queue.push_front(5)
# queue.push_back(6)
# queue.pop_front()
# queue.printQueue()
# queue.pop_back()
# queue.push_front(7)
# queue.printQueue()
