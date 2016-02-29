import function
import math


class Exp(function.Function):

    def _evaluate(self, x):
        return math.e ** x

    def get_derivative(self):
        return self
