from __future__ import division
import unittest
import math
from black_scholes import d_1, black_scholes, estimated_black_scholes, vega_black_scholes


class BlackScholesTestCases(unittest.TestCase):

    def test_d1(self):
        self.assertAlmostEqual(d_1(t=0, S=40, K=40, T=9/12, sigma=0.30, q=0.01, r=0.03), 0.187638837487, places=12)

    def test_call_option(self):
        self.assertAlmostEqual(black_scholes (0,42,40,0.5,0.3,0.03,0.05, option_type='CALL'), 4.705327411511, places=12)

    def test_put_option(self):
        self.assertAlmostEqual(black_scholes(0,20,40,0.25,0.3,0.03,0.02, option_type='PUT'), 19.9499395465949, places=12)

    def test_estimated_black_scholes(self):
        self.assertAlmostEqual(estimated_black_scholes(0, 40, 40, 3/12, 0.20, 0.01, 0.05, option_type='CALL'), 1.789613023816, places=12)

    def test_black_scholes_vega(self):
        self.assertAlmostEqual(vega_black_scholes(0, 50, 50, 0.25, 0.3, 0, 0), 9.945545790187, places=12)

if __name__ == '__main__':
    unittest.main()
