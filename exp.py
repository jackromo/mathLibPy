import function
import math


class Exp(function.Function):

    def _evaluate(self, x):
        return math.e ** x

    def get_derivative(self):
        return self


def main():
    exp = Exp()
    assert(exp(0) == 1)
    assert(exp(1) == math.e)
    assert(exp.get_derivative()(0) == 1)
    assert(exp.get_derivative()(1) == math.e)

if __name__ == "__main__":
    main()
