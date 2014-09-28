from __future__ import division
import math
from simpson_rule import converger

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
        print "discount_factor for t={0} : {1:.12}".format(flow_time, discount_factor)
        price += cash_flow_values[i] * discount_factor

    return price

def bond_price(cash_flow_times, cash_flow_values, zero_rate_function):
    
    price = 0

    for i in xrange(len(cash_flow_times)):
        flow_time = cash_flow_times[i]
        discount_factor = math.exp(-flow_time*zero_rate_function(flow_time))
        print discount_factor
        price += cash_flow_values[i] * discount_factor

    return price

def price_duration_convexity(cash_flow_times, cash_flow_values, the_yield):
    price = 0
    duration = 0
    convexity = 0

    for i in xrange(len(cash_flow_times)):
        flow_time = cash_flow_times[i]
        discount_factor = math.exp(-flow_time*the_yield)
        price += cash_flow_values[i]*discount_factor
        duration += flow_time*cash_flow_values[i]*discount_factor
        convexity += flow_time*flow_time*cash_flow_values[i]*discount_factor

    return price, duration/price, convexity/price

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
    flow_times = [6/12, 12/12, 18/12, 24/12]
    flow_values = [2.5, 2.5, 2.5, 102.5]
    tol_values = [math.pow(10,-6), math.pow(10, -6), math.pow(10,-6), math.pow(10,-8)]
    p = bond_price_inst_rate(flow_times, flow_values, r_homework9_t, tol_values)
    print "{0:.9f}".format(p)
