# Andrew Kozempel
# Exam 2

# function for 1-4
def f(x):
    return x**3 - 7*x**2 + 1 

# first derivative
def df(x):
    return 3*x**2 - 14*x

# second derivative
def df2(x):
    return 6*x - 14

# forward, centered, backward diff
def forward_difference(f, x, h):
    return (f(x + h) - f(x)) / h

def backward_difference(f, x, h):
    return (f(x) - f(x - h)) / h

def centered_difference(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

# Question 1+2

print('\nQuestion 1 and 2:')
error = 0
for i in range(1,11):

    h = 0.5 ** i

    if error == 0:
        ratio = 0
    else:
        ratio = abs((forward_difference(f, 1, h) - df(1)) / error)

    print(f'i = {i}\th = {h:.6f}\tApproximation = {forward_difference(f, 1, h):.6f}\terror = {error:.6f}\terror ratio= {ratio:.6f}')

    error = abs(forward_difference(f, 1, h) - df(1))

# Question 3+4

print('\nQuestion 3 and 4:')

def central_diff_2nd_deriv(f, x, h):
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h ** 2)

error = 0
for i in range(1,11):

    h = 0.5 ** i

    if error == 0:
        ratio = 0
    else:
        ratio = abs((central_diff_2nd_deriv(f, 1, h) - df2(1)) / error)

    print(f'h = {h:.6f}\tApproximation = {central_diff_2nd_deriv(f, 1, h):.6f}\terror = {error:.6f}\terror ratio= {ratio:.6f}')

    error = abs(central_diff_2nd_deriv(f, 1, h) - df2(1))

# Question 5
print('\nQuestion 5:')

import math

def f(x):
    return math.exp(2*x - 1)

def df(x):
    return 2 * math.exp((2*x - 1))

def three_point_forward_diff(f, x, h):
    return (-3*f(x) + 4*f(x + h) - f(x + 2*h)) / (2*h)

def three_point_backward_diff(f, x, h):
    return (3*f(x) - 4*f(x - h) + f(x - 2*h)) / (2*h)

# interval [0,1], h = 0.1
x = 0
h = 0.1

error = 0
while x <= 1:

    if error == 0:
        ratio = 0
    else:
        ratio = abs((three_point_forward_diff(f, x, h) - df(x)) / error)

    error = abs(three_point_forward_diff(f, x, h) - df(x))
    print(f'x = {x:.6f}\tApproximation = {three_point_forward_diff(f, x, h):.6f}\tTrue = {df(x):.6f}\terror = {error:.6f}\terror ratio= {ratio:.6f}')

    x += h

# Question 6
print('\nQuestion 6:')

# function and first 3 derivatives
def f(x):
    return 2 * math.exp(-x)
def df(x):
    return - 2 * math.exp(-x)
def df_2(x):
    return 2 * math.exp(-x)
def df_3(x):
    return - 2 * math.exp(-x)

# approx. formula
def third_deriv(f, x, h):
    return (f(x + 2*h) - (2 * f(x + h)) + (2 * f(x - h)) - f(x - 2*h)) / (2 * h**3)

# x and h values
x = 0
h = 0.1

for i in range(1,4):

    h = h ** i

    if error == 0:
        ratio = 0
    else:
        ratio = abs((third_deriv(f, x, h) - df_3(x)) / error)

    print(f'i = {i}\th = {h:.6f}\tApproximation = {third_deriv(f, x, h):.6f}\terror = {error:.6f}\terror ratio= {ratio:.6f}')

    error = abs(third_deriv(f, x, h) - df_3(x))


# Question 7
print('\nQuestion 7:')

def f(t, y):
    return y - t

def true(t):
    return (t + 1) - 2 * math.exp(t)

h = 0.1 # step size

t = 0 # initial t value
y = -1 # initial y

while t <= 1:

    print(f't = {t:.6f}\ty approx = {y:.6f}\ty true = {true(t):.6f}\terror = {abs(y-true(t)):.6f}')

    prev_y = y
    y = prev_y + h * f(t, prev_y)
    t += h