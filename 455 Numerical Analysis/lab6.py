'''
Andrew Kozempel
CMPSC 455
Lab 6
29 November 2023
'''

import math

def f(x):
    return math.exp(x)
    #return 3*x**2

true_val = math.exp(1) - 1

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
end = 1

# delta_x = 0.1
delta_x = 0.1
print(f"\n\n\t----- delta_x = {delta_x} -----\n")

# approximations
left = left_endpoint(f, start, end, delta_x)
right = right_endpoint(f, start, end, delta_x)
mid = midpoint(f, start, end, delta_x)
trapezoid = trapezoidal(f, start, end, delta_x)

# errors
left_error1 = abs(left-true_val)
right_error1 = abs(right-true_val)
mid_error1 = abs(mid-true_val)
trapezoid_error1 = abs(trapezoid-true_val)

print(f"Left endpoint approximation: {left:.6f}\t\t Error: {left_error1:.5f}\t\t Error ratio: N/A")
print(f"Right endpoint approximation: {right:.6f}\t\t Error: {right_error1:.5f}\t\t Error ratio: N/A")
print(f"Midpoint approximation: {mid:.6f}\t\t Error: {mid_error1:.5f}\t\t Error ratio: N/A")
print(f"Trapezoid approximation: {trapezoid:.6f}\t\t Error: {trapezoid_error1:.5f}\t\t Error ratio: N/A")

##### delta_x = 0.05
delta_x = 0.05
print(f"\n\n\t----- delta_x = {delta_x} -----\n")

# approximations
left = left_endpoint(f, start, end, delta_x)
right = right_endpoint(f, start, end, delta_x)
mid = midpoint(f, start, end, delta_x)
trapezoid = trapezoidal(f, start, end, delta_x)

# errors
left_error2 = abs(left-true_val)
right_error2 = abs(right-true_val)
mid_error2 = abs(mid-true_val)
trapezoid_error2 = abs(trapezoid-true_val)

print(f"Left endpoint approximation: {left:.6f}\t\t Error: {left_error2:.5f}\t\t Error ratio: {abs(left_error2/left_error1):.2f}")
print(f"Right endpoint approximation: {right:.6f}\t\t Error: {right_error2:.5f}\t\t Error ratio: {abs(right_error2/right_error1):.2f}")
print(f"Midpoint approximation: {mid:.6f}\t\t Error: {mid_error2:.5f}\t\t Error ratio: {abs(mid_error2/mid_error1):.2f}")
print(f"Trapezoid approximation: {trapezoid:.6f}\t\t Error: {trapezoid_error2:.5f}\t\t Error ratio: {abs(trapezoid_error2/trapezoid_error1):.2f}")

##### delta_x = 0.025
delta_x = 0.025
print(f"\n\n\t----- delta_x = {delta_x} -----\n")

# approximations
left = left_endpoint(f, start, end, delta_x)
right = right_endpoint(f, start, end, delta_x)
mid = midpoint(f, start, end, delta_x)
trapezoid = trapezoidal(f, start, end, delta_x)

# errors
left_error3 = abs(left-true_val)
right_error3 = abs(right-true_val)
mid_error3 = abs(mid-true_val)
trapezoid_error3 = abs(trapezoid-true_val)

print(f"Left endpoint approximation: {left:.6f}\t\t Error: {left_error3:.5f}\t\t Error ratio: {abs(left_error3/left_error2):.2f}")
print(f"Right endpoint approximation: {right:.6f}\t\t Error: {right_error3:.5f}\t\t Error ratio: {abs(right_error3/right_error2):.2f}")
print(f"Midpoint approximation: {mid:.6f}\t\t Error: {mid_error3:.5f}\t\t Error ratio: {abs(mid_error3/mid_error2):.2f}")
print(f"Trapezoid approximation: {trapezoid:.6f}\t\t Error: {trapezoid_error3:.5f}\t\t Error ratio: {abs(trapezoid_error3/trapezoid_error2):.2f}")
