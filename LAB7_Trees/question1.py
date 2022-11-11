from LAB4_StacksAndQueues.question1 import Stack


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder(root):
    if root == None:
        return
    stack = Stack()
    stack.push(root)
    while stack:
        node = stack.pop()
        print(node.data, end=" ")
        if node.right is not None:
            stack.push(node.right)
        if node.left is not None:
            stack.push(node.left)
    print()


def inorder(root):
    if root == None:
        return
    stack = Stack()
    node = root
    while stack or node:
        if node:
            stack.push(node)
            node = node.left
        else:
            node = stack.pop()
            print(node.data, end=" ")
            node = node.right
    print()


def postorder(root):
    if root == None:
        return
    s1 = Stack()
    s2 = Stack()
    s1.push(root)
    while s1:
        node = s1.pop()
        s2.push(node)
        if node.left:
            s1.push(node.left)
        if node.right:
            s1.push(node.right)

    while s2:
        node = s2.pop()
        print(node.data, end=" ")

    print()


def inorderInsert(root, parent, lchild, rchild):
    if root == None:
        root = Node(parent)
        if (lchild):
            root.left = Node(lchild)
        if (rchild):
            root.right = Node(rchild)
        # print("Added the root", root.data, "left child", root.left.data,
        #       "right child", root.right.data)
        return root

    stack = Stack()
    node = root
    while stack or node:
        if node:
            if (node.data == parent):
                if (lchild):
                    node.left = Node(lchild)
                if (rchild):
                    node.right = Node(rchild)
                # print("Added the node", node.data, "left child",
                #       node.left.data, "right child", node.right.data)
                return
            stack.push(node)
            node = node.left
        else:
            node = stack.pop()
            node = node.right


file = []
with open("question1.txt") as f:
    for line in f:
        file.append(list(map(str, line.strip().split(','))))

inp = []
for i in file:
    tmp = []
    for j in i:
        try:
            tmp.append(int(j))
        except:
            tmp.append(None)
    inp.append(tmp)

try:
    root = inorderInsert(None, inp[0][0], inp[0][1], inp[0][2])
except Exception as e:
    print(e)

for i in inp[1:]:
    inorderInsert(root, i[0], i[1], i[2])

# print("Preorder traversal: ", end="")
# preorder(root)
# print("\nInorder traversal: ", end="")
# inorder(root)
# print("\nPostorder traversal: ", end="")
# postorder(root)
