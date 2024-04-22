'''
Andrew Kozempel
CMPSC 412
Lab 9
Fall 2023
'''

import timeit
import random

# node class for BST nodes
class Node:

    # initialize node with val + left/right
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# BST class
class BinarySearchTree:

    # initalize BST
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

            # if new node is less than or equal to current
            if val <= current.val:

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

    # print inorder
    def print(self, node):

        if node:

            self.print(node.left)
            print(node.val, '-> ', end = '')
            self.print(node.right)

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
    
    def delete(self, val):

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

# node class for a linked list
class ListNode:

    # initalize node with value and next
    def __init__(self, value):
        self.value = value
        self.next = None

# linked list class
class LinkedList:

    # initalize LL
    def __init__(self):
        self.head = None

    def insert(self, val):

        # if empty, insert at beginning (head)
        if self.head is None:
            self.head = ListNode(val)

        # if not empty
        else:

            # current pointer
            current = self.head

            # go through nodes, until the end
            while current.next:
                current = current.next

            # add node to the end
            current.next = ListNode(val)

    def print(self):

        # intitialize current
        current = self.head

        # keep printing while there are still nodes
        while current:
            print(current.value, end=" -> ")
            current = current.next

    def find(self, value):

        # if the list is empty, false
        if self.head is None:
            return False

        # if head is target, true
        if self.head.value == value:
            return True

        # initialize current node
        current = self.head

        # iterate through nodes
        while current.next:

            # if next is target, return true
            if current.next.value == value:
                return True
            
            current = current.next

        # not found
        return False

    def delete(self, val):

        # unlink head if it is the node to be deleted
        if self.head == val:
            self.head = self.head.next

        # intitialize current
        current = self.head

        # iterate throught nodes
        while current.next:

            # if next node val is to be deleted, bypass it
            if current.next.value == val:
                current.next = current.next.next
                return

            current = current.next

def generate_ints(quantity):

    return [random.randint(1,10000) for _ in range(quantity)]

random_ints = generate_ints(25000)

# list

test_list = []

for ele in random_ints:
    test_list.append(ele)

# dict

test_dict = {}

for ele in random_ints:
    test_dict[len(test_dict)] = ele

# BST

test_BST = BinarySearchTree()

for ele in random_ints:
    test_BST.insert(ele)

# LL

test_LL = LinkedList()

for ele in random_ints:
    test_LL.insert(ele)

### PRINT

print_time_list = timeit.timeit(lambda: print(test_list), number=1)
print_time_dict = timeit.timeit(lambda: print(test_dict), number=1)
print_time_bst = timeit.timeit(lambda: test_BST.print(test_BST.root), number=1)
print_time_LL = timeit.timeit(lambda: test_LL.print(), number=1)

print(f'\nPrinting list time: {print_time_list:.5f} seconds')
print(f'Printing dict time: {print_time_dict:.5f} seconds')
print(f'Printing BST time: {print_time_bst:.5f} seconds')
print(f'Printing LL time: {print_time_LL:.5f} seconds')

### RETRIEVAL

random_value = random.choice(random_ints)

print(f'\nRetrieval from list time: {timeit.timeit(lambda: random_value in test_list, number=1):.5f} seconds')
print(f'Retrieval from dict time: {timeit.timeit(lambda: random_value in test_dict.values(), number=1):.5f} seconds')
print(f'Retrieval from BST time: {timeit.timeit(lambda: test_BST.find(random_value), number=1):.5f} seconds')
print(f'Retrieval from LL time: {timeit.timeit(lambda: test_LL.find(random_value), number=1):.5f} seconds')

### INSERTION

new_random_value = random.randint(1, 10000)

#test_dict[len(test_dict)] = new_random_value

print(f'\nInsert into list time: {timeit.timeit(lambda: test_list.append(new_random_value), number=1):.5f} seconds')
print(f'Insert into dict time: {timeit.timeit(lambda: test_dict.update({len(test_dict): new_random_value}), number=1):.5f} seconds')
print(f'Insert into BST time: {timeit.timeit(lambda: test_BST.insert(new_random_value), number=1):.5f} seconds')
print(f'Insert into LL time: {timeit.timeit(lambda: test_LL.insert(new_random_value), number=1):.5f} seconds')

### DELETION

delete_random_value = random.choice(random_ints)

# delete first key seen if value is found
def delete_from_dict():
    for key, val in test_dict.items():

        if val == delete_random_value:
            del test_dict[key]
            break

print(f'\nDelete from list time: {timeit.timeit(lambda: test_list.remove(delete_random_value), number=1):.5f} seconds')
print(f'Delete from dict time: {timeit.timeit(lambda: delete_from_dict(), number=1):.5f} seconds')
print(f'Delete from BST time: {timeit.timeit(lambda: test_BST.delete(delete_random_value), number=1):.5f} seconds')
print(f'Delete from LL time: {timeit.timeit(lambda: test_LL.delete(delete_random_value), number=1):.5f} seconds')