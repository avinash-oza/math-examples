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

#       print "N={0} simpson_rule = {1:.12f} abs_diff={2}".format(n, val_next, abs_diff)
        
        val_prev = val_next
    return val_next

def converger(a, b, f, tol):
    n = 2
    abs_diff = 999999999999999999999999999
    val_prev = 0

    while abs_diff > tol:
        n *=2
        val_next = simpson_rule(a, b, f, n)
        abs_diff = abs(val_prev-val_next)

#       print "N={0} simpson_rule = {1} abs_diff={2}".format(n, val_next, abs_diff)
        
        val_prev = val_next

    return val_next

def numerical_cumulative_distribution(z_value):
    z = abs(z_value)
    y = 1/(1 + 0.2316419*z)
    a1 = 0.319381530
    a2 = -0.356563782
    a3 = 1.781477937
    a4 = -1.821255978
    a5 = 1.330274429

    m = 1 - math.exp(-z_value*z_value/2)*(a1*y+a2*math.pow(y, 2)+a3*math.pow(y, 3)+a4*math.pow(y, 4)+a5*math.pow(y, 5))/math.sqrt(2*math.pi)

    if z_value > 0:
        return m
    else:
        return 1 - m

if __name__ == '__main__':
#   print simpson_rule(0, 2, f_x, 4)
#   print simpson_rule(0, 2, f_x, 100000)
#   print converger(0, 2, f_x, math.pow(10,-12))

#   print normal_converger(0, .1, N__x, math.pow(10,-12))
#   print normal_converger(0, .5, N__x, math.pow(10,-12))
#   print normal_converger(0, 1, N__x, math.pow(10,-12))

#   Test of table 3.1
    print "{0:0.12f}".format(numerical_cumulative_distribution(0.45))
    print normal_converger(0, .45, N__x, math.pow(10,-12))
    pass
