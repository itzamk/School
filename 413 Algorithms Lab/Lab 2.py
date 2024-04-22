'''
Andrew Kozempel
CMPSC 413
Lab 2
Fall 2023
'''

import time
import timeit

# function to measure time of functions
# *args used to pass variable number of arguments
def measure_time(function, *args, number=1):

    wrapped = lambda: function(*args)  # Wrap the function call in a lambda to handle the arguments
    return timeit.timeit(wrapped, number=number)* 1e9

# Best: O(1)
# Worst: O(n)
def linear_search(lst, target):

    # iterate through list
    for i in range(len(lst)):

        # if element is target, return index
        if lst[i] == target:
            return i
        
# Best: O(1) - mid element
# Worst: O(logn) - first or last
def binary_search(lst, target):

    # assign left and right indices
    left = 0
    right = len(lst) - 1
    
    # while loop until target is found
    while left <= right:

        # calculate mid index
        mid = (left + right) // 2

        # if mid index is target, return index
        if lst[mid] == target:
            return mid
        
        # search right half
        elif lst[mid] < target:
            left = mid + 1

        # search left half
        else:
            right = mid - 1

# Best: O(n) - sorted
# Worst: O(n^2) - reverse
def insertion_sort(lst):

    # loop through list starting at second
    for i in range(1, len(lst)):

        curr = lst[i] # store current element
        j = i - 1 # element before curr

        # while there are elements to the left of curr
        # and curr is less than previous element
        while j >= 0 and curr < lst[j]:

            lst[j + 1] = lst[j] # move element to the right (copy?)
            j -= 1 # move to previous element

        # insert current element in correct spot
        lst[j + 1] = curr
    
    return lst

# Best: O(n^2)
# Worst: O(n^2)
# always compares all elements
def selection_sort(lst):

    # iterate through list
    for i in range(len(lst)):

        # initalize min index
        min_idx = i

        # iterate through unsorted elements
        for j in range(i+1, len(lst)):

            # update min index if smaller elements is found
            if lst[j] < lst[min_idx]:
                min_idx = j

        # swap
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    
    return lst

# Best: O(n) - sorted
# Worst: O(n^2) - reverse
def bubble_sort(lst):

    # length of list
    n = len(lst)

    # iterate through list
    for i in range(n):

        # flag to track swaps
        swapped = False

        # iterate through unsorted (ignore the last i elements)
        for j in range(0, n-i-1):

            # swap if out of order
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True # swap is true

        # break if swapped (sorted)
        if not swapped:
            break
    
    return lst

############################################################
#  PART 2 - STUDENT SORTING
############################################################

# Best: O(1)
# Worst: O(n)
def student_linear_search(lst, target, key):

    # iterate through list
    for i, student in enumerate(lst):

        # if element is target, return index
        if student[key] == target:
            return i

# Best: O(n)
# Worst: O(n^2)
def student_insertion_sort(lst, key):

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
    
    return lst

# Best: O(n^2)
# Worst: O(n^2)
def student_selection_sort(lst, key):

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
    
    return lst

# Best: O(n)
# Worst: O(n^2)
def student_bubble_sort(lst, key):

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

    return lst

# Read file
def read_student_data(filename):

    # store student data
    students = []

    # open the file in read mode
    with open(filename, 'r') as file:

        # read first line to get the headers/column names
        headers = file.readline().strip().split(',')
        
        # loop through each line in the file
        for line in file:

            # split the line into individual data items
            data = line.strip().split(',')
            
            # create a dictionary for each student
            student = {}
            
            # iterate through items in line
            for i in range(len(headers)):
                student[headers[i]] = data[i]
            
            # append the student dictionary to the students list
            students.append(student)
    
    # return the list of student dictionaries
    return students

students_data = read_student_data('students.txt')

#for student in students_data:
#    print(student)

search_value = 7001

print("\n PART 2:\n")

# Linear Search
print(f'Linear search time: {measure_time(student_linear_search, students_data, search_value, "Student ID"):.2f} nanoseconds')

# Insertion Sort
print(f'Insertion sort time: {measure_time(student_insertion_sort, students_data.copy(), "Student ID"):.2f} nanoseconds')

# Selection Sort
print(f'Selection sort time: {measure_time(student_selection_sort, students_data.copy(), "Student ID"):.2f} nanoseconds')

# Bubble Sort
print(f'Bubble sort time: {measure_time(student_bubble_sort, students_data.copy(), "Student ID"):.2f} nanoseconds')

############################################################
#  PART 3 - STUDENT SORTING SORTED
############################################################

print("\n PART 3 (SORTED):\n")

sorted_students_data = student_insertion_sort(students_data.copy(), "first name")

for student in sorted_students_data:
    print(student)

# Insertion Sort
print(f'Insertion sort time: {measure_time(student_insertion_sort, sorted_students_data.copy(), "first name"):.2f} nanoseconds')

# Selection Sort
print(f'Selection sort time: {measure_time(student_selection_sort, sorted_students_data.copy(), "first name"):.2f} nanoseconds')

# Bubble Sort
print(f'Bubble sort time: {measure_time(student_bubble_sort, sorted_students_data.copy(), "first name"):.2f} nanoseconds')

############################################################
#  PART 4 - STUDENT SORTING SAME STUDENT
############################################################

same_student_data = read_student_data('samestudent.txt')

print("\n PART 4 (SAME STUDENT):\n")

# Insertion Sort
print(f'Insertion sort time: {measure_time(student_insertion_sort, same_student_data.copy(), "Student ID"):.2f} nanoseconds')

# Selection Sort
print(f'Selection sort time: {measure_time(student_selection_sort, same_student_data.copy(), "Student ID"):.2f} nanoseconds')

# Bubble Sort
print(f'Bubble sort time: {measure_time(student_bubble_sort, same_student_data.copy(), "Student ID"):.2f} nanoseconds\n')