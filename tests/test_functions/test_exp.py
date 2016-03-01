from mathlibpy.functions import *
import math
import unittest


class ExpTester(unittest.TestCase):

    def setUp(self):
        self.exp = Exp()

    def test_eq(self):
        self.assertEqual(self.exp, Exp())

    def test_call(self):
        self.assertEqual(self.exp(0), 1)
        self.assertEqual(self.exp(1), math.e)

    def test_get_derivative(self):
        self.assertEqual(self.exp.get_derivative(), self.exp)


class LogTester(unittest.TestCase):

    def setUp(self):
        self.log = Log()

    def test_eq(self):
        self.assertEqual(self.log, Log())

    def test_call(self):
        self.assertEqual(self.log(1), 0)
        self.assertEqual(self.log(math.e), 1)

    def test_get_derivative_call(self):
        self.assertEqual(self.log.get_derivative()(1), 1)
        self.assertEqual(self.log.get_derivative()(5), 0.2)
        self.assertRaises(Exception, self.log.get_derivative().__call__, 0)


class PowerTester(unittest.TestCase):

    def setUp(self):
        self.pow1 = Power(Constant(1), Constant(1))
        self.pow2 = Power(Polynomial([0, 1]), Constant(2))
        self.pow3 = Power(Constant(2), Polynomial([0, 1]))

    def test_eq(self):
        self.assertEqual(self.pow1, Power(Constant(1), Constant(1)))
        self.assertEqual(self.pow2, Power(Polynomial([0, 1]), Constant(2)))

    def test_call(self):
        self.assertEqual(self.pow1(3), 1)
        self.assertEqual(self.pow2(3), 9)
        self.assertEqual(round(self.pow3(3), 10), 8)    # Accurate within 10 decimal places

    def test_get_derivative_call(self):
        self.assertEqual(self.pow1.get_derivative()(3), 0)
        self.assertEqual(self.pow2.get_derivative()(3), 6)
        self.assertEqual(round(self.pow3.get_derivative()(3), 10), round(math.log(2)*8, 10))


class LogBaseTester(unittest.TestCase):

    def setUp(self):
        self.log2 = LogBase(2)
        self.ln = LogBase(math.e)
        self.log5 = LogBase(Constant(5))
        self.log_x_squared = LogBase(Polynomial([0, 0, 1]))

    def test_eq(self):
        self.assertEqual(self.log2, LogBase(2))
        self.assertEqual(self.log_x_squared, LogBase(Polynomial([0, 0, 1])))

    def test_call(self):
        self.assertEqual(self.log2(2), 1)
        self.assertEqual(self.ln(math.e), 1)
        self.assertEqual(self.log5(5), 1)
        self.assertEqual(self.log_x_squared(2), 0.5)

    def test_get_derivative_call(self):
        self.assertEqual(round(self.log2.get_derivative()(2), 10), round(0.5 / math.log(2), 10))
        self.assertEqual(round(self.ln.get_derivative()(math.e), 10), round((1 / math.e), 10))
        self.assertEqual(round(self.log_x_squared.get_derivative()(3), 10), 0)


if __name__ == "__main__":
    unittest.main()
