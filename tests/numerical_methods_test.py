from __future__ import division
from functools import partial
import math
import unittest
from numerical_methods import implied_volatility, bisection_method, newtons_method, test_f, f_hw5_num3, f_hw5_num3_deriv,secant_method

class NumericalMethodsTestCases(unittest.TestCase):

    def test_implied_volatility(self):
        self.assertAlmostEqual(implied_volatility(7, 25, 20, 1, 0, 0.05, 0.25), 0.363063180486, places=12)
        self.assertAlmostEqual(implied_volatility(price_call=2.5, S=30, K=30, T=1/2, q=0.01, r=0.03,initial_guess=0.5), 0.280755777837, places=12)

    def test_bisection_method(self):
       self.assertAlmostEqual(bisection_method(a=-2, b=3, f=test_f, tol_approx=math.pow(10, -6), tol_int=math.pow(10, -9), price_call=0), -0.889641813585, places=12)

    def test_newtons_method(self):
       f = partial(f_hw5_num3,t=0, S=30, T=3/12, sigma=0.30, q=0.01, r=0.025)
       f_deriv = partial(f_hw5_num3_deriv,t=0, S=30, T=3/12, sigma=0.30, q=0.01, r=0.025)
       self.assertAlmostEqual(newtons_method(x0=30, f=f, f_prime=f_deriv, tol_approx=math.pow(10, -9),price_call=0),30.4390645053369, places=12) 

    def test_secant_method(self):
       self.assertAlmostEqual(secant_method(-3.01, -3, f=test_f, tol_approx=math.pow(10, -9), tol_consec=math.pow(10, -6), price_call=0), -2.074304402883815, places=12) 

if __name__ == '__main__':
    unittest.main()
