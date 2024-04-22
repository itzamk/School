# Andrew Kozempel
# CMPSC 455
# Fall 2023
# HW 5

import math

#####################
# QUESTION 3: PART A
#####################

print('\n=====QUESTION 3: PART A=====\n')

def lhospital(x):

    return (math.exp(x)-math.exp(-x))/x

for i in range(1,19):
    
    x = 10**-(i)

    print(f'10^-{i} --> {lhospital(x)}')

    
#####################
# QUESTION 3: PART B
#####################

print('\n=====QUESTION 3: PART B=====\n')

def e(x):

    return 1 + x + (x**2) / 2

def lhospital2(x):

    return (e(x)-e(-x))/x

for i in range(1,19):
    
    x = 10**-(i)

    print(f'10^-{i} --> {lhospital2(x)}')