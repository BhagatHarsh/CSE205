from LAB7_Trees.question1 import inorder, postorder
import random


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def insert(self, data):
        if (self.root == None):
            self.root = Node(data)
            return

        curr = self.root
        while (curr != None):
            if (data < curr.data):
                if (curr.left == None):
                    curr.left = Node(data)
                    print("inserted", data, "to the left subtree of",
                          curr.data)
                    return
                else:
                    curr = curr.left

            elif (data > curr.data):
                if (curr.right == None):
                    curr.right = Node(data)
                    print("inserted", data, "to the right subtree of",
                          curr.data)
                    return
                else:
                    curr = curr.right
            else:
                raise Exception("node already exists" + str(data))
        return

    def findMin(self):
        curr = self.root
        while (curr != None):
            if (curr.left == None):
                return curr.data
            else:
                curr = curr.left
        return

    def findMinInd(self, root):
        curr = root
        while (curr != None):
            if (curr.left == None):
                return curr.data
            else:
                curr = curr.left
        return curr

    def remove(self, data) -> None:
        print(data, "is being removed")
        self.root = self.removeTree(self.root, data)
        return

    def removeTree(self, root, data) -> None:
        if root == None:
            return None
        print(root.data)
        if data < root.data:
            root.left = self.removeTree(root.left, data)
        elif data > root.data:
            root.right = self.removeTree(root.right, data)
        else:
            if (root.left != None):
                temp = root.right
                root = None
                return temp

            elif (root.right != None):
                temp = root.left
                root = None
                return temp
            temp = self.findMinInd(root.right)
            root.data = temp.data
            root.right = self.removeTree(root.right, temp.data)

        return root


tree = BST()
nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(nodes)
print("the array formed is ", nodes)
for i in nodes:
    tree.insert(i)
inorder(tree.getRoot())
print("The minimum element of the tree is", tree.findMin())
tree.remove(nodes[random.randint(0, len(nodes) - 1)])
print("getting the result")
inorder(tree.getRoot())
postorder(tree.getRoot())
