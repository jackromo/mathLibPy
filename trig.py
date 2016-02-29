import function
import math


class Sin(function.Function):

    def _evaluate(self, x):
        return math.sin(x)

    def get_derivative(self):
        return Cos()


class Cos(function.Function):

    def _evaluate(self, x):
        return math.cos(x)

    def get_derivative(self):
        return function.Constant(-1) * Sin()


class Tan(function.Function):

    def _evaluate(self, x):
        sin = Sin()
        cos = Cos()
        if cos(x) == 0:
            raise ZeroDivisionError()
        return sin(x) / cos(x)

    def get_derivative(self):
        return function.Constant(1) / (Cos() * Cos())
