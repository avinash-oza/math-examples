import unittest
import math
from simpson_rule import f_x, simpson_rule, normal_converger, N__x, numerical_cumulative_distribution

class SimpsonRuleTestCases(unittest.TestCase):

    def test_4_interval(self):
        self.assertAlmostEqual(simpson_rule(0, 2, f_x, 4), 0.882065510401, places=12)

    def test_100k_interval(self):
        self.assertAlmostEqual(simpson_rule(0, 2, f_x, 100000), 0.882081390762, places=12)

class NormalDistributionTestCases(unittest.TestCase):

    def test_1(self):
        self.assertAlmostEqual(normal_converger(0, .5, N__x, math.pow(10,-12)), 0.691462461274, places=12)
    def test_2(self):
         self.assertAlmostEqual(normal_converger(0, 1, N__x, math.pow(10,-12)), 0.841344746069, places=12)
         
    def test_approx_cumulative_distribution(self):
        self.assertAlmostEqual(numerical_cumulative_distribution(0.45), 0.673644759227, places=12)
if __name__ == '__main__':
    unittest.main()
