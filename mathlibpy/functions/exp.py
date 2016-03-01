import function
import polynomial
import numbers
import math


class Exp(function.Function):

    def _evaluate(self, x):
        return math.e ** x

    def get_derivative(self):
        return self


class Power(function.Function):

    def __init__(self, f1, f2):
        self.f1 = f1
        self.f2 = f2
        self.exp = Exp()
        self.log = Log()

    def _evaluate(self, x):
        return self.exp(self.f2(x) * self.log(self.f1(x)))

    def get_derivative(self):
        return self.exp(self.f2 * self.log(self.f1)).get_derivative()


class Log(function.Function):

    def _evaluate(self, x):
        return math.log(x)

    def get_derivative(self):
        return function.Constant(1) / polynomial.Polynomial([0, 1])


class LogBase(function.Function):

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
