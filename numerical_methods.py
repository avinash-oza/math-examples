from __future__ import division
from functools import partial

import logging
logging.basicConfig(format='%(module)s - %(funcName)s - %(message)s', level=logging.INFO)
log = logging.getLogger(__name__)

import math
import time
import csv
from simpson_rule import normal_converger, N__x
from black_scholes import black_scholes, vega_black_scholes, d_1

def test_f(sigma):
    return math.pow(sigma, 4) - 5*sigma*sigma + 4 - 1/(1 + math.exp(math.pow(sigma,3)))

def f_hw5_num3(t,S,x,T,sigma,q,r):
    return (x*sigma*math.sqrt(2*math.pi*(T - t))*(math.exp(-q*(T-t))*normal_converger(0, d_1(t,S,x,T,sigma,q,r), N__x, math.pow(10,-12)) - 0.5))

def f_hw5_num3_deriv(t,S,x,T,sigma,q,r):
    return -1*math.exp(-q*(T-t)-0.5*d_1(t,S,x,T,sigma,q,r))

def f_hw5_num4(x):
    return 2.5*(math.exp(-1*r_0_05*0.5)+math.exp(-r_0_1*1)+math.exp(-1.5*(0.25*x+0.75*r_0_1)) + math.exp(-2*(0.5*x+0.5*r_0_1))+ math.exp(-2.5*(0.75*x+0.25*r_0_1)) + math.exp(-3*x)) + 100*math.exp(-3*x) - 102

def f_hw5_num4_deriv(x, r_0_05, r_0_1):
    return 2.5*-1.5*0.25*math.exp(-1.5*(0.25*x+0.75*r_0_1)) + 2.5*-2*0.5*math.exp(-2*(0.5*x+0.5*r_0_1)) +2.5*-2.5*0.75*math.exp(-2.5*(0.75*x + 0.25*r_0_1)) + 102.5*-3*math.exp(-3*x)

def f_hw5_num4_part2(x, r_0_05, r_0_1, r_0_15, r_0_2, r_0_25, r_0_3):
    return 3*(math.exp(-r_0_05*0.5) + math.exp(-r_0_1*1) + math.exp(-r_0_15*1.5) + math.exp(-r_0_2*2) + math.exp(-r_0_25*2.5) + math.exp(-r_0_3*3) + math.exp(-3.5*(0.25*x+0.75*r_0_3)) + math.exp(-4*(0.5*x + 0.5*r_0_3)) + math.exp(-4.5*(0.75*x + 0.25*r_0_3)) + math.exp(-5*x)) + 100*math.exp(-5*x) - 104
    
def f_hw5_num4_part2_deriv(x, r_0_3):
    return 3*((-3.5)*(0.25)*math.exp(-3.5*(0.25*x+0.75*r_0_3)) +(-4)*(0.5)*math.exp(-4*(0.5*x + 0.5*r_0_3)) +(-4.5)*0.75*math.exp(-4.5*(0.75*x + 0.25*r_0_3)) + (-5)*math.exp(-5*x)) + 100*(-5)*math.exp(-5*x)
    
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
         
        log.debug("Guess: {0:0.12f}".format(x_solution))
        
    return x_solution

def newtons_method(x0, f, f_prime, tol_approx, price_call):
    x_new = x0
    x_old = x0 - 1

    while abs(x_new - x_old) > tol_approx:
        x_old = x_new
        x_new = x_old - (f(x=x_old) - price_call)/f_prime(x=x_old)
        log.info("Guess: {0:0.9f}".format(x_new))
    return x_new

def secant_method(x00, x0, f, tol_approx, tol_consec, price_call):
    x_new = x0
    x_old = x00
    x_oldest = 0

    while abs((f(sigma=x_new) - price_call)) > tol_approx or abs(x_new - x_old) > tol_consec:
        x_oldest = x_old
        x_old = x_new
        x_new = x_old - (f(sigma=x_old) - price_call)*(x_old - x_oldest)/(f(sigma=x_old) - f(sigma=x_oldest))
        log.debug("Guess: {0:0.12f}".format(x_new))

    return x_new
    
def implied_volatility(price_call, S, K, T, q, r, initial_guess, option_type='CALL'):

    x0 = initial_guess # An initial guess
    x_new = x0
    x_old = x0 - 1
    tol = math.pow(10, -6)

    while abs(x_new - x_old) > tol:
        x_old = x_new
        x_new = x_new - (black_scholes(0, S, K, T, x_new, q, r, option_type=option_type)- price_call)/vega_black_scholes(0, S, K, T, x_new, q, r)
        log.debug("Implied guess: {0:0.12f}".format(x_new))
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

#   f = partial(black_scholes,t=0, S=40, K=40, T=5/12, q=0.01, r=0.025, option_type='CALL')
#   vega_func= partial(vega_black_scholes,t=0,S=40,K=40,T=5/12,q=0.01,r=0.025) 

#   print "IMPLIED VOL: {0:0.12f}".format(
#   implied_volatility(price_call=2.75, S=40, K=40, T=5/12, q=0.01, r=0.025,initial_guess=0.5))
#   print "IMPLIED VOL NEWTONs METHOD: {0:0.12f}".format(
#   newtons_method(x0=0.5, f=f, f_prime=vega_func, tol_approx=math.pow(10, -6),price_call=2.75))    
#   print "IMPLIED VOL VIA bisection method: {0:0.12f}".format(bisection_method(a=0.0001, b=1, f=f, tol_approx=math.pow(10, -9), tol_int=math.pow(10, -6), price_call=2.75))
#   print "IMPLIED VOL VIA secant method: {0:0.12f}".format(secant_method(x0=0.5, f=f, tol_approx=math.pow(10, -6),  price_call=2.75))

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

#################################################################
#   HW 5 #3

#   f = partial(f_hw5_num3,t=0, S=30, T=3/12, sigma=0.30, q=0.01, r=0.025)
#   f_deriv = partial(f_hw5_num3_deriv,t=0, S=30, T=3/12, sigma=0.30, q=0.01, r=0.025)

#   print "STRIKE VIA NEWTONs METHOD: {0:0.12f}".format(
#   newtons_method(x0=30, f=f, f_prime=f_deriv, tol_approx=math.pow(10, -6),price_call=0))    

################################################################
#   HW5 #4
#   r_0_05 = -2*math.log(97.5/100)
#   r_0_1 = -1*math.log((100-2.5*math.exp(-r_0_05*0.5))/102.5)
#   f_deriv = partial(f_hw5_num4_deriv,r_0_05=r_0_05, r_0_1=r_0_1)

#   r_0_3 = newtons_method(x0=0.05, f=f_hw5_num4, f_prime=f_deriv, tol_approx=math.pow(10, -6),price_call=0) 

#   r_0_15 = 0.25*r_0_3 + 0.75*r_0_1
#   r_0_2 = 0.50*r_0_3 + 0.50*r_0_1
#   r_0_25 = 0.75*r_0_3 + 0.25*r_0_1

#   f_r_0_5 = partial(f_hw5_num4_part2,r_0_05=r_0_05, r_0_1=r_0_1, r_0_15=r_0_15, r_0_2=r_0_2, r_0_25=r_0_25, r_0_3=r_0_3)

#   f_deriv_r_0_5 = partial(f_hw5_num4_part2_deriv, r_0_3=r_0_3)

#   r_0_5 = newtons_method(x0=0.05, f=f_r_0_5, f_prime=f_deriv_r_0_5, tol_approx=math.pow(10, -6),price_call=0) 

#   r_0_35 = 0.25*r_0_5 + 0.75*r_0_3
#   r_0_4 = 0.50*r_0_5 + 0.50*r_0_3
#   r_0_45 = 0.75*r_0_5 + 0.25*r_0_3

#   print "r(0,0.5): {0:0.9f}".format(r_0_05)
#   print "r(0,1): {0:0.9f}".format(r_0_1)
#   print "r(0,1.5): {0:0.9f}".format(r_0_15)
#   print "r(0,2): {0:0.9f}".format(r_0_2)
#   print "r(0,2.5): {0:0.9f}".format(r_0_25)
#   print "r(0,3): {0:0.9f}".format(r_0_3)
#   print "r(0,3.5): {0:0.9f}".format(r_0_35)
#   print "r(0,4): {0:0.9f}".format(r_0_4)
#   print "r(0,4.5): {0:0.9f}".format(r_0_45)
#   print "r(0,5): {0:0.9f}".format(r_0_5)
    pass
