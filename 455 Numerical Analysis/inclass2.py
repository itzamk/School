#bisection method
import math

def f(x):

    return math.exp(x) - x**2

a = -2
b = 0

fa = f(a)
fb = f(b)

er = 10**-6
k = round(math.ceil(((math.log10(b-a) - math.log(er)) / math.log10(2))))

for n in range(1,k):

    print("\niteration", n)
  
    c = (a+b)/2
    fc = f(c)

    print('c is', c)

    if fc == 0:
        print('root is', c)

    elif fc * fb > 0:
        b=c
        fb=fc

    else:
        a=c
        fa=fc

    print('error is', abs(b-a))

    if abs(b-a) < er:
        print(f"\nroot is approximately", c )
        break