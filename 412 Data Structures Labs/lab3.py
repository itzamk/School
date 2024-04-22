'''
Andrew Kozempel
CMPSC 412
Lab 3
Fall 2023
'''

###################
# PART 1
###################

class QueueStacks:
    def __init__(self):

        # initialize stacks for queue
        self.stackA = []
        self.stackB = []

    def enqueue(self, item):

        # always push onto stack A
        self.stackA.append(item)

    def dequeue(self):

        # if stackB is empty
        if not self.stackB:

            # while stackA is not empty
            while self.stackA:

                # transfer top element of stackA to stackB
                # reverse the order (LIFO -> FIFO)
                self.stackB.append(self.stackA.pop())

        # if stackB is empty, return nothing
        if not self.stackB:
            return None 
        
        # return top of stackB, which was bottom of stackA
        return self.stackB.pop()
    
###################
# PART 2
###################

def isValid(test):

    # create stack for parentheses
    p_stack = []

    # create dict for pair lookup
    pairs = {'(':')', '{':'}', '[':']'}

    # for each character in the test case
    for char in test:

        # if starting bracket, push on to stack
        if char in pairs.keys():
            p_stack.append(char)

        # if closing bracket
        else:

            # if stack is empty, False
            if not p_stack:
                return False
            
            # if open and close bracket dont match, False
            if pairs[p_stack.pop()] != char:
                return False

    # if stack is empty, True
    if not p_stack:
        return True
    
    # if stack if not empty (unmatched parentheses), False
    else:
        return False

# test cases
test_cases = ["[()]", "(", ")", "[(])"]

# test each test case
for test in test_cases:
    print(isValid(test))