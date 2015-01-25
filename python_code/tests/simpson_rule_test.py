import unittest
import math
from simpson_rule import f_x, converger, simpson_rule, midpoint_rule, normal_converger, N__x, N, numerical_cumulative_distribution

class SimpsonRuleTestCases(unittest.TestCase):

    def test_4_interval(self):
        self.assertAlmostEqual(simpson_rule(0, 2, f_x, 4), 0.882065510401, places=12)

    def test_100k_interval(self):
        self.assertAlmostEqual(simpson_rule(0, 2, f_x, 100000), 0.882081390762, places=12)

# class NormalDistributionTestCases(unittest.TestCase):

    def test_run_1(self):
        expected_value = 0.691462461274
        self.assertAlmostEqual(normal_converger(0, .5, N__x, math.pow(10,-12)), expected_value, places=12)
        self.assertAlmostEqual(N(0.5), expected_value, places=12)
    def test_run_2(self):
         self.assertAlmostEqual(normal_converger(0, 1, N__x, math.pow(10,-12)), 0.841344746069, places=12)
         
# class ConvergerTestCases(unittest.TestCase):
    def test_simpson_converger(self):
         self.assertAlmostEqual(converger(0, 2, f_x, math.pow(10,-12), approx_func=simpson_rule), 0.882081390762, places=12)

    def test_midpoint_converger(self):
        """Tests midpoint rule. Weird tolerance is added to match p49 512 interval number"""
        self.assertAlmostEqual(converger(0, 2, f_x, 1.4*math.pow(10,-7), approx_func=midpoint_rule), 0.88208144, places=8)

# class NormalDistributionTestCases(unittest.TestCase):
    def test_approx_cumulative_distribution(self):
        self.assertAlmostEqual(numerical_cumulative_distribution(0.45), 0.673644759227, places=12)
if __name__ == '__main__':
    unittest.main()
