from graphs import Queue

# Basic binary tree unit - Node
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.value}"


class BinaryTree:
    def __init__(self, root: Node=None):
        self.root = root

    #  Inorder (Left -> Root -> Right) 
    def inorder(self, node=None):
        node = node if node else self.root
        if node.left:
            self.inorder(node.left)
        print("Node: ", node.value)
        if node.right:
            self.inorder(node.right)

    #  Preoder (Root -> Left -> Right) 
    def preorder(self, node=None):
        node = node if node else self.root
        print("Node: ", node.value)
        if node.left:
            self.preorder(node.left)
        if node.right:
            self.preorder(node.right)

    def level_order(self, node=None):
        node = node if node else self.root
        q = Queue([node])
        
        while len(q.collection) > 0:
            node = q.remove()
            print(node)
            if node.left:
                q.add(node.left)
            if node.right:
                q.add(node.right)

    def search(self, target, node=None):
        node = node if node else self.root
        if node.value == target:
            return True
        left = self.search(target, node.left) if node.left else False
        right = self.search(target, node.right) if node.right else False
        return left or right


""" Create the following tree
        a
       / \
      b    c
     / \    \
    d   e    f
"""

root_a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
root_a.left = b
root_a.right = c
b.left = d
b.right = e
c.right = f

a_tree = BinaryTree(root=root_a)
# b.inorder()
# a_tree.inorder()
# print()
# a_tree.preorder()
# print("hello world")
# print(a_tree.search('e'))
# print(a_tree.search('z'))
a_tree.level_order()


# Binary Search Tree
"""
        10
       /  \
      5    15
     / \     \
    2   7     20
"""
class BinarySearchTree(BinaryTree):
    def search(self, target):
        node = self.root
        while node != None:
            if node.value == target:
                return True
            elif node.value > target:
                node = node.left
            else:
                node = node.right

        return False

root = Node(10)
b = Node(5)
c = Node(15)
d = Node(2)
e = Node(7)
f = Node(20)
root.left = b
root.right = c
b.left = d
b.right = e
c.right = f
bst = BinarySearchTree(root)
print(bst.search(2))
print(bst.search(1))
print(bst.search(21))



