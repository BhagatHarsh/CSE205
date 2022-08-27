class Node:
    def __init__(self,data) -> None:
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
    
    def append(self,data):
        if(self.head == None):
            self.head = Node(data)
            self.tail = self.head
            return
        
        #O(n) sol
        # temp = self.head
        # while(temp.next != None):
        #     temp = temp.next
        
        # newNode = Node(data)
        # temp.next = newNode
        
        
        #O(1) sol
        newNode = Node(data)
        self.tail.next = newNode
        self.tail = newNode
        return 


l = LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
l.append(6)
l.printList()




# I tried using the normal function but it does not work
# class ListNode:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# def linsatend(root:ListNode,n:int):
#     tmp = root
#     while(tmp.next != None):
#         tmp = tmp.next
#     tmp.next = ListNode(n)
#     return root

# def printList(root:ListNode):
#     while(root.next != None):
#         print(root.data,end=' ')
#         root = root.next
#     print()
#     return

# # created some nodes
# a = ListNode(1)
# b = ListNode(2)
# c = ListNode(3)
# d = ListNode(4)

# # created links between the nodes
# a.next = b
# b.next = c
# c.next = d

# root = a
# n = int(input("Enter a number to be appended: "))
# root = linsatend(root,n)
# print('after appending the list now is: ')
# printList(root)