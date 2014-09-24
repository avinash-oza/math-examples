from __future__ import division
import math

def f_x(x):
    return math.exp(-x*x)

def simpson_rule(a, b, f, n):
    h = (b-a)/n
    result = (f(a) + f(b))/6

    for i in xrange(1, n):
        result += f(a + i*h)/3
        print i

    for i in xrange(1, n+1):
        result += 2*f(a + (i - 0.5)*h)/3
        print i
    result *= h
    
    return result

if __name__ == '__main__':
    print simpson_rule(0, 2, f_x, 4)
#   print simpson_rule(0, 2, f_x, 256)
