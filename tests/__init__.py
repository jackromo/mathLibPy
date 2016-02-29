from test_matrix import MatrixTester
from test_polynomial import PolynomialTester
from test_exp import ExpTester
import unittest


def run_tests():
    for tester in [MatrixTester, PolynomialTester, ExpTester]:
        suite = unittest.TestLoader().loadTestsFromTestCase(tester)
        unittest.TextTestRunner(verbosity=1).run(suite)
