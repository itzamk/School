'''
Andrew Kozempel
CMPSC 413
Lab 1
Fall 2023
'''

import math
import random
import time

############################################################
#  PART 1 - GCD
############################################################

# best case: O(1)
# if element is first list
# worst case: O(n), n = min(num1,num2)
# if all elements within range are checked
def GCD(num1, num2):

    # get start time
    start = time.time_ns()

    # test numbers ranging from the smaller number to 1
    for i in range(min(num1,num2), 0, -1):

        # if both numbers are divisible by i, return i and total time
        if num1 % i == 0 and num2 % i == 0:
            return i, time.time_ns() - start

# Test cases
gcd_test_cases = [(100, 25), 
                  (48, 18), 
                  (17, 5),
                  (12345, 67890),
                  (234567, 765432)]

# print calculated and expected result, as well as total time
print("\n\tPART 1: GCD")
for a, b in gcd_test_cases:

    gcd, gcd_time = GCD(a,b)

    print(f"\nTesting: {a}, {b} \
          \nResult: {gcd} \
          \nExpected: {math.gcd(a,b)} \
          \nTime: {gcd_time} nanoseconds")


############################################################
#  PART 2 - Min/Max
############################################################

# O(n)
# iterates through all elements
def find_max(list):

    # get start time
    start = time.time_ns()

    # initialize max as first element for future comparisons
    max = list[0]

    # iterate through all elements in the list
    for i in list:

        # if i is larger than max, i is new max
        if i > max:
            max = i

    # return max and total time
    return max, time.time_ns() - start

# O(n)
def find_min(list):

    # get start time
    start = time.time_ns()

    # initialize min as first element for future comparisons
    min = list[0]

    # iterate through all elements in the list
    for i in list:

        # if i is larger than max, assign it as max
        if i < min:
            min = i

    # return min and total time
    return min, time.time_ns() - start

# test cases for 1000 and 10000 numbers
minmax_test_cases = [[],[]]

for i in range(1000):
    minmax_test_cases[0].append(random.randint(1,100000))

for i in range(10000):
    minmax_test_cases[1].append(random.randint(1,100000))

# print min and max values
print("\n\tPART 2: MIN AND MAX")
for test in minmax_test_cases:

    min_val, min_time = find_min(test)
    max_val, max_time = find_max(test)

    print(f"\nTesting: {len(test)} elements \
          \nResult:   Min: {min_val}, Max: {max_val} \
          \nExpected: Min: {min(test)}, Max: {max(test)} \
          \nMin Time: {min_time} nanoseconds \
          \nMax Time: {max_time} nanoseconds")
    
############################################################
#  PART 3 - Min/Max
############################################################

# O(n)
def daq_max(list, left, right):

    # if list has 1 element, return element
    if left == right:
        return list[left]
        
    else:

        # find mid index
        mid = (right + left) // 2

        # recursively find max in each half
        max_left = daq_max(list, left, mid)
        max_right = daq_max(list, mid+1, right)

        # return the max of both sides
        if max_left > max_right:
            return max_left
        else:
            return max_right

# O(n)
def daq_min(list, left, right):

    # if list has 1 element, return element
    if left == right:
        return list[left]
        
    else:

        # find mid index
        mid = (right + left) // 2

        # recursively find min in each half
        min_left = daq_min(list, left, mid)
        min_right = daq_min(list, mid+1, right)

        # return the min of both sides 
        if min_left < min_right:
            return min_left
        else:
            return min_right

# print min and max values
print("\n\tPART 3: DIVIDE AND CONQUER")
for test in minmax_test_cases:

    # assign left and right indices
    right = len(test)-1
    left = 0

    # find max and calculate time
    daq_max_start = time.time_ns()
    daq_max_val = daq_max(test, left, right)
    daq_max_time = time.time_ns() - daq_max_start

    # find min and calculate time
    daq_min_start = time.time_ns()
    daq_min_val = daq_min(test, left, right)
    daq_min_time = time.time_ns() - daq_min_start

    # print results
    print(f"\nTesting: {len(test)} elements \
          \nResult:   Min: {daq_min_val}, Max: {daq_max_val} \
          \nExpected: Min: {min(test)}, Max: {max(test)} \
          \nMin Time: {daq_min_time} nanoseconds\
          \nMax Time: {daq_max_time} nanoseconds")