# Andrew Kozempel
# CMPSC 455
# Fall 2023
# 10 October 2023 In Class Practice

def f(x):
    
    return x**3 - x - 3

def f_prime(x):

    return 3*x**2 - 1

def bisection(a, b, steps):

    for i in range(steps):

        c = (a + b) / 2.0
        print(c)

        if f(c) == 0:
            return c
        
        elif f(c) * f(a) < 0:
            b = c

        else:
            a = c

    return (a + b) / 2.0

def bisection_tol(a, b, tol):

    while (b - a) / 2.0 > tol:

        c = (a + b) / 2.0
        print(c)

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
        print(x0)

    return x0

def secant(x0, x1, tolerance):

    while abs(x1-x0) >= tolerance:

        x2 = x1 - f(x1) / ((f(x1) - f(x0)) / (x1 - x0))

        print(x2)

        x0 = x1
        x1 = x2

    return x2

newt_tol = secant(0, 0.5, 10**-6)
print("Secant Method: ", newt_tol)

# bisect3 = bisection_tol(0, 2, 10**-3)
# print(f"\nBisection Method (10^-3): {bisect3}")

bisect6 = bisection_tol(0, 2, 10**-6)
print(f"\nBisection Method (10^-6): {bisect6}")

# bisect9 = bisection_tol(0, 2, 10**-9)
# print(f"\nBisection Method (10^-9): {bisect9}")

# newt = newton(1, 10)
# print(f"Newton's Method:  {newt}\n")