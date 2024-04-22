'''
Andrew Kozempel
CMPSC 412
Lab 5
Fall 2023
'''

# node class for BST nodes with left/right child
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
            if val < current.val:

                # if no left child, left = node
                if current.left is None:
                    current.left = node
                    return
                
                # point to left child
                current = current.left

            # if new node is greater than current
            elif val > current.val:

                # if no right child, right = node
                if current.right is None:
                    current.right = node
                    return
                
                # point to right child
                current = current.right

            # already exists, exit
            else:
                return
            
    # print left, root, right
    def Inorder(self, node):

        if node:

            self.Inorder(node.left)
            print(node.val, '-> ', end = '')
            self.Inorder(node.right)

    # print root, left, right
    def Preorder(self, node):

        if node:

            print(node.val, '-> ', end = '')
            self.Preorder(node.left)
            self.Preorder(node.right)

    # print left, right, root
    def Postorder(self, node):

        if node:

            self.Postorder(node.left)
            self.Postorder(node.right)
            print(node.val, '-> ', end = '')

    def find(self, val):

        # create current pointer for going through nodes
        current = self.root
        parent = None

        # go through elements
        while current:

            # found, return True
            if val == current.val:
                return True, current, parent

            # if val is less than current
            elif val < current.val:
                parent = current
                current = current.left

            # if new node is greater than current
            elif val > current.val:
                parent = current
                current = current.right

        # not found, return False
        return False, None, None
    
    def BSTmin(self):

        # empty tree, return None
        if not self.root:
            return None

        # create current pointer for going through nodes
        current = self.root

        # go through leftmost path
        while current.left:
            current = current.left

        return current.val

    def BSTmax(self):

        # empty tree, return None
        if not self.root:
            return None

        # create current pointer for going through nodes
        current = self.root

        # go through rightmost path
        while current.right:
            current = current.right

        return current.val
    
    def removeNode(self, val):

        found, node, parent = self.find(val)

        # if node doesnt exist, return
        if not found:
            return
        
        # two children
        if node.left and node.right:

            # find in-order successor
            successor = node.right
            successor_parent = node

            # keep looping left to find smallest val
            while successor.left:
                successor_parent = successor
                successor = successor.left

            # copy successor value to node
            node.val = successor.val

            # remove successor
            if successor == successor_parent.left:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right

        # if left child
        elif node.left:

            # if node is parent's left child
            if node == parent.left:
                # parent's left child is now nodes left child
                parent.left = node.left

            # if node is parent's right child
            else:
                # parent's right child is now nodes left child
                parent.right = node.left

        # if right child
        elif node.right:

            # if node is parent's left child
            if node == parent.left:
                # parent's left child is now nodes right child
                parent.left = node.right

            # if node is parent's right child
            else:
                # parent's right child is now nodes right child
                parent.right = node.right

        # no child
        else:
            if node == parent.left:
                parent.left = None
            elif node == parent.right:
                parent.right = None
            else:
                self.root = None

    def merge(self, tree2_root):

        # iterate through nodes in BST2 and insert nodes
        if tree2_root:
            self.insert(tree2_root.val)
            self.merge(tree2_root.left)
            self.merge(tree2_root.right)

        return self
    
    def buildFromList(self, lst):

        # iterate through lst and insert elements
        for ele in lst:
            self.insert(ele)

        return self
    
    # in order traversal helper function
    def inOrder(self, node):

        # if node, do inorder traversal and return vals
        if node:
            return (self.inOrder(node.left) +
                    [node.val] +
                    self.inOrder(node.right))
        
        return []
        
    def isValid(self):

        # get vals from inorder traversal
        vals = self.inOrder(self.root)

        # check if vals are sorted (propert of BST)
        if vals == sorted(vals):
            return True
        
        return False


### EXAMPLES

# create a tree and insert 10 values
bst = BinarySearchTree()
values = [50, 30, 70, 15, 35, 62, 87, 7, 22, 44]
for value in values:
    bst.insert(value)

# print traversals
print("\nInorder traversal:")
bst.Inorder(bst.root)

print("\n\nPreorder traversal:")
bst.Preorder(bst.root)

print("\n\nPostorder traversal:")
bst.Postorder(bst.root)

# find a node in the BST
found, node, parent = bst.find(35)

if found:
    print("\n\nValue 35 found in the BST.")
else:
    print("\nValue 35 not found in the BST.")

# find minimum and maximum values in the BST
print("\nMinimum value in the BST:", bst.BSTmin())
print("Maximum value in the BST:", bst.BSTmax())

# validate BST
if bst.isValid():
    print("\nThe tree is a valid BST.")
else:
    print("\nThe tree is not a valid BST.")

# remove a node from the BST
bst.removeNode(30)  # two children
print("\nInorder traversal after removing 30:")
bst.Inorder(bst.root)

# create second BST to merge
bst2 = BinarySearchTree()
bst2_values = [90, 67, 85, 32]
for value in bst2_values:
    bst2.insert(value)
    
# merge trees
bst.merge(bst2.root)
print("\n\nInorder traversal after merging with another tree:")
bst.Inorder(bst.root)

# validate BST
if bst.isValid():
    print("\n\nThe merged tree is a valid BST.")
else:
    print("\n\nThe merged tree is not a valid BST.")