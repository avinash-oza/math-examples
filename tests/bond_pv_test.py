from __future__ import division
import unittest
import math
from bond_pv import calculate_df, calculate_flows

class BondPvTestCases(unittest.TestCase):
    def test_calculate_flows(self):
        expected_flows = [3.5, 3.5, 3.5, 3.5, 103.5]
        expected_times = [0.4166666666666667, 0.9166666666666666, 1.4166666666666667, 1.9166666666666667, 2.4166666666666665]
        flow_times, flow_values = calculate_flows(coupon=7, frequency=2, maturity=29)
        self.assertEqual(expected_times, flow_times)
        self.assertEqual(expected_flows, flow_values)

    def test_calculate_df(self):
       expected_df = 0.0024787521766663585
       self.assertAlmostEqual(calculate_df(2, 3), expected_df)
