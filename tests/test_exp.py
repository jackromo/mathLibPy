from exp import *
import math
import unittest


class ExpTester(unittest.TestCase):

    def setUp(self):
        self.exp = Exp()

    def test_call(self):
        self.assertEqual(self.exp(0), 1)
        self.assertEqual(self.exp(1), math.e)

    def test_get_derivative(self):
        self.assertEqual(self.exp.get_derivative(), self.exp)


if __name__ == "__main__":
    unittest.main()
