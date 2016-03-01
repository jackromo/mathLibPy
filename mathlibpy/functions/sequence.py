import abc
import function


class Sequence(object):
    """
    An infinite sequence of terms.
    """

    __metaclass__ = abc.ABCMeta

    def __call__(self, n):
        if not isinstance(n, int):
            raise TypeError("Can only be called on integers")
        elif not 0 <= n:
            raise ValueError("Argument must be > 0")
        else:
            return self._term_at(n)

    @abc.abstractmethod
    def _term_at(self, n):
        """
        Given a value n, returns the nth item in the sequence.
        n is guaranteed to be an integer > 0.
        """

    @abc.abstractmethod
    def __eq__(self, other):
        """
        Will rely upon Function equality test, as many series will be implemented as Functions.
        """

    def sum_from_to(self, i, n):
        """
        Given a value n, returns the sum of all items from i to n inclusive.
        """
        return sum(self(j) for j in range(i, n+1))


class FunctionSequence(Sequence):
    """
    Sequence where each item is defined by a Function.
    """

    def __init__(self, f):
        if not isinstance(f, function.Function):
            raise TypeError("Must supply Function to FunctionSequence")
        self.func = f

    def __eq__(self, other):
        if not isinstance(other, FunctionSequence):
            return False
        return self.func == other.func

    def _term_at(self, n):
        return self.func(n)


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

    def __eq__(self, other):
        if not isinstance(other, ArithmeticSequence):
            return False
        return (self.initial == other.initial) and (self.const == other.const)

    def _term_at(self, n):
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

    def __eq__(self, other):
        if not isinstance(other, GeometricSequence):
            return False
        return (self.initial == other.initial) and (self.const == other.const)

    def _term_at(self, n):
        return self.initial * (self.const ** n)
