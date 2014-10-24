from __future__ import division
import math
from simpson_rule import converger

import logging
logging.basicConfig(format='%(module)s - %(funcName)s - %(message)s', level=logging.DEBUG)
log = logging.getLogger(__name__)

def r_t(t):
    return 0.0525 + math.log(1+2*t)/200

def r_homework_t(t):
    return 0.05 + 0.005*math.sqrt(1 + t)

def r_homework2_t(t):
    return 0.02 + t/(200-t)

def r_example9_t(t):
    return 0.0525+1/(100*(1+math.exp(-t*t)))

def r_homework9_t(t):
    return 0.05/(1+2*math.exp(-(1+t)*(1+t)))

def bond_price_inst_rate(cash_flow_times, cash_flow_values, inst_rate_function, tol_values):
    
    price = 0

    for i in xrange(len(cash_flow_times)):
        flow_time = cash_flow_times[i]
        inst_rate = converger(0, flow_time, inst_rate_function, tol_values[i])

        discount_factor = math.exp(-inst_rate)
        log.debug("discount_factor for t={0} : {1:.12}".format(flow_time, discount_factor))
        price += cash_flow_values[i] * discount_factor

    return price

def bond_price_zero_rate(cash_flow_times, cash_flow_values, zero_rate_function):
    
    price = 0

    for i in xrange(len(cash_flow_times)):
        flow_time = cash_flow_times[i]
        discount_factor = math.exp(-flow_time*zero_rate_function(flow_time))
        log.debug("Discount Factor: ".format(discount_factor))
        price += cash_flow_values[i] * discount_factor

    return price

def bond_price(cash_flow_times, cash_flow_values, the_yield):
    price = 0
    for i in xrange(len(cash_flow_times)):
        flow_time = cash_flow_times[i]
        discount_factor = math.exp(-flow_time*the_yield)
        price += cash_flow_values[i]*discount_factor

    return price

def bond_duration(cash_flow_times, cash_flow_values, the_yield):
    price = bond_price(cash_flow_times, cash_flow_values, the_yield)
    duration = 0

    for i in xrange(len(cash_flow_times)):
        flow_time = cash_flow_times[i]
        discount_factor = math.exp(-flow_time*the_yield)
        duration += flow_time*cash_flow_values[i]*discount_factor
        
    return duration/price

def bond_convexity(cash_flow_times, cash_flow_values, the_yield):
    price = bond_price(cash_flow_times, cash_flow_values, the_yield)
    convexity = 0

    for i in xrange(len(cash_flow_times)):
        flow_time = cash_flow_times[i]
        discount_factor = math.exp(-flow_time*the_yield)
        price += cash_flow_values[i]*discount_factor
        convexity += flow_time*flow_time*cash_flow_values[i]*discount_factor

    return convexity/price

def bond_derivative(cash_flow_times, cash_flow_values, the_yield):
    """Calculates the derivative of a bond for use with Newton's Method
    Implemented from p149"""
    f_prime = 0

    for i in xrange(len(cash_flow_times)):
        flow_time = cash_flow_times[i]
        discount_factor = math.exp(-flow_time*the_yield)
        f_prime += flow_time * cash_flow_values[i] * discount_factor

    return -1 * f_prime

def bond_yield(cash_flow_times, cash_flow_values, bond_market_price, tol=math.pow(10, -6)):
    """Implements the bond yield formula using Newton's method on p150"""

    assert len(cash_flow_times) == len(cash_flow_values), "Times and values length mismatch"
    x0 = 0.1 # initital guess

    x_new = x0
    x_old = x0 -1

    while abs(x_new - x_old) > tol:
        x_old = x_new
        x_new = x_old - (bond_price(cash_flow_times, cash_flow_values, x_old) - bond_market_price)/bond_derivative(cash_flow_times, cash_flow_values, x_old)
        log.debug("Guess: {0:0.15f}".format(x_new))

    return x_new

if __name__ == '__main__':
#   cash_flow_times = [2/12, 8/12, 14/12, 20/12]
#   cash_flow_values = [3, 3, 3, 103]
#   print bond_price(cash_flow_times, cash_flow_values, r_t)

    #Homework values
#   flow_times = [6/12 ,12/12, 18/12, 24/12]
#   flow_values = [3.5, 3.5, 3.5, 103.5]
#   print bond_price(flow_times, flow_values, r_homework_t)


#   flow_times = [1/12, 7/12, 13/12, 19/12]
#   flow_values = [3.5, 3.5, 3.5, 103.5]
#   print bond_price(flow_times, flow_values, r_homework_t)

    #7a
 #  flow_times = [7/12, 19/12]
 #  flow_values = [4, 104]
 #  print bond_price(flow_times, flow_values, r_homework2_t)
    #7b
#   flow_times = [1/12, 7/12, 13/12, 19/12]
#   flow_values = [2, 2, 2, 102]
#   print bond_price(flow_times, flow_values, r_homework2_t)

    #7c
#   flow_times = [1/12, 4/12, 7/12, 10/12, 13/12, 16/12, 19/12]
#   flow_values = [1, 1, 1, 1, 1, 1, 101]
#   print "{0:.9f}".format(bond_price(flow_times, flow_values, r_homework2_t))
    
    #book_example relevant to 8
#   flow_times = [2/12, 8/12, 14/12, 20/12]
#   flow_values = [3, 3, 3, 103]
#   the_yield = 0.065
#   p, d, c = price_duration_convexity(flow_times, flow_values, the_yield)
#   print "{0:.9f} {1:.9f} {2:.9f}".format(p, d, c)
    #8
#   flow_times = [1/12, 7/12, 13/12, 19/12]
#   flow_values = [2, 2, 2, 102]
#   the_yield = 0.025
#   p, d, c = price_duration_convexity(flow_times, flow_values, the_yield)
#   print "{0:.9f} {1:.9f} {2:.9f}".format(p, d, c)
    
    #Example for #9
#   flow_times = [2/12, 8/12, 14/12, 20/12]
#   flow_values = [3, 3, 3, 103]
#   tol_values = [math.pow(10,-4), math.pow(10, -4), math.pow(10,-4), math.pow(10,-6)]
#   p = bond_price_inst_rate(flow_times, flow_values, r_example9_t, tol_values)
#   print "{0:.6f}".format(p)

    #9
#   flow_times = [6/12, 12/12, 18/12, 24/12]
#   flow_values = [2.5, 2.5, 2.5, 102.5]
#   tol_values = [math.pow(10,-6), math.pow(10, -6), math.pow(10,-6), math.pow(10,-8)]
#   p = bond_price_inst_rate(flow_times, flow_values, r_homework9_t, tol_values)
#   print "{0:.9f}".format(p)

#   p150 example
    flow_times = [4/12, 10/12, 16/12, 22/12, 28/12, 34/12]
    flow_values = [4, 4, 4, 4, 4, 104]
    p = bond_yield(flow_times, flow_values, 105)
    print "Bond yield {0:.9f}".format(p)
