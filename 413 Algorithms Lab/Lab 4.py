'''
Andrew Kozempel
CMPSC 413
Lab 4
Fall 2023
'''

import heapq

#### PART 1 - ARRAY ####

class PQ_Array:

    # initialize with is_max flag for sorting
    def __init__(self, is_max=True):
        self.queue = []
        self.is_max = is_max

    # insert/append
    def insert(self, item, priority):
        self.queue.append((item, priority))

        # sort based on min or max
        self.queue.sort(key=lambda x: x[1], reverse=self.is_max)

    # get first element if not empty
    def peek(self):

        if self.queue:
            return self.queue[0]  
        
        else:
            return None

    # delete first element if not empty
    def delete(self):

        if self.queue:
            return self.queue.pop(0)
        
        else:
            return None

    # change elements priority
    def change_priority(self, item, new_priority):

        # for index and tuple pair
        for i, (ele, priority) in enumerate(self.queue):

            # if element is the item
            if ele == item:

                # change elements priority and sort
                self.queue[i] = (item, new_priority)
                self.queue.sort(key=lambda x: x[1], reverse=self.is_max)

#### PART 2 - Linked List ####

# node class for linked list
class Node:

    # initialize node with item, priority
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority
        self.next = None

class PQ_LinkedList:

    # initialize empty linked list
    def __init__(self, is_max=True):
        self.head = None
        self.is_max = is_max

    # str method to help with printing later
    def __str__(self):

        # current pointer
        current = self.head
        # list to store tuples
        elements = []
        
        # if LL is empty
        if self.head is None:
            return '[]'
        
        # cycle through elements and add to list
        while current is not None:
            elements.append(f'({current.item}, {current.priority})')
            current = current.next

        # return elements
        return "\t" + " -> ".join(elements)

    def insert(self, item, priority):

        # create new node based on element and priority
        new_node = Node(item, priority)

        if self.is_max:

            # if LL is empty or new node priority is greater than head's
            if self.head is None or new_node.priority > self.head.priority:

                # insert new node at beginning
                new_node.next = self.head
                self.head = new_node

            # if LL is not empty
            else:

                # current pointer
                current = self.head

                # cycle through elements until 
                # you get to correct priority position
                while current.next is not None and current.next.priority >= new_node.priority:
                    current = current.next

                # add node to position you just determined (insert after current)
                new_node.next = current.next
                current.next = new_node

        else:

            # if LL is empty or new node priority is less than head's
            if self.head is None or new_node.priority < self.head.priority:

                # insert new node at beginning
                new_node.next = self.head
                self.head = new_node

            # if LL is not empty
            else:

                # current pointer
                current = self.head

                # cycle through elements until 
                # you get to correct priority position
                while current.next is not None and current.next.priority <= new_node.priority:
                    current = current.next

                # add node to position you just determined
                new_node.next = current.next
                current.next = new_node

    def peek(self):

        # if LL not empty, return head values
        if self.head:
            return (self.head.item, self.head.priority)
        else:
            return None
        
    def delete(self):

        # if LL not empty, return head values
        if self.head:

            # store values to return
            item = self.head.item
            priority = self.head.priority

            # make second item the new head
            self.head = self.head.next

            # return values
            return item, priority
        
        else:
            return None

    def change_priority(self, item, new_priority):

        # current and previous pointer
        current = self.head
        previous = None
        
        # cycle through items
        while current:

            # if current item is found
            if current.item == item:

                # if not first item/head
                if previous is not None:

                    # remove/unlink current from LL
                    previous.next = current.next

                # if first item/head
                else:
                    # remove/unlink head/current
                    self.head = current.next    

                # break after removed
                break

            # shift previous and current up
            previous = current
            current = current.next

        if current:

            # update priority and re insert item
            current.priority = new_priority
            self.insert(current.item, current.priority)
        
#### PART 3 - Min/Max Heaps ####

class PQ_Heap:

    # intitialize heap as list
    def __init__(self, is_max=True):
        self.heap = []
        self.is_max = is_max

    # insert using heapq.heappush 
    def insert(self, item, priority):
        
        if self.is_max:
            # (negated priority) if max heap
            heapq.heappush(self.heap, (-priority, item))
        else:
            heapq.heappush(self.heap, (priority, item))


    def peek(self):

        # if heap is not empty
        if self.heap:

            if self.is_max:
            
                # return item with max priority (negate)
                priority, item = self.heap[0]
                return item, -priority
            
            else:
                # return item with min priority 
                priority, item = self.heap[0]
                return item, priority
            
        return None

    def delete(self):

        # if heap is not empty
        if self.heap:

            if self.is_max:
                # delete and return item with max priority (negate)
                priority, item = heapq.heappop(self.heap)
                return item, -priority
        
            else:
                # delete and return item with min priority 
                priority, item = heapq.heappop(self.heap)
                return item, priority
        
        return None

    def change_priority(self, item, new_priority):

        # iterate through elements in heap
        for i, (priority, ele) in enumerate(self.heap):

            # if item is found
            if ele == item:

                if self.is_max:
                    # set new priority based on index and rearrange
                    self.heap[i] = (-new_priority, item)
                    break
                
                else:  
                    # set new priority based on index and rearrange
                    self.heap[i] = (new_priority, item)
                    break
        
        # reorganize to maintain heap property
        heapq.heapify(self.heap)
        return     
    
# EXAMPLES

###### Part 1: Array
print("\nPart 1: Array")
max_pq_array = PQ_Array(is_max=True)
min_pq_array = PQ_Array(is_max=False)

print("\nMax Priority Queue (Array):")
print("\tMax PQ Array:", max_pq_array.queue)
max_pq_array.insert('A', 1)
max_pq_array.insert('B', 2)
print("\tMax PQ Array after insert:", max_pq_array.queue)
max_pq_array.change_priority('A', 4)
print("\tMax PQ Array after priority change:", max_pq_array.queue)
print("\tMax PQ Array Peak:", max_pq_array.peek())
print("\tMax PQ Array deletion return value:",max_pq_array.delete())
print("\tMax PQ Array after delete:", max_pq_array.queue)

print("\nMin Priority Queue (Array):")
print("\tMin PQ Array:", min_pq_array.queue)
min_pq_array.insert('A', 1)
min_pq_array.insert('B', 2)
print("\tMin PQ Array after insert:", min_pq_array.queue)
min_pq_array.change_priority('A', 4)
print("\tMin PQ Array after priority change:", min_pq_array.queue)
print("\tMin PQ Array Peek:", min_pq_array.peek())
print("\tMin PQ Array deletion return value:", min_pq_array.delete())
print("\tMin PQ Array after delete:", min_pq_array.queue)

###### Part 2: Linked List
print("\nPart 2: Linked List")
max_pq_ll = PQ_LinkedList(is_max=True)
min_pq_ll = PQ_LinkedList(is_max=False)

print("\nMax Priority Queue (Linked List):")
print('\tMax PQ LL:', max_pq_ll)
max_pq_ll.insert('A', 1)
max_pq_ll.insert('B', 2)
print("\tMax PQ LL after insert:")
print(max_pq_ll)
max_pq_ll.change_priority('A', 4)
print("\tMax PQ LL after priority change:")
print(max_pq_ll)
print("\tMax PQ LL Peek:", max_pq_ll.peek())
print("\tMax PQ LL deletion return value:", max_pq_ll.delete())
print("\tMax PQ LL after delete:", max_pq_ll)

print("\nMin Priority Queue (Linked List):")
print('\tMin PQ LL:', min_pq_ll)
min_pq_ll.insert('A', 1)
min_pq_ll.insert('B', 2)
print("\tMin PQ LL after insert:")
print(min_pq_ll)
min_pq_ll.change_priority('A', 4)
print("\tMin PQ LL after priority change:")
print(min_pq_ll)
print("\tMin PQ LL Peek:", min_pq_ll.peek())
print("\tMin PQ LL deletion return value:", min_pq_ll.delete())
print("\tMin PQ LL after delete:", min_pq_ll)

###### Part 3: Heap
print("\nPart 3: Heap")
max_pq_heap = PQ_Heap(is_max=True)
min_pq_heap = PQ_Heap(is_max=False)

print("\nMax Priority Queue (Heap):")
print("\tMax PQ Heap:", max_pq_heap.heap)
max_pq_heap.insert('A', 1)
max_pq_heap.insert('B', 2)
print("\tMax PQ Heap after insert:", max_pq_heap.heap)
max_pq_heap.change_priority('A', 4)
print("\tMax PQ Heap after priority change:", max_pq_heap.heap)
print("\tMax PQ Heap Peek:", max_pq_heap.peek())
print("\tMax PQ Heap deletion return value:", max_pq_heap.delete())
print("\tMax PQ Heap after delete:", max_pq_heap.heap)

print("\nMin Priority Queue (Heap):")
print("\tMin PQ Heap:", min_pq_heap.heap)
min_pq_heap.insert('A', 1)
min_pq_heap.insert('B', 2)
print("\tMin PQ Heap after insert:", min_pq_heap.heap)
min_pq_heap.change_priority('A', 4)
print("\tMin PQ Heap after priority change:", min_pq_heap.heap)
print("\tMin PQ Heap Peek:", min_pq_heap.peek())
print("\tMin PQ Heap deletion return value:", min_pq_heap.delete())
print("\tMin PQ Heap after delete:", min_pq_heap.heap)