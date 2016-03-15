"""
.. module:: trig
    :synopsis: Sin, Cos and Tan classes.

.. moduleauthor:: Jack Romo <sharrackor@gmail.com>
"""


import function
import math


class Sin(function.Function):
    """
    Wrapper class for sine function.
    """

    def _evaluate(self, x):
        # TODO: implement this as Maclaurin series
        return math.sin(x)

    def get_derivative(self):
        return Cos()

    def __eq__(self, other):
        return isinstance(other, Sin)


class Cos(function.Function):
    """
    Wrapper class for cosine function.
    """

    def _evaluate(self, x):
        # TODO: implement this as Maclaurin series
        return math.cos(x)

    def get_derivative(self):
        return function.Constant(-1) * Sin()

    def __eq__(self, other):
        return isinstance(other, Cos)


class Tan(function.Function):
    """
    Wrapper class for tangent function.
    """

    def _evaluate(self, x):
        sin = Sin()
        cos = Cos()
        if cos(x) == 0:
            raise ZeroDivisionError()
        return sin(x) / cos(x)

    def get_derivative(self):
        return function.Constant(1) / (Cos() * Cos())

    def __eq__(self, other):
        return isinstance(other, Tan)
