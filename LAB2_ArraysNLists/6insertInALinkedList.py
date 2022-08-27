class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def isrch(root: ListNode, n: int) -> int:
    ind = 0
    while(root.next != None):
        if(root.data == n):
            return ind
        ind += 1
        root = root.next
    return -1


# created some nodes
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

# created links between the nodes
a.next = b
b.next = c
c.next = d

root = a
n = int(input("Enter a number to be searched: "))
search = isrch(root, n)
if(search == -1):
    print('Element not found')
else:
    print('Element found at index: ',search)

