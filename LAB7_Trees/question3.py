import random


class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def size(self):
        return len(self.heap)

    def insertKey(self, k):
        self.heap.append(k)
        self.heapifyUp(len(self.heap) - 1)
        return

    def heapifyUp(self, i):
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(
                i)], self.heap[i]
            i = self.parent(i)
        return

    def heapifyDown(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[
                i]
            self.heapifyDown(smallest)
        return

    def decreaseKey(self, i, new_val):
        self.heap[i] = new_val
        self.heapifyUp(i)
        return

    def extractMin(self):
        if len(self.heap) == 0:
            return
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapifyDown(0)
        return root

    def getMin(self):
        return self.heap[0]

    def printHeap(self):
        print(self.heap)
        return

    def getHeap(self):
        nodes = []
        for i in range(0, self.size()):
            nodes.append(self.extractMin())
        return nodes


nodes = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
    22, 23, 24, 25, 26, 27, 28
]
random.shuffle(nodes)


def heapSort(nodes: list) -> list:
    heap = MinHeap()
    for i in range(len(nodes)):
        heap.insertKey(nodes[i])
    return heap.getHeap()


print(heapSort(nodes))
