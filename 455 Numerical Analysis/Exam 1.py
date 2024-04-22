# Andrew Kozempel
# Exam 1

import math

###### Question 3 #########

print("\nQUESTION 3")

def q3f(x):

    return (x - math.sin(x)) / x**3

x = 1  

for i in range(16):

    print(q3f(x))
    x = 0.1 * x

###### Question 6 #########

print("\nQUESTION 6")

def q6f(x):

    return math.log(x) - 5 + x

def bisection(a, b, steps):

    #c = (a+b)/2

    for i in range(steps):
        
        c = (a+b)/2

        if q6f(c) == 0:
            return c
        
        if q6f(a)*q6f(c) < 0:
            b = c

        else:
            a = c

        print(c)

    print("Root is", c)
    return c

bisection(3,4,10)

###### Question 7 #########

print("\nQUESTION 7")

def q7f(x):

    return x * math.exp(-x)

def q7f_prime(x):

    return -x * math.exp(-x)

def newtons(x):

    iterations = 0

    while abs(x) > 0.001:
        iterations += 1
        x = x - (q7f(x)/q7f_prime(x))

    print(f"Root is {x} after {iterations} iterations")
    return x

#newtons(0.2)

###### Question 8 #########

print("\nQUESTION 8")

def q8f(x):

    return x**2 - 11

def q8f_prime(x):

    return 2*x

def steps_newtons(x, steps):

    for i in range(steps):
        x = x - (q8f(x)/q8f_prime(x))
        print(x)

    print(f"Root is {x}")
    return x

steps_newtons(1.5,10)