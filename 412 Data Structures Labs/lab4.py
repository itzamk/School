'''
Andrew Kozempel
CMPSC 412
Lab 4
Fall 2023

VIDEO
'''

import sys
import timeit
import tracemalloc

############################################################
#  PART 1 - Binary Search Guesser
############################################################

# Best: O(1) - mid element
# Worst: O(logn) - first or last
def binsearch_guess(lst):

    # print length of list
    print("Guessing your number from list of length", len(lst))

    # assign left and right indices
    left = 0
    right = len(lst) - 1
    
    # while loop until target is found
    while left <= right:

        # calculate mid index
        mid = (left + right) // 2

        # print memory usage
        print(f"\nMemory usage of variable 'lst': {sys.getsizeof(lst[left:right])} bytes")
        print(f"Memory usage of variable 'low': {sys.getsizeof(left)} bytes")
        print(f"Memory usage of variable 'high': {sys.getsizeof(right)} bytes")
        print(f"Memory usage of variable 'mid': {sys.getsizeof(mid)} bytes")

        # initialize answer to guess
        answer = 0

        # loop to get a valid user input
        while answer not in [1,2,3]:
        
            answer = int(input(f'Is your number less than (1), greater than (2), or equal to (3) {lst[mid]}? '))

        # if mid index is target, return index
        if answer == 3:
            print(f'\nYour number is {lst[mid]}.')
            return lst[mid]
        
        # search right half if greater than guess
        elif answer == 2:
            left = mid + 1

        # search left half if less than guess
        else:
            right = mid - 1

# generate list for binary search
def generate_ints(quantity, int_list):
    
    # loop "quantity" times
    for x in range(1, quantity+1):

        int_list.append(x) # fill list

test_list = []
generate_ints(10000, test_list)

# perform guessing game
binsearch_guess(test_list)

############################################################
#  PART 2 - STUDENT SORTING
############################################################

# function to measure time of functions
# *args used to pass variable number of arguments
def measure_time(function, *args, number=1):

    wrapped = lambda: function(*args)  # Wrap the function call in a lambda to handle the arguments
    return timeit.timeit(wrapped, number=number)* 1e9

# function to read students file and store as list of dictionaries
def read_students_from_file(filename):

    # initialize list
    students = []
    
    # read from file
    with open(filename, "r") as file:

        # for each line, split info and store info for each student
        for line in file:
            student_id, first_name, last_name, email_id, major = line.split()
            students.append({
                "Student_ID": int(student_id),
                "first_name": first_name,
                "last_name": last_name,
                "email_id": email_id,
                "major": major
            })
    
    return students

# function to write the sorted list to new file
def write_sorted_to_file(sorted_list, filename):
    with open(filename, 'w') as file:

        # write the info for each student on a new line
        for student in sorted_list:
            line = f"{student['Student_ID']} {student['first_name']} {student['last_name']} {student['email_id']} {student['major']}\n"
            file.write(line)

# Best: O(n)
# Worst: O(n^2)
def insertion_sort(lst, key, filename):

    # start tracing memory allocations
    tracemalloc.clear_traces() # reset memory allocation
    tracemalloc.start()

    # loop through list starting at second
    for i in range(1, len(lst)):

        curr = lst[i] # store current element
        j = i - 1 # element before curr

        # while there are elements to the left of curr
        # and curr is less than previous element
        while j >= 0 and curr[key] < lst[j][key]:

            lst[j + 1] = lst[j] # move element to the right (copy)
            j -= 1 # move to previous element

        # insert current element in correct spot
        lst[j + 1] = curr

    # get current and peak mem allocation
    current, peak = tracemalloc.get_traced_memory()
    
    # stop tracing memory allocations
    tracemalloc.stop()

    # print the memory usage
    print(f"Memory used during sorting: {current} bytes")
    print(f"Peak memory used during sorting: {peak} bytes")

    write_sorted_to_file(lst, filename)
    
    return lst

# Best: O(n^2)
# Worst: O(n^2)
def selection_sort(lst, key, filename):

    # start tracing memory allocations
    tracemalloc.clear_traces() # reset memory allocation
    tracemalloc.start()

    # iterate through list
    for i in range(len(lst)):

        # initalize min index
        min_idx = i

        # iterate through unsorted elements
        for j in range(i+1, len(lst)):

            # update min index if smaller elements is found
            if lst[j][key] < lst[min_idx][key]:
                min_idx = j

        # swap
        lst[i], lst[min_idx] = lst[min_idx], lst[i]

    # get current and peak mem allocation
    current, peak = tracemalloc.get_traced_memory()
    
    # stop tracing memory allocations
    tracemalloc.stop()

    # print the memory usage
    print(f"Memory used during sorting: {current} bytes")
    print(f"Peak memory used during sorting: {peak} bytes")

    write_sorted_to_file(lst, filename)
    
    return lst

# Best: O(n)
# Worst: O(n^2)
def bubble_sort(lst, key, filename):

    # start tracing memory allocations
    tracemalloc.clear_traces() # reset memory allocation
    tracemalloc.start()

    # length of list
    n = len(lst)

    # iterate through list
    for i in range(n):

        # flag to track swaps
        swapped = False

        # iterate through unsorted (ignore the last i elements)
        for j in range(0, n-i-1):

            # swap if out of order
            if lst[j][key] > lst[j+1][key]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True # swap is true

        # break if swapped (sorted)
        if not swapped:
            break

    # get current and peak mem allocation
    current, peak = tracemalloc.get_traced_memory()
    
    # stop tracing memory allocations
    tracemalloc.stop()

    # print the memory usage
    print(f"Memory used during sorting: {current} bytes")
    print(f"Peak memory used during sorting: {peak} bytes")

    write_sorted_to_file(lst, filename)

    return lst

# Best: O(nlogn)
# Worst: O(nlogn)
def _merge_sort(lst, key):
    
    # base case: return list if 1 or 0
    if len(lst) <= 1:
        return lst
    
    # split in half
    middle = len(lst) // 2
    left_half = lst[:middle]
    right_half = lst[middle:]
    
    # recursively sort and merge the halves
    return merge(_merge_sort(left_half, key), _merge_sort(right_half, key), key)

# merge portion
def merge(left, right, key):
    
    # create temp merge
    merged = []

    # initialize indices
    left_idx, right_idx = 0, 0

    # while both halves are not empty
    while left_idx < len(left) and right_idx < len(right):

        # add from left half if element is smaller
        if left[left_idx][key] < right[right_idx][key]:
            merged.append(left[left_idx])
            left_idx += 1
            
        # add from right half if element is smaller
        else:
            merged.append(right[right_idx])
            right_idx += 1
    
    # add extra elements from either list, if any
    return merged + left[left_idx:] + right[right_idx:]

def merge_sort(lst, key, filename):

    # start tracing memory allocations
    tracemalloc.clear_traces() # reset memory allocation
    tracemalloc.start()

    # perform merge sort
    lst = _merge_sort(lst, key)

    # get current and peak mem allocation
    current, peak = tracemalloc.get_traced_memory()
    
    # stop tracing memory allocations
    tracemalloc.stop()

    # print the memory usage
    print(f"Memory used during sorting: {current} bytes")
    print(f"Peak memory used during sorting: {peak} bytes")

    write_sorted_to_file(lst, filename)

    return lst

students = read_students_from_file("students.txt")

# sort by ID

print('\n---SORTING BY ID---')

print('\nINSERTION SORT:')
print(f"Time Taken: {measure_time(insertion_sort, students.copy(), 'Student_ID', 'insertion_id.txt'):.2f} nanoseconds")

print('\nSELECTION SORT:')
print(f"Time Taken: {measure_time(selection_sort, students.copy(), 'Student_ID','selection_id.txt'):.2f} nanoseconds")

print('\nBUBBLE SORT:')
print(f"Time Taken: {measure_time(bubble_sort, students.copy(), 'Student_ID','bubble_id.txt'):.2f} nanoseconds")

print('\nMERGE SORT:')
print(f"Time Taken: {measure_time(merge_sort, students.copy(), 'Student_ID','merge_id.txt'):.2f} nanoseconds")

# sort by first name

print('\n---SORTING BY FIRST NAME---')

print('\nINSERTION SORT:')
print(f"Time Taken: {measure_time(insertion_sort, students.copy(), 'first_name', 'insertion_fn.txt'):.2f} nanoseconds")

print('\nSELECTION SORT:')
print(f"Time Taken: {measure_time(selection_sort, students.copy(), 'first_name','selection_fn.txt'):.2f} nanoseconds")

print('\nBUBBLE SORT:')
print(f"Time Taken: {measure_time(bubble_sort, students.copy(), 'first_name','bubble_fn.txt'):.2f} nanoseconds")

print('\nMERGE SORT:')
print(f"Time Taken: {measure_time(merge_sort, students.copy(), 'first_name','merge_fn.txt'):.2f} nanoseconds")