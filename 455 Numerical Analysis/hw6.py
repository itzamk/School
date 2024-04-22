# Andrew Kozempel
# CMPSC 455
# Fall 2023
# HW 6

def f(x):
    
    return x**2 - 2

def f_prime(x):

    return 2*x

def bisection(a, b, steps):

    for i in range(steps):

        c = (a + b) / 2.0

        if f(c) == 0:
            return c
        
        elif f(c) * f(a) < 0:
            b = c

        else:
            a = c

    return (a + b) / 2.0

def newton(x0, steps):

    for i in range(steps):

        x0 = x0 - f(x0) / f_prime(x0)

    return x0

bisect = bisection(0, 2, 6)
print(f"\nBisection Method: {bisect}")

newt = newton(1, 6)
print(f"Newton's Method:  {newt}\n")