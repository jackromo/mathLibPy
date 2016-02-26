import abc


class Sequence(object):
    """
    An infinite sequence of terms.
    """

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __call__(self, n):
        """
        Given a value n, returns the nth item in the sequence.
        """

    def sum_from_to(self, i, n):
        """
        Given a value n, returns the sum of all items from i to n inclusive.
        """
        return sum(self(j) for j in range(i, n+1))


class ArithmeticSequence(Sequence):
    """
    A sequence where each term is the previous one plus a constant.
    """

    def __init__(self, initial, c):
        """
        c: constant added onto each term.
        initial: 0th term's value.
        """
        self.initial = initial
        self.const = c

    def __call__(self, n):
        if not isinstance(n, int):
            raise TypeError("Can only be called on integers")
        elif not 0 <= n:
            raise ValueError("Argument must be > 0")
        else:
            return self.initial + (self.const * n)


class GeometricSequence(Sequence):
    """
    A sequence where each term is the previous one multiplied by a constant.
    """

    def __init__(self, initial, r):
        """
        r: constant multiplied by each term.
        initial: 0th term's value.
        """
        self.initial = initial
        self.const = r

    def __call__(self, n):
        if not isinstance(n, int):
            raise TypeError("Can only be called on integers")
        elif not 0 <= n:
            raise ValueError("Argument must be > 0")
        else:
            return self.initial * (self.const ** n)


def main():
    arith_seq = ArithmeticSequence(1, 1)
    assert(arith_seq(0) == 1)
    assert(arith_seq(2) == 3)
    geom_seq = GeometricSequence(1, 2)
    assert(geom_seq(0) == 1)
    assert(geom_seq(3) == 8)

if __name__ == "__main__":
    main()
