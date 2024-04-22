import time
import random

# function to generate random integers and store them in list/dict
def generate_ints(quantity, int_list, int_dict):
    
    # loop "quantity" times
    for x in range(quantity):

        rand = random.randint(1,10000) # generate random int

        int_list.append(rand) # fill list
        int_dict[rand] = x # fill dict

# function to measure time of functions
# *args used to pass variable number of arguments
def measure_time(function, *args):

    start = time.time()
    function(*args)
    
    return (time.time() - start)

# function to print list
def print_list(int_list):
    
    for int in int_list:
        print(int)

# function to print dict items
def print_dict(int_dict):

    for key, value in int_dict.items():
        print(f"{key}:{value}")

# find in list
def find_list(int_list, targets):
    
    retrievals = []

    for target in targets:
        # verify if in list
        if target in int_list:
            retrievals.append(target)

    return retrievals

# find in dict
def find_dict(int_dict, targets):

    retrievals = []
    
    for target in targets:
        # verify if in dict
        if target in int_dict:
            retrievals.append(target) 

    return retrievals

# insert in list
def insert_list(int_list, int):
    int_list.append(int)
    print_list(int_list)

# insert in dict
def insert_dict(int_dict, int):
    int_dict[int] = len(int_dict)
    print_dict(int_dict)

# delete from list
def delete_list(int_list, int):
    int_list.remove(int)

# delete from dict
def delete_dict(int_dict, int):
    del int_dict[int]

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
    generate_ints(1000, int_list, int_dict) 

    # PRINT
    list_print.append(measure_time(print_list,int_list))
    dict_print.append(measure_time(print_dict,int_dict))

    # RETRIEVAL
    targets = random.choices(int_list, k = 500)
    list_find.append(measure_time(find_list, int_list, targets))
    dict_find.append(measure_time(find_dict, int_dict, targets))

    # INSERTION
    insert = random.randint(1,10000)
    list_insert.append(measure_time(insert_list, int_list, insert))
    dict_insert.append(measure_time(insert_dict, int_dict, insert))

    # DELETION
    delete = random.choice(int_list)
    list_delete.append(measure_time(delete_list, int_list, delete))
    dict_delete.append(measure_time(delete_dict, int_dict, delete))

print("\nLIST PRINT")
for i, ele in enumerate(list_print):
    print(f"Trial {i}: {ele}")

print("\nDICTIONARY PRINT")
for i, ele in enumerate(dict_print):
    print(f"Trial {i}: {ele}")

print("\nLIST RETRIEVAL")
for i, ele in enumerate(list_find):
    print(f"Trial {i}: {ele}")
    
print("\nDICTIONARY RETRIEVAL")
for i, ele in enumerate(dict_find):
    print(f"Trial {i}: {ele}")

print("\nLIST INSERTION")
for i, ele in enumerate(list_insert):
    print(f"Trial {i}: {ele}")
    
print("\nDICTIONARY INSERTION")
for i, ele in enumerate(dict_insert):
    print(f"Trial {i}: {ele}")

print("\nLIST DELETION")
for i, ele in enumerate(list_delete):
    print(f"Trial {i}: {ele}")
    
print("\nDICTIONARY DELETION")
for i, ele in enumerate(dict_delete):
    print(f"Trial {i}: {ele}")