'''
Andrew Kozempel
CMPSC 412
Lab 6
Fall 2023
'''

# node class for BST nodes with left/right child
# val = [id, name]
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# BST class
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):

        # create new node to insert
        node = Node(val)

        # create current pointer for going through nodes
        current = self.root

        # if there's no root yet, root = node
        if not self.root:
            self.root = node
            return

        while True:

            # if new node is less than current
            if val[0] < current.val[0]:

                # if no left child, left = node
                if current.left is None:
                    current.left = node
                    return
                
                # point to left child
                current = current.left

            # if new node is greater than current
            elif val[0] > current.val[0]:

                # if no right child, right = node
                if current.right is None:
                    current.right = node
                    return
                
                # point to right child
                current = current.right

            # already exists, exit
            else:
                return
            
    def find(self, id):

        # create current pointer for going through nodes
        current = self.root

        # go through elements
        while current:

            # found, return True
            if id == current.val[0]:
                print(f"\nStudent with ID {id} found: {current.val[1]}")
                return

            # if val is less than current
            elif id < current.val[0]:
                current = current.left

            # if new node is greater than current
            elif id > current.val[0]:
                current = current.right

        # not found, return False
        print(f"\nStudent with ID {id} not found")
        return
                       
    # print inorder (left, root, right)
    def print_students(self, node):

        if node:

            self.print_students(node.left)
            print(f'ID: {node.val[0]}, Name: {node.val[1]}')
            self.print_students(node.right)

# create tree
bst = BinarySearchTree()

student1 = [1001, "Andrew Kozempel"]
student2 = [1002, "John Doe"]
student3 = [1000, "Jane Smith"]
student4 = [1004, "Tony Stark "]

# print, insert, print x4
print("\nBST before insert 1:")
bst.print_students(bst.root)
bst.insert(student1)
print("\nBST after insert 1:")
bst.print_students(bst.root)

print("\nBST before insert 2:")
bst.print_students(bst.root)
bst.insert(student2)
print("\nBST after insert 2:")
bst.print_students(bst.root)

print("\nBST before insert 3:")
bst.print_students(bst.root)
bst.insert(student3)
print("\nBST after insert 3:")
bst.print_students(bst.root)

print("\nBST before insert 4:")
bst.print_students(bst.root)
bst.insert(student4)
print("\nBST after insert 4:")
bst.print_students(bst.root)

# search
bst.find(1002)
bst.find(1003)