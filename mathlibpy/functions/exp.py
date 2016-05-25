"""
All exponential, power and logarithmic functions.

Author: Jack Romo <sharrackor@gmail.com>
"""


import function
import polynomial
import numbers
import math


class Exp(function.Function):
    """
    Exponential function.
    """

    def _evaluate(self, x):
        # TODO: Compute this via Maclaurin series or use constants.E
        return math.e ** x

    def get_derivative(self):
        return self

    def __eq__(self, other):
        return isinstance(other, Exp)


class Power(function.Function):
    """
    Adjustment of Exp for general powers of functions to functions.
    """

    def __init__(self, f1, f2):
        if isinstance(f1, function.Function):
            self.f1 = f1
        elif isinstance(f1, numbers.Number):
            self.f1 = function.Constant(f1)
        if isinstance(f2, function.Function):
            self.f2 = f2
        elif isinstance(f2, numbers.Number):
            self.f2 = function.Constant(f2)
        self.exp = Exp()
        self.log = Log()

    def _evaluate(self, x):
        return self.exp(self.f2(x) * self.log(self.f1(x)))

    def get_derivative(self):
        return self.exp(self.f2 * self.log(self.f1)).get_derivative()

    def __eq__(self, other):
        if not isinstance(other, Power):
            return False
        return (self.f1 == other.f1) and (self.f2 == other.f2)


class Log(function.Function):
    """
    Natural logarithm.
    """

    def _evaluate(self, x):
        return math.log(x)

    def get_derivative(self):
        return function.Constant(1) / polynomial.Polynomial([0, 1])

    def __eq__(self, other):
        return isinstance(other, Log)


class LogBase(function.Function):
    """
    Adjustment of Log to accommodate arbitrary bases.
    """

    def __init__(self, b):
        self.log = Log()
        if isinstance(b, numbers.Number) or isinstance(b, function.Function):
            self.b = b
        else:
            raise TypeError("Base must either be a Function or a Number")

    def _evaluate(self, x):
        if isinstance(self.b, function.Function):
            return self.log(x) / self.log(self.b(x))
        else:
            return self.log(x) / self.log(self.b)

    def get_derivative(self):
        if isinstance(self.b, function.Function):
            return ((function.Constant(1) / Log()(self.b)) * Log()).get_derivative()
        else:
            return ((function.Constant(1) / function.Constant(Log()(self.b))) * Log()).get_derivative()

    def __eq__(self, other):
        if not isinstance(other, LogBase):
            return False
        return self.b == other.b
