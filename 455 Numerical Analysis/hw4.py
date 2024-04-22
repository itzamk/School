def forward_difference(f, x, h):
    return (f(x + h) - f(x)) / h
def backward_difference(f, x, h):
    return (f(x) - f(x - h)) / h
def centered_difference(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)
def second_derivative(f, x, h):
    return (f(x + h) - 2 * f(x) + f(x - h)) / h**2
def third_derivative(f, x, h):
    return (f(x + 2*h) - 2 * f(x + h) + 2 * f(x - h) - f(x - 2*h)) / (2 * h**3)
def three_point_forward_difference(f, x, h=1e-5):
    return (-3*f(x) + 4*f(x + h) - f(x + 2*h)) / (2*h)
def three_point_backward_difference(f, x, h=1e-5):
    return (3*f(x) - 4*f(x - h) + f(x - 2*h)) / (2*h)
def bisection(f, a, b, tol=1e-5, max_iter=100):
    for _ in range(max_iter):
        c = (a + b) / 2
        if f(c) == 0 or (b - a) / 2 < tol:
            return c
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return c
def newton(f, df, x, tol=1e-5, max_iter=100):
    for _ in range(max_iter):
        dx = f(x) / df(x)
        x -= dx
        if abs(dx) < tol:
            return x
    return x