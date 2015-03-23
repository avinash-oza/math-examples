from __future__ import division
from functools import partial
import math
from simpson_rule import N, N__x, numerical_cumulative_distribution
import logging
logging.basicConfig(format='%(module)s - %(funcName)s - %(message)s', level=logging.DEBUG)
log = logging.getLogger(__name__)

def d_1(t,S,K,T,sigma,q,r):
    return (math.log(S/K)+(r-q+sigma*sigma*0.5)*(T-t))/(sigma*math.sqrt(T-t))

def pvf_d_1(pvf, disc, K, T, sigma):
    return (math.log(pvf/(K*disc))/(sigma*math.sqrt(T)) + (sigma*math.sqrt(T)/2))

def black_scholes(t,S,K,T,sigma,q,r,option_type=None):
    d1= d_1(t, S, K, T, sigma, q, r)
    d2 = d1 - sigma*math.sqrt(T-t)

    log.debug("d1={0} d2={1}".format(d1,d2))
    call_price = S*math.exp(-q*(T-t))*N(d1) - K*math.exp(-r*(T-t))*N(d2)
    put_price = -S*math.exp(-q*(T-t))*N(-d1) + K*math.exp(-r*(T-t))*N(-d2)

    if option_type is None:
        log.warning ("NO OPTION TYPE PASSED, ASSUMING CALL")
        return call_price
    elif option_type.upper() == 'CALL':
        return call_price
    elif option_type.upper() =='PUT':
        return put_price

def estimated_black_scholes(t,S,K,T,sigma,q,r, option_type=None):
    d1= d_1(t, S, K, T, sigma, q, r)
    d2 = d1 - sigma*math.sqrt(T-t)

    log.debug("d1={0} d2={1}".format(d1, d2))
    call_price = S*math.exp(-q*(T-t))*numerical_cumulative_distribution(d1) - K*math.exp(-r*(T-t))*numerical_cumulative_distribution(d2)
    put_price = -S*math.exp(-q*(T-t))*numerical_cumulative_distribution(-d1) + K*math.exp(-r*(T-t))*numerical_cumulative_distribution(-d2)

    if option_type is None:
        log.warning ("NO OPTION TYPE PASSED, ASSUMING CALL")
        return call_price
    elif option_type.upper() == 'CALL':
        return call_price
    elif option_type.upper() =='PUT':
        return put_price

def pvf_black_scholes(pvf, disc, K, T, sigma, option_type=None):
    d1 = pvf_d_1(pvf, disc, K, T, sigma)
    d2 = d1 - sigma*math.sqrt(T)

    call_price = pvf*numerical_cumulative_distribution(d1) - K*disc*numerical_cumulative_distribution(d2)
    put_price = K*disc*numerical_cumulative_distribution(-d2) - pvf*numerical_cumulative_distribution(-d1)
    
    if option_type is None:
       log.warning ("NO OPTION TYPE PASSED, ASSUMING CALL")
       return call_price
    elif option_type.upper() == 'CALL':
       return call_price
    elif option_type.upper() =='PUT':
       return put_price

def vega_pvf_black_scholes(pvf, disc, K, T, x, option_type=None):
    d1 = pvf_d_1(pvf, disc, K, T, x)
    return pvf*math.sqrt(T/(2*math.pi))* math.exp(-d1*d1/2)

def vega_black_scholes(t, S, K, T, x, q, r):
    d1=(math.log(S/K)+(r-q+x*x*0.5)*(T-t))/(x*math.sqrt(T-t))
    return 1/math.sqrt(2*math.pi)*S*math.exp(-q*T)*math.sqrt(T)*math.exp(-d1*d1/2)

def call_approx(S, K, T, sigma, q, r):
    """Implements approximation formula from HW 5"""
    return sigma*S*math.sqrt(T/(2*math.pi))*(1 - 0.5*(r + q)*T) + 0.5*T*S*(r - q)

if __name__ == '__main__':
#   black_scholes (0,42,40,0.5,0.3,0.03,0.05)
    # Forum example CALL
#   black_scholes(0,60,50,0.75,0.2,0.02,0.01)
    # Forum example PUT
#   black_scholes(0,20,40,0.25,0.3,0.03,0.02)
    #8i PUT
#   black_scholes(0,100,100,0.5,0.3,0,0.05)
    #8i PUT part 2
#   black_scholes(0,102,100,125/252,0.3,0,0.05)

    #10i PUT
#   black_scholes(0,25,30,13/52,0.3,0,0.02)
#   black_scholes(0,30,30,12/52,0.3,0,0.02)
#   black_scholes(0,26,30,11/52,0.3,0,0.02)
#   black_scholes(0,22,30,10/52,0.3,0,0.02)
#   black_scholes(0,27,30,9/52,0.3,0,0.02)

    # For 6 plot
#   black_scholes(0,0.5,1,9/52,0.3,0,0.02)
#   black_scholes(0,0.25,1,9/52,0.3,0,0.02)
#   black_scholes(0,0.125,1,9/52,0.3,0,0.02)
#   black_scholes(0,2,1,9/52,0.3,0,0.02)
    
    # HW 4
    # 1a
#   print "Estimated black scholes: {0:0.12f}".format(estimated_black_scholes(0, 40, 40, 3/12, 0.20, 0.01, 0.05, option_type='CALL'))
#   black_scholes(0, 40, 40, 3/12, 0.20, 0.01, 0.05)

#   print "VEGA TESt: {0:0.12f}".format(vega_black_scholes(0, 50, 50, 0.25, 0.3, 0, 0))

#####################################################################
#   HW 5 #9
#   f = partial(call_approx, S=40, K=40, sigma=0.30, q=0.01, r=0.03)
#   bs = partial(black_scholes, t=0, S=40, K=40, sigma=0.30, q=0.01, r=0.03, option_type='CALL')
#   T_values = [12/12, 36/12, 60/12, 120/12, 240/12]
#   for t in T_values:
#       print "For T={0}:  Black Scholes: {1:0.9f}, Call Approx: {2:0.9f}, error={3:0.9f} ".format(
#       t, bs(T=t), f(T=t),  abs(f(T=t) - bs(T=t))/bs(T=t))
#####################################################################
    pass
