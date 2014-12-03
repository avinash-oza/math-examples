from __future__ import division
import math
from simpson_rule import converger, simpson_rule

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

def r_homework5_2_t(t):
    return 0.015 + t/(100 + math.sqrt(1 + t * t))

def bond_price_inst_rate(cash_flow_times, cash_flow_values, inst_rate_function, tol_values):
    """Bond price code on p67 for r(t) function
    """
    
    price = 0

    for i in xrange(len(cash_flow_times)):
        flow_time = cash_flow_times[i]
        inst_rate = converger(0, flow_time, inst_rate_function, tol_values[i], simpson_rule)

        discount_factor = math.exp(-inst_rate)
        log.debug("discount_factor for t={0} : {1:.12}".format(flow_time, discount_factor))
        price += cash_flow_values[i] * discount_factor

    return price

def bond_price_zero_rate(cash_flow_times, cash_flow_values, zero_rate_function):
    """Bond price code on p66.
    
    """
    
    price = 0

    for i in xrange(len(cash_flow_times)):
        flow_time = cash_flow_times[i]
        discount_factor = math.exp(-flow_time*zero_rate_function(flow_time))
        log.info("discount_factor for t={0} : {1:.12}".format(flow_time, discount_factor))
        price += cash_flow_values[i] * discount_factor

    return price

def calculate_flows(coupon, frequency, maturity):
    """
    coupon in dollars
    frequency is an int
    maturity in months
    returns intervals scaled by years
    """
    flow_times = range(maturity, 0, int(-12/frequency))
    flow_times.reverse()
    flow_times = [t/12 for t in flow_times]
    flow_values = [coupon/frequency for i in flow_times[:-1]] + [100+coupon/frequency]

    log.info("Flow times={times} \nFlow Values = {values}".format(times=flow_times, values=flow_values))
    return flow_times, flow_values

def calculate_df(r, t):
    """
    Calculates discount factor for rate and time
    """
    return math.exp(-r*t)

def lin_interpolator(a, b, x):
    """
    Creates linear interpolation equation and returns constants
    """
    return (b-x)/(b-a), (x-a)/(b-a)

def calculate_rate(i_tuple, r1, r2):
    """
    Calculates an interpolated rate
    """
    return i_tuple[0]*r1+i_tuple[1]*r2

def bond_price(cash_flow_times, cash_flow_values, the_yield):
    """Bond price code on p69 
    """
    price = 0
    for i in xrange(len(cash_flow_times)):
        flow_time = cash_flow_times[i]
        discount_factor = math.exp(-flow_time*the_yield)
        price += cash_flow_values[i]*discount_factor

    return price

def bond_duration(cash_flow_times, cash_flow_values, the_yield, dollar_type=False):
    """Bond duration code on p69 
    """
    price = bond_price(cash_flow_times, cash_flow_values, the_yield)
    duration = 0

    for i in xrange(len(cash_flow_times)):
        flow_time = cash_flow_times[i]
        discount_factor = math.exp(-flow_time*the_yield)
        duration += flow_time*cash_flow_values[i]*discount_factor
        
    return duration if dollar_type else duration/price

def bond_convexity(cash_flow_times, cash_flow_values, the_yield, dollar_type=False):
    """Bond convexity code on p69 
    """
    price = bond_price(cash_flow_times, cash_flow_values, the_yield)
    convexity = 0

    for i in xrange(len(cash_flow_times)):
        flow_time = cash_flow_times[i]
        discount_factor = math.exp(-flow_time*the_yield)
        convexity += flow_time*flow_time*cash_flow_values[i]*discount_factor

    return convexity if dollar_type else convexity/price

def DV01(dollar_duration):
    return dollar_duration/10000

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
    count = 0

    while abs(x_new - x_old) > tol:
        count +=1
        log.info("Guess: {0:0.9f}".format(x_new))
        x_old = x_new
        x_new = x_old - (bond_price(cash_flow_times, cash_flow_values, x_old) - bond_market_price)/bond_derivative(cash_flow_times, cash_flow_values, x_old)

    log.info("Final Guess: {res:0.9f}. Iterations:{iterations}".format(res=x_new, iterations=count))
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
#   flow_times = [4/12, 10/12, 16/12, 22/12, 28/12, 34/12]
#   flow_values = [4, 4, 4, 4, 4, 104]
#   p = bond_yield(flow_times, flow_values, 105)
#   print "Bond yield {0:.9f}".format(p)

#######################################################################
#   HW5 #1
#   flow_times = [6/12, 12/12, 18/12, 24/12, 30/12, 36/12]
#   flow_values = [2, 2, 2, 2, 2, 102]
#   the_yield = bond_yield(flow_times, flow_values, 101)
#   print "Bond yield {0:.9f}".format(the_yield)
#   print "Bond duration {0:.9f} , convexity: {1:.9f}".format(bond_duration(flow_times, flow_values, the_yield), bond_convexity(flow_times, flow_values, the_yield))

#   HW5 #2
    flow_times, flow_values = calculate_flows(coupon=7, frequency=2, maturity=29)
    def r_t(t):
        return 0.015 + (1+2*t)/(100+100*t)
    market_bond_price = bond_price_zero_rate(flow_times, flow_values, r_t)
    print "Bond price {0:.9f}".format(market_bond_price)
    the_yield = bond_yield(flow_times, flow_values, market_bond_price)
    print "Bond yield {0:.9f}".format(the_yield)
    b_duration = bond_duration(flow_times, flow_values,the_yield,dollar_type=False)
    b_convexity = bond_convexity(flow_times, flow_values, the_yield,dollar_type=False)
    dv01 = DV01(bond_duration(flow_times, flow_values, the_yield,dollar_type=True))

    print "Bond duration {b_duration:.9f} , convexity: {b_convexity:.9f}, dv01={dv01}".format(b_duration=b_duration, b_convexity=b_convexity, dv01=dv01)

########################################################################

#   HW 6 #7
#   flow_times = [3/12, 6/12, 9/12, 12/12, 15/12, 18/12, 21/12, 24/12]
#   flow_values = [2, 2, 2, 2, 2, 2, 2, 102]
#   the_yield = 0.09
#   delta_y = [0.0010, 0.0050, 0.01, 0.02, 0.04]

#   bond_p = bond_price(flow_times, flow_values, the_yield)
#   bond_d = bond_duration(flow_times, flow_values, the_yield)
#   bond_c = bond_convexity(flow_times, flow_values, the_yield)
#   def b_new_d(delta, B=bond_p):
#       return B*(-1*bond_d*delta + 1)

#   def b_new_d_c(delta, B=bond_p):
#       return B*(-1*bond_d*delta + bond_c/2 * delta*delta + 1)

#   print "Bond Price: {0:.9f}, Bond duration {1:.9f} , convexity: {2:.9f}".format(bond_p, bond_d, bond_c)

#   for d in delta_y:
#       B_price = bond_price(flow_times, flow_values, the_yield +d)
#       B_new_d = b_new_d(d)
#       B_new_d_c = b_new_d_c(d)
#       B_new_d_error = abs(B_new_d - B_price)/B_price
#       B_new_d_c_error = abs(B_new_d_c - B_price)/B_price
#       print "Delta: {delta:.4f} Bond Value: {0:.9f}, b_new_d: {1:.9f}, b_new_d_c: {2:.9f}, b_new_d_error : {3:.9f}, b_new_d_c_error : {4:.9f}".format(B_price, B_new_d, B_new_d_c, B_new_d_error, B_new_d_c_error, delta=d)
    pass
