'''
Andrew Kozempel
CMPSC 412
Lab 1
Fall 2023
'''

import time
import random

# function to generate random integers and store them in list/dict
def generate_ints(quantity, int_list, int_dict):
    
    # loop "quantity" times
    for x in range(quantity):

        rand = random.randint(1,10000) # generate random int

        int_list.append(rand) # fill list
        int_dict[x] = rand # fill dict

# function to measure time of functions
# *args used to pass variable number of arguments
def measure_time(function, *args):

    start = time.time_ns() # start time
    function(*args) # perform specified function
    
    return (time.time_ns() - start) # return total time

# function to print list
def print_list(int_list):
    
    # loop through list and print elements
    for int in int_list:
        print(int)

# function to print dict items
def print_dict(int_dict):

    # loop through dict and print key, value pairs
    for key, value in int_dict.items():
        print(f"{key}:{value}")

# find in list
def find_list(int_list, target):
    
    # loop through list, return if target is found
    for int in int_list:
        if int == target:
            return int_list[int]

# find in dict
def find_dict(int_dict, target):

    # loop through dict, return if target is found
    for key, value in int_dict.items():
        if value == target:
            return int_dict[key]

# insert in list
def insert_list(int_list, int):
    int_list.append(int) # append alement
    print_list(int_list) # print list

# insert in dict
def insert_dict(int_dict, int):
    int_dict[int] = len(int_dict) # add key, value
    print_dict(int_dict) # print dict

# delete from list
def delete_list(int_list, int):

    # loop through list and delete element
    for i in int_list:
        if i == int:
            int_list.remove(int)
            break

# delete from dict
def delete_dict(int_dict, int):

    # loop through dict and delete element
    for key, value in int_dict.items():
        if value == int:
            del int_dict[key]
            break

# lists to store times
list_print = []
list_find = []
list_insert = []
list_delete = []
dict_print = []
dict_find = []
dict_insert = []
dict_delete = []

# perform 3 trials, store times
for i in range(3):

    int_list = []
    int_dict = {}
    generate_ints(100000, int_list, int_dict) 

    # PRINT
    list_print.append(measure_time(print_list,int_list))
    dict_print.append(measure_time(print_dict,int_dict))

    # RETRIEVAL
    target = random.choice(int_list)
    list_find.append(measure_time(find_list, int_list, target))
    dict_find.append(measure_time(find_dict, int_dict, target))

    # INSERTION
    insert = random.randint(1,10000)
    list_insert.append(measure_time(insert_list, int_list, insert))
    dict_insert.append(measure_time(insert_dict, int_dict, insert))

    # DELETION
    delete = random.choice(int_list)
    list_delete.append(measure_time(delete_list, int_list, delete))
    dict_delete.append(measure_time(delete_dict, int_dict, delete))

# PRINT OUTPUT
print("\nLIST PRINT")
for i, ele in enumerate(list_print):
    print(f"Trial {i+1}: {ele}")

print("\nDICTIONARY PRINT")
for i, ele in enumerate(dict_print):
    print(f"Trial {i+1}: {ele}")

print("\nLIST RETRIEVAL")
for i, ele in enumerate(list_find):
    print(f"Trial {i+1}: {ele}")
    
print("\nDICTIONARY RETRIEVAL")
for i, ele in enumerate(dict_find):
    print(f"Trial {i+1}: {ele}")

print("\nLIST INSERTION")
for i, ele in enumerate(list_insert):
    print(f"Trial {i+1}: {ele}")
    
print("\nDICTIONARY INSERTION")
for i, ele in enumerate(dict_insert):
    print(f"Trial {i+1}: {ele}")

print("\nLIST DELETION")
for i, ele in enumerate(list_delete):
    print(f"Trial {i+1}: {ele}")
    
print("\nDICTIONARY DELETION")
for i, ele in enumerate(dict_delete):
    print(f"Trial {i+1}: {ele}")