'''
Andrew Kozempel
CMPSC 413
Lab 8
Fall 2023
'''

# node class for AVL nodes with left/right child
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1

# AVL class
class AVLTree:
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
                    node.parent = current
                    break
                
                # point to left child
                current = current.left

            # if new node is greater than current
            elif val > current.val:

                # if no right child, right = node
                if current.right is None:
                    current.right = node
                    node.parent = current
                    break
                
                # point to right child
                current = current.right

            # already exists, exit
            else:
                return
            
        # perform rotations to balance tree
        while node:
            self.rebalance(node)
            node = node.parent
            
    # print left, root, right
    def Inorder(self, node):

        if node:

            self.Inorder(node.left)
            print(node.val, '-> ', end = '')
            self.Inorder(node.right)

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

        # perform rotations to balance tree
        current = parent
        while current:
            self.rebalance(current)
            current = current.parent

    # gets height of a node
    def getHeight(self, node):
        
        # invalid node
        if not node:
            return 0
        
        return node.height

    # get balance factor of node
    def getBalance(self, node):
        
        # invalid node
        if not node:
            return 0
        
        # height of left subtree minus height of right subtree
        return self.getHeight(node.left) - self.getHeight(node.right)
    
    def rightRotate(self, y):

        # store values for rotation
        x = y.left # x is left child of y
        x_right_sub = x.right # right subtree of of x

        # perform rotation
        x.right = y # x is root, y is right child
        y.left = x_right_sub # left subtree of y

        #     y           x
        #  x                y
        #   RST          RST
        
        # update heights
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))

        # return root
        return x

    def leftRotate(self, x):

        # store values for rotation
        y = x.right # y is right child of x
        y_left_sub = y.left # left subtree of y

        # perform rotation
        y.left = x # y is new root, x is left child
        x.right = y_left_sub # right subtree of x

        #     x            y
        #       y        x   
        #    LST          LST 

        # update heights
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        
        # return root
        return y

    def rebalance(self, node):

        # invalid node
        if not node:
            return None

        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        balance = self.getBalance(node)

        # left left
        if balance > 1 and self.getBalance(node.left) >= 0:
            return self.rightRotate(node)

        # left right
        if balance > 1 and self.getBalance(node.left) < 0:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)

        # right right
        if balance < -1 and self.getBalance(node.right) <= 0:
            return self.leftRotate(node)

        # right left
        if balance < -1 and self.getBalance(node.right) > 0:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node
    
    def isAVL(self, node):

        if not node:
            return True

        left_height = self.getHeight(node.left)
        right_height = self.getHeight(node.right)

        # Check balance factor and BST property
        if abs(left_height - right_height) <= 1:
            return self.isAVL(node.left) and self.isAVL(node.right)
        else:
            return False
    

# TESTS

# create and insert
tree = AVLTree()
vals = [30, 20, 40, 10, 25, 35, 50, 5, 15, 27, 37]

# insertion
print(f'\nInserting vals: {vals}')
for val in vals:
    tree.insert(val)

# inorder traversal
print('\nInorder Traversal:')
tree.Inorder(tree.root)
print("\nValid AVL?:", tree.isAVL(tree.root))

# deletion
tree.removeNode(20)
print("\nInorder Traversal after deleting 20:")
tree.Inorder(tree.root)
print("\nValid AVL?:", tree.isAVL(tree.root))
