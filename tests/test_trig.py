from trig import *
import unittest


class TrigTester(unittest.TestCase):

    def setUp(self):
        self.sin = Sin()
        self.cos = Cos()
        self.tan = Tan()

    def test_sin_call(self):
        self.assertEqual(self.sin(0), 0)

    def test_cos_call(self):
        self.assertEqual(self.cos(0), 1)

    def test_tan_call(self):
        self.assertEqual(self.tan(0), 0)

    def test_add_call(self):
        self.assertEqual((self.tan + self.cos + self.sin)(0), 1)

    def test_sin_get_derivative_call(self):
        self.assertEqual(self.sin.get_derivative()(0), 1)

    def test_cos_get_derivative_call(self):
        self.assertEqual(self.cos.get_derivative()(math.pi/2), -1)
