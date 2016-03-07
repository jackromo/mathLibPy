# All universal constants in MathLibPy.

import numbers


class Infinity(object):

    def __init__(self, rank, grp_id):
        # Rank defines partial ordering of infinities
        # Sign of rank also determines sign of infinity
        self.rank = rank
        # Only infinities with same group ID (grp_id) are comparable
        self.grp_id = grp_id

    def __lt__(self, other):
        if isinstance(other, numbers.Number):
            return self.rank >= 0
        elif isinstance(other, Infinity):
            return self.grp_id == other.grp_id and self.rank < other.rank
        else:
            raise TypeError("Not comparable with non-number or infinity")

    def __eq__(self, other):
        if not isinstance(other, Infinity):
            return False
        return self.grp_id == other.grp_id and self.rank == other.rank

    def __gt__(self, other):
        if isinstance(other, numbers.Number):
            return self.rank < 0
        elif isinstance(other, Infinity):
            return self.grp_id == other.grp_id and self.rank > other.rank
        else:
            raise TypeError("Not comparable with non-number or infinity")

    def __add__(self, other):
        if isinstance(other, numbers.Number):
            return self
        elif isinstance(other, Infinity):
            if other.grp_id == self.grp_id:
                return max(self, other)
            else:
                return self
        else:
            raise TypeError("Not composable with non-number or infinity")

    def __sub__(self, other):
        if isinstance(other, numbers.Number) or isinstance(other, Infinity):
            return self
        else:
            raise TypeError("Not composable with non-number or infinity")

    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            if other == 0:
                return 0
            else:
                return self
        elif isinstance(other, Infinity):
            return self
        else:
            raise TypeError("Not composable with non-number or infinity")

    def __div__(self, other):
        if isinstance(other, numbers.Number):
            if other == 0:
                raise ZeroDivisionError()
            else:
                return self
        elif isinstance(other, Infinity):
            return self
        else:
            raise TypeError("Not composable with non-number or infinity")


class IrrationalNumber(numbers.Number):
    """
    Irrational numbers must be a different type from floats, as all floats are rational.
    (This is due to them all having finite decimal places.)
    """

    TEST_ACCURACY = 100     # number of decimal places needed to be equal for 2 irrational numbers to be equal

    def __init__(self, generator):
        """
        Takes a generator function that returns value to provided number of decimal places.
        """
        if not hasattr(generator, "__call__"):
            raise TypeError("Irrational number requires a generator function to produce value")
        self.generator = generator

    def __eq__(self, other):
        if not isinstance(other, IrrationalNumber):
            return False
        elif other.generator == self.generator:
            return True
        else:
            # see if both values return same number up to a degree of accuracy
            return other.generator(IrrationalNumber.TEST_ACCURACY) == \
                   self.generator(IrrationalNumber.TEST_ACCURACY)

    def __float__(self):
        return self.generator(20)

    def __int__(self):
        return self.generator(0)


INFINITY = Infinity(1, 0)
NEG_INF = Infinity(-1, 0)     # Negative infinity
UNDEFINED = "undefined"       # Not a value, incomparable

# Cardinalities of sets, incomparable with aforementioned INFINITY
REAL_CARD = Infinity(2, 1)     # Cardinality of the set of real numbers
NAT_CARD = Infinity(1, 1)      # Cardinality of the set of natural numbers
