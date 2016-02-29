from test_matrix import MatrixTester
from test_polynomial import PolynomialTester
import unittest


def run_tests():
    for tester in [MatrixTester, PolynomialTester]:
        suite = unittest.TestLoader().loadTestsFromTestCase(tester)
        unittest.TextTestRunner(verbosity=1).run(suite)
