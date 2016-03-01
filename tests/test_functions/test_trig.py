from mathlibpy.functions import *
import unittest


class SinTester(unittest.TestCase):

    def setUp(self):
        self.sin = Sin()

    def test_call(self):
        self.assertEqual(self.sin(0), 0)

    def test_eq(self):
        self.assertEqual(self.sin, Sin())

    def test_get_derivative_call(self):
        self.assertEqual(self.sin.get_derivative()(0), 1)


class CosTester(unittest.TestCase):

    def setUp(self):
        self.cos = Cos()

    def test_call(self):
        self.assertEqual(self.cos(0), 1)

    def test_eq(self):
        self.assertEqual(self.cos, Cos())

    def test_get_derivative_call(self):
        self.assertEqual(self.cos.get_derivative()(math.pi/2), -1)


class TanTester(unittest.TestCase):

    def setUp(self):
        self.tan = Tan()

    def test_call(self):
        self.assertEqual(self.tan(0), 0)

    def test_eq(self):
        self.assertEqual(self.tan, Tan())

    def test_get_derivative(self):
        self.assertEqual(self.tan.get_derivative()(0), 1)


if __name__ == "__main__":
    unittest.main()
