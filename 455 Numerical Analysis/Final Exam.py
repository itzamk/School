'''
Andrew Kozempel
CMPSC 455
Fall 2023
Final Exam
'''

import math

'''
Question 1
'''

def g(x):

    return (math.exp(x)-1) / x

for i in range(1,16):

    x = 10 ** -i

    print(f'x = 10^{-i}\tAnalytical Limit: {g(x)}')

'''
Question 2
'''

def f(x):

    return x**2 - 8

def df(x):

    return 2*x

def newton(f, df, x, tol):

    i = 0

    while True:
        
        dx = f(x) / df(x)
        x -= dx
        i += 1

        if abs(dx) < tol:
            break

    return x, i

x,i = newton(f, df, 3, 10**-6)

print(f'\nQ2. Root Approximation is {x:.5f} after {i} iterations.\tError = {abs(x-math.sqrt(8)):.5f}')


'''
Question 3
'''

def f(x):
    return x**2 - math.exp(-x)

actual_derivative = 1

prev_error = 0
print('\nQ3:')
for i in range(2, 6):
    h = (1/2)**i
    
    approx = (f(3*h) - 9*f(h) + 8*f(0)) / (-6*h)
    error = abs(approx - actual_derivative)

    if prev_error != 0:
        ratio = round(error / prev_error, 2)
    else:
        ratio = ''

    print(f'h = {h:.5f}\t Approximation: {approx:.5f}\t\t Error: {error:.5f}\t\t Error Ratio: {ratio}')

    prev_error = error

'''
Question 4
'''

print('\nQ4:')

def f(t, y):
    return math.exp(t) * (math.sin(t) + math.cos(t)) + 2 * t

def true(t):
    return math.exp(t) * math.sin(t) + 1

print('\ndelta t = 1/10')

h = 0.1

t = 0
y = 1

while t <= 2.01:

    print(f't = {t:.6f}\ty approx = {y:.6f}\ty true = {true(t):.6f}\terror = {abs(y-true(t)):.6f}')

    prev_y = y
    y = prev_y + h * f(t, prev_y)
    t += h

print('\ndelta t = 1/20')
h = 0.05

t = 0
y = 1

while t <= 2.01:

    print(f't = {t:.6f}\ty approx = {y:.6f}\ty true = {true(t):.6f}\terror = {abs(y-true(t)):.6f}')

    prev_y = y
    y = prev_y + h * f(t, prev_y)
    t += h
 
'''
Question 7
'''

print('\nQ7')
def f(x):
    return (math.sin(x) ** 2) * math.cos(x)

def simpson(f, a, b):
    return (b - a) / 6 * (f(a) + 4 * f((a + b) / 2) + f(b))

exact_integral = 0.270151

h = 1/5

prev_error = 0

while h > 1/160:

    h /= 2

    integral = 0
    n = int(1/h)

    for i in range(n):

        a = i * h
        b = (i+1) * h

        integral += simpson(f, a, b)

    error = abs(exact_integral - integral)

    if prev_error != 0:
        ratio = round(error / prev_error, 2)
    else:
        ratio = ''

    print(f'h = {h:.5f}\t\tApproximation = {integral:.5f}\t\terror = {error:.5f}\t\terror ratio = {ratio}\t\t')
    prev_error = error

     
'''
Question 8
'''

def f(x):
    return math.exp(x**2)

true_val = 0.2553074606

def left_endpoint(f, start, end, delta_x):

    integral = 0
    x = start

    for _ in range(int((end-start)/delta_x)):

        integral += f(x) * delta_x
        x += delta_x

    return integral

def right_endpoint(f, start, end, delta_x):
    
    integral = 0
    x = start

    for _ in range(int((end-start)/delta_x)):

        integral += f(x + delta_x) * delta_x
        x += delta_x

    return integral

def midpoint(f, start, end, delta_x):
    
    integral = 0
    x = start

    for _ in range(int((end-start)/delta_x)):

        integral += f((x + (x+delta_x)) / 2) * delta_x
        x += delta_x

    return integral

def trapezoidal(f, start, end, delta_x):

    integral = 0
    x = start

    for _ in range(int((end-start)/delta_x)):
        
        integral += ((f(x) + f(x+delta_x)) / 2) * delta_x
        x += delta_x

    return integral

start = 0
end = 1/4

prev_left_error = 0
prev_right_error = 0
prev_mid_error = 0
prev_trapezoid_error = 0

print('\nQ8')

for i in range(1,5):

    delta_x = (1/8)**i

    print(f"\n\ndelta_x = 1/{8**i}\n")

    # approximations
    left = left_endpoint(f, start, end, delta_x)
    right = right_endpoint(f, start, end, delta_x)
    mid = midpoint(f, start, end, delta_x)
    trapezoid = trapezoidal(f, start, end, delta_x)

    # errors
    left_error = abs(left-true_val)
    right_error = abs(right-true_val)
    mid_error = abs(mid-true_val)
    trapezoid_error = abs(trapezoid-true_val)

    if prev_left_error + prev_right_error + prev_mid_error + prev_trapezoid_error != 0:
        left_ratio = round(left_error / prev_left_error, 4)
        right_ratio = round(right_error / prev_right_error, 4)
        mid_ratio = round(mid_error / prev_mid_error, 4)
        trapezoid_ratio = round(trapezoid_error / prev_trapezoid_error, 4)
    else:
        left_ratio = ''
        right_ratio = ''
        mid_ratio = ''
        trapezoid_ratio = ''

    print(f"Left endpoint: {left:.5f}\t\t Error: {left_error:.5f}\t\t Error ratio: {left_ratio}")
    print(f"Right endpoint: {right:.5f}\t\t Error: {right_error:.5f}\t\t Error ratio: {right_ratio}")
    print(f"Midpoint: {mid:.5f}\t\t Error: {mid_error:.5f}\t\t Error ratio: {mid_ratio}")
    print(f"Trapezoid: {trapezoid:.5f}\t\t Error: {trapezoid_error:.5f}\t\t Error ratio: {trapezoid_ratio}")
    
    prev_left_error = left_error
    prev_right_error = right_error
    prev_mid_error = mid_error
    prev_trapezoid_error = trapezoid_error