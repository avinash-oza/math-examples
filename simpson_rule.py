from __future__ import division
import math

def f_x(x):
    return math.exp(-x*x)

def N__x(x):
    return math.exp(-x*x/2)

def simpson_rule(a, b, f, n):
    h = (b-a)/n
    result = (f(a) + f(b))/6

    for i in xrange(1, n):
        result += f(a + i*h)/3

    for i in xrange(1, n+1):
        result += 2*f(a + (i - 0.5)*h)/3
    result *= h
    
    return result

def normal_converger(a, b, f, tol):
    n = 2
    abs_diff = 999999999999999999999999999
    val_prev = 0

    while abs_diff > tol:
        n *=2
        val_next = 1/2 + (1/math.sqrt(2*math.pi))*simpson_rule(a, b, f, n)
        abs_diff = abs(val_prev-val_next)

        print "N={0} simpson_rule = {1:.12f} abs_diff={2}".format(n, val_next, abs_diff)
        
        val_prev = val_next

def converger(a, b, f, tol):
    n = 2
    abs_diff = 999999999999999999999999999
    val_prev = 0

    while abs_diff > tol:
        n *=2
        val_next = simpson_rule(a, b, f, n)
        abs_diff = abs(val_prev-val_next)

        print "N={0} simpson_rule = {1} abs_diff={2}".format(n, val_next, abs_diff)
        
        val_prev = val_next

    return val_next

if __name__ == '__main__':
#   print simpson_rule(0, 2, f_x, 4)
#   print simpson_rule(0, 2, f_x, 100000)
#   print converger(0, 2, f_x, math.pow(10,-12))

#   print normal_converger(0, .1, N__x, math.pow(10,-12))
#   print normal_converger(0, .5, N__x, math.pow(10,-12))
#   print normal_converger(0, 1, N__x, math.pow(10,-12))
    pass
