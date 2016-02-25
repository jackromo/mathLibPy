import function
import math


class Exp(function.Function):

    def _evaluate(self, x):
        return math.e ** x


def main():
    exp = Exp()
    assert(exp(0) == 1)
    assert(exp(1) == math.e)

if __name__ == "__main__":
    main()
