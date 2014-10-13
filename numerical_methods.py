from __future__ import division
from functools import partial
import math
import time
import csv
from black_scholes import black_scholes, vega_black_scholes

def test_f(sigma):
    return math.pow(sigma, 4) - 5*sigma*sigma + 4 - 1/(1 + math.exp(math.pow(sigma,3)))

def bisection_method(a, b, f, tol_approx, tol_int, price_call):
    x_left = a
    x_right = b
    x_solution = 0

    while max(abs(f(sigma=x_left) - price_call), abs(f(sigma=x_right)- price_call)) > tol_approx or x_right- x_left > tol_int:
        x_solution = (x_left + x_right)/2
        
        if (f(sigma=x_left) - price_call)*(f(sigma=x_solution) - price_call) < 0:
            x_right = x_solution
        else:
            x_left = x_solution
         
#       print "Guess: {0:0.12f}".format(x_solution)
        
    return x_solution

def newtons_method(x0, f, f_prime, tol_approx, price_call):
    x_new = x0
    x_old = x0 - 1

    while abs(f(sigma=x_new) - price_call) > tol_approx:
        x_old = x_new
        x_new = x_old - (f(sigma=x_old) - price_call)/f_prime(x_old)
        print "Guess: {0:0.12f}".format(x_new)

def secant_method(x0, f, tol_approx, price_call):
    x_new = x0
    x_old = x0 - 1
    x_oldest = 0

    while abs((f(sigma=x_new) - price_call)) > tol_approx:
        x_oldest = x_old
        x_old = x_new
        x_new = x_old - (f(sigma=x_old) - price_call)*(x_old - x_oldest)/(f(sigma=x_old) - f(sigma=x_oldest))
#       print "Guess: {0:0.12f}".format(x_new)

    return x_new
    
def implied_volatility(price_call, S, K, T, q, r, initial_guess):

    x0 = initial_guess # An initial guess
    x_new = x0
    x_old = x0 - 1
    tol = math.pow(10, -6)

    while abs(x_new - x_old) > tol:
        x_old = x_new
        x_new = x_new - (black_scholes(0, S, K, T, x_new, q, r)- price_call)/vega_black_scholes(0, S, K, T, x_new, q, r)
#       print "Implied guess: {0:0.12f}".format(x_new)
    return x_new

if __name__ == '__main__':
#   print simpson_rule(0, 2, f_x, 4)
#   print simpson_rule(0, 2, f_x, 100000)
#   print converger(0, 2, f_x, math.pow(10,-12))

#   print normal_converger(0, .1, N__x, math.pow(10,-12))
#   print normal_converger(0, .5, N__x, math.pow(10,-12))
#   print normal_converger(0, 1, N__x, math.pow(10,-12))

#   Test of table 3.1
#   print "{0:0.12f}".format(numerical_cumulative_distribution(0.45))
#   print normal_converger(0, .45, N__x, math.pow(10,-12))
    
#   Test of 5.7
#   print "IMPLIED VOL: {0:0.12f}".format(implied_volatility(7, 25, 20, 1, 0, 0.05, 0.25))

#   HW 4 #6   
#   print "IMPLIED VOL: {0:0.12f}".format(
#   implied_volatility(price_call=2.5, S=30, K=30, T=1/2, q=0.01, r=0.03,initial_guess=0.5))


    #ef implied_volatility(price_call, S, K, T, q, r, tol):
#   HW 4 #7
#   Test for bisection method
#   print "IMPLIED VOL VIA bisection method: {0:0.12f}".format(bisection_method(a=-2, b=3, f=test_f, tol_approx=math.pow(10, -6), tol_int=math.pow(10, -9), price_call=0))

    f = partial(black_scholes,t=0, S=40, K=40, T=5/12, q=0.01, r=0.025)
    
    print "IMPLIED VOL: {0:0.12f}".format(
    implied_volatility(price_call=2.75, S=40, K=40, T=5/12, q=0.01, r=0.025,initial_guess=0.5))
    
    print "IMPLIED VOL VIA bisection method: {0:0.12f}".format(bisection_method(a=0.0001, b=1, f=f, tol_approx=math.pow(10, -6), tol_int=math.pow(10, -6), price_call=2.75))
    print "IMPLIED VOL VIA secant method: {0:0.12f}".format(secant_method(x0=0.5, f=f, tol_approx=math.pow(10, -6),  price_call=2.75))

#   HW 4 #10
    put_data = [(1100, 56.2, 130/365),
                (1200, 91.85, 130/365),
                (800, 10.55, 130/365),
                
                (1175, 104.5, 208/365),
                (1200, 115.3, 208/365),
                (1225, 126.75, 208/365),
                
                (1175, 127.15, 306/365),
                (1200, 137.9, 306/365),
                (1225, 149.55, 306/365)]
    
    call_data = [(1350, 17.95, 130/365),
                 (1400, 8.60, 130/365),
                 
                 (1175, 111.35, 208/365),
                 (1200, 97.1, 208/365),
                 
                 (1175, 129.1, 306/365),
                 (1200, 115.05, 306/365)]
#   with open('dump.csv', 'wb') as csvfile: 
#       my_writer = csv.writer(csvfile, delimiter=',')
#       for case in call_data:
#           data = ["Call",case[0],case[1],case[2],implied_volatility(price_call=case[1],S=1193.0, K=case[0], T=case[2], q=0.017, r=0.001,initial_guess=0.4)]
#           my_writer.writerow(data)
#           print "Strike: {0}, P_MID: {1}, Num days: {2}, Impl vol:{3:0.12f}".format(case[0], case[1], case[2],
#                   implied_volatility(price_call=case[1],S=1193.0, K=case[0], T=case[2], q=0.017, r=0.001,initial_guess=0.4))

    pass
