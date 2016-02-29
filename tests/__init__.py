from test_matrix import MatrixTester
import unittest


def run_tests():
    matrix_suite = unittest.TestLoader().loadTestsFromTestCase(MatrixTester)
    unittest.TextTestRunner(verbosity=2).run(matrix_suite)
