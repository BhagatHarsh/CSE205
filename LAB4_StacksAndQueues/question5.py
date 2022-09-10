# Implementation of the unbounded Priority Queue ADT using a Python list
# with new items appended to the end.
# Private storage class for associating queue items with their priority.


class _PriorityQEntry(object):

    def __init__(self, item, priority):
        self.item = item
        self.priority = priority
        self.next = None


class PriorityQueue:

    # Create an empty unbounded priority queue.
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Returns True if the priority queue is empty.
    def isEmpty(self):
        return self.size == 0

    # Returns the number of items in the priority queue.
    def __len__(self):
        return self.size

    # Adds the given item to the priority queue.
    def enqueue(self, data, priority):
        if(self.head == None):
            self.head = _PriorityQEntry(data, priority)
            self.tail = self.head
            self.size += 1
            return

        newNode = _PriorityQEntry(data, priority)
        self.tail.next = newNode
        self.tail = newNode
        self.size += 1
        return

    # Removes and returns the first item in the priority queue.
    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."

        # Find the entry with the highest priority.
        highest = self.head.priority
        highesti = self.head
        prev = self.head
        tmp = self.head
        prevTemp = prev
        val = 0

        while(tmp != None):
            # See if the ith entry contains a higher priority (smaller integer).
            if tmp.priority < highest:
                highest = tmp.priority
                highesti = tmp
                prevTemp = prev
            prev = tmp
            tmp = tmp.next
        # Remove the entry with the highest priority and return the item.
        if(self.head == highesti):
            if(self.head.next != None):
                val = highesti.item
                self.head = self.head.next
            else:
                val = self.head.item
                self.head = None
        else:
            val = highesti.item
            prevTemp.next = highesti.next
        self.size -= 1
        return val

    # Print PQ
    def prnpq(self):
        temp = self.head
        while (temp != None):
            print("{ %s , %s }" %
                  (str(temp.item), str(temp.priority)), end=' ')
            temp = temp.next
        print()
        return


# pqueue = PriorityQueue()
# pqueue.enqueue(300, 0)
# pqueue.enqueue(100, 2)
# pqueue.enqueue(200, 1)
# pqueue.prnpq()
# print(pqueue.dequeue())
# print(pqueue.dequeue())
# print(pqueue.dequeue())
