import function
import math


class Sin(function.Function):

    def _evaluate(self, x):
        return math.sin(x)


class Cos(function.Function):

    def _evaluate(self, x):
        return math.cos(x)


class Tan(function.Function):

    def _evaluate(self, x):
        sin = Sin()
        cos = Cos()
        if cos(x) == 0:
            raise ZeroDivisionError()
        return sin(x) / cos(x)


def main():
    sin = Sin()
    cos = Cos()
    tan = Tan()
    assert(sin(0) == 0)
    assert(cos(0) == 1)
    assert(tan(0) == 0)
    assert((tan + cos + sin)(0) == 1)

if __name__ == "__main__":
    main()