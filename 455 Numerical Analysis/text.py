# Andrew Kozempel
# CMPSC 455
# Fall 2023
# Lab 3

import math

# function and derivative
def f(x):
    return x**2

def f_prime(x):
    return 2*x

# backward
def backward_difference(x, h):
    return (f(x) - f(x-h)) / h

# forward
def forward_difference(x, h):
    return (f(x+h) - f(x)) / h

# centered
def centered_difference(x, h):
    return (f(x+h) - f(x-h)) / (2*h)

x = 0
actual_derivative = f_prime(x)

bw_prev_error = 0
print('\n\t\t--------BACKWARD DIFFERENCE--------\n')
for i in range(1, 11):
    h = (1/2)**i
    
    backward_approx = backward_difference(x, h)
    backward_error = abs(backward_approx - actual_derivative)

    if bw_prev_error != 0:
        bw_ratio = round(backward_error / bw_prev_error, 2)
    else:
        bw_ratio = ''

    print(f'h = {h:.5f}\t Approximation: {backward_approx:.5f}\t\t Error: {backward_error:.5f}\t\t Error Ratio: {bw_ratio}')

    bw_prev_error = backward_error

fw_prev_error = 0
print('\n\t\t\t--------FORWARD DIFFERENCE--------\n')
for i in range(1, 11):
    h = (1/2)**i
    
    forward_approx = forward_difference(x, h)
    forward_error = abs(forward_approx - actual_derivative)

    if fw_prev_error != 0:
        fw_ratio = round(forward_error / fw_prev_error, 2)
    else:
        fw_ratio = ''

    print(f'h = {h:.5f}\t Approximation: {forward_approx:.5f}\t\t Error: {forward_error:.5f}\t\t Error Ratio: {fw_ratio}')

    fw_prev_error = forward_error

c_prev_error = 0
print('\n\t\t\t--------CENTERED DIFFERENCE--------\n')
for i in range(1, 11):
    h = (1/2)**i
    
    centered_approx = centered_difference(x, h)
    centered_error = abs(centered_approx - actual_derivative)

    if c_prev_error != 0:
        c_ratio = round(centered_error / c_prev_error,2)
    else:
        c_ratio = ''

    print(f'h = {h:.5f}\t Approximation: {centered_approx:.5f}\t\t Error: {centered_error:.5f}\t\t Error Ratio: {c_ratio}')
    
    c_prev_error = centered_error