from __future__ import division
import math
from simpson_rule import N__x,normal_converger, numerical_cumulative_distribution

def black_scholes(t,S,K,T,sigma,q,r,option_type=None):
    d1=(math.log(S/K)+(r-q+sigma*sigma*0.5)*(T-t))/(sigma*math.sqrt(T-t))
    d2 = d1 - sigma*math.sqrt(T-t)

#   print "d1={0} d2={1}".format(d1,d2)
    call_price = S*math.exp(-q*(T-t))*normal_converger(0,d1,N__x,math.pow(10,-12)) - K*math.exp(-r*(T-t))*normal_converger(0,d2,N__x,math.pow(10,-12))
    put_price = -S*math.exp(-q*(T-t))*normal_converger(0,-d1,N__x,math.pow(10,-12)) + K*math.exp(-r*(T-t))*normal_converger(0,-d2,N__x,math.pow(10,-12))
#   print "Call Price:{0:.12f} | Put Price: {1:.12f}".format(call_price, put_price)

    if option_type is None:
        print ("NO OPTION TYPE PASSED, ASSUMING CALL")
        return call_price
    elif option_type.upper() == 'CALL':
        return call_price
    elif option_type.upper() =='PUT':
        return put_price

def estimated_black_scholes(t,S,K,T,sigma,q,r):
    d1=(math.log(S/K)+(r-q+sigma*sigma*0.5)*(T-t))/(sigma*math.sqrt(T-t))
    d2 = d1 - sigma*math.sqrt(T-t)

    print "d1={0} d2={1}".format(d1,d2)
    call_price = S*math.exp(-q*(T-t))*numerical_cumulative_distribution(d1) - K*math.exp(-r*(T-t))*numerical_cumulative_distribution(d2)
    put_price = -S*math.exp(-q*(T-t))*numerical_cumulative_distribution(-d1) + K*math.exp(-r*(T-t))*numerical_cumulative_distribution(-d2)
    print "Call Price:{0:.12f} | Put Price: {1:.12f}".format(call_price, put_price)

def vega_black_scholes(t, S, K, T, x, q, r):
    d1=(math.log(S/K)+(r-q+x*x*0.5)*(T-t))/(x*math.sqrt(T-t))
    return 1/math.sqrt(2*math.pi)*S*math.exp(-q*T)*math.sqrt(T)*math.exp(-d1*d1/2)

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
#   estimated_black_scholes(0, 40, 40, 3/12, 0.20, 0.01, 0.05)
#   black_scholes(0, 40, 40, 3/12, 0.20, 0.01, 0.05)

    print "VEGA TESt: {0:0.12f}".format(vega_black_scholes(0, 50, 50, 0.25, 0.3, 0, 0))
    
    pass
