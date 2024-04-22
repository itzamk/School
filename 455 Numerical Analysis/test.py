def f(x):
    return x**3 - 7*(x**2) + 1

def forward_difference(f, x, h):
    return (f(x + h) - f(x)) / h

def backward_difference(f, x, h):
    return (f(x) - f(x - h)) / h

hs = [0.5, 0.25, 0.125, 0.0625]

error = 1
for h in hs:

    ratio = abs(forward_difference(f, 1, h)+11) / error

    print(f'h = {h}\t\tapprox = {abs(forward_difference(f, 1, h)+11)}\t\tratio = {ratio:.6}')
    error = abs(forward_difference(f, 1, h)+11)

error = 1
for h in hs:

    ratio = abs(backward_difference(f, 1, h)+11) / error

    print(f'h = {h}\t\tapprox = {abs(backward_difference(f, 1, h)+11)}\t\tratio = {ratio:.6}')
    error = abs(backward_difference(f, 1, h)+11)

def central_difference_second_derivative(f, x, h):
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h ** 2)

hs = [0.25, 0.125, 0.0625]

error = 1
for h in hs:

    ratio = abs(central_difference_second_derivative(f, 1, h)+11) / error

    print(f'h = {h}\t\tapprox = {central_difference_second_derivative(f, 1, h)}\t\terror = {abs(central_difference_second_derivative(f, 1, h)+8)}\t\tratio = {ratio:.6}')
    error = abs(central_difference_second_derivative(f, 1, h)+11)

# 5 and 6
import math

def f(x):
    return math.exp(2*x + 1)

# Derivative approximations
def three_point_approximation(f, x, h):
    return (-f(x + 2*h) + 4*f(x + h) - 3*f(x)) / (2*h)

def centered_difference(f, x, h):
    return (f(x + h) - f(x - h)) / (2*h)

xs = [0, 0.2, 0.4, 0.6, 0.8, 1]

for x in xs:

    print(f'x val = {x}\t\tapprox = {three_point_approximation(f, x, 0.2):.6f}')

xs = [0.2, 0.4, 0.6, 0.8]

for x in xs:

    print(f'x val = {x}\t\tapprox = {centered_difference(f, x, 0.2):.6f}')

# q8-10

def central_difference_third_derivative(func, x, h):
    return (func(x + 2 * h) - 2 * func(x + h) + 2 * func(x - h) - func(x - 2 * h)) / (2 * h ** 3)

def f(x):
    return math.exp(-2 * x)

h_values_new = [0.2, 0.1, 0.05]

# Initialize the error for the first iteration
error = 1

# Iterating over the provided h values
for h in h_values_new:
    
    ratio = abs(central_difference_third_derivative(f, 0, h) + 8) / error

    print(f'h = {h:.2f}\t\tapprox = {central_difference_third_derivative(f, 0, h):.6f}\t\terror = {abs(central_difference_third_derivative(f, 0, h) + 8):.6f}\t\tratio = {ratio:.6f}')
    error = abs(central_difference_third_derivative(f, 0, h) + 8)

import math

# interval [0,1]
x = 0 # start
y = -1 # initial y value
h = 0.2 # step size

# function of y'
def f(x, y):
    return y - x

# function for true value
def true(x):
    return (x + 1) - 2 * math.exp(x)

# Initialize the error for the first iteration
error = 1

# Iterating over the interval [0,1]
while x <= 1:
    y_true = true(x)
    current_error = abs(y - y_true)
    ratio = current_error / error if error != 0 else 0

    print(f'x = {x:.2f}\t\ty = {y:.6f}\t\ttrue = {y_true:.6f}\t\terror = {current_error:.6f}\t\tratio = {ratio:.6f}')
    
    error = current_error
    y = y + h * f(x, y) # Update y for the next iteration
    x += h