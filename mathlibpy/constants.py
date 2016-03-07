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

    TEST_ACCURACY = 10     # number of decimal places needed to be equal for 2 irrational numbers to be equal

    def __init__(self, val):
        if not (isinstance(val, int) or isinstance(val, float)):
            raise TypeError("Irrational number requires base Number value")
        self.val = val

    def __eq__(self, other):
        if not isinstance(other, IrrationalNumber):
            return False
        elif other.val == self.val:
            return True
        else:
            # see if both values return same number up to a degree of accuracy
            return round(other.val, IrrationalNumber.TEST_ACCURACY) == \
                   round(self.val, IrrationalNumber.TEST_ACCURACY)

    def __float__(self):
        return self.val

    def __int__(self):
        return int(round(self.val, 0))

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return IrrationalNumber(self.val + other)
        elif isinstance(other, IrrationalNumber):
            return IrrationalNumber(self.val + other.val)
        else:
            return self.val + other

    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return IrrationalNumber(self.val - other)
        elif isinstance(other, IrrationalNumber):
            return IrrationalNumber(self.val - other.val)
        else:
            return self.val - other

    def __neg__(self):
        return IrrationalNumber(-self.val)


INFINITY = Infinity(1, 0)
NEG_INF = Infinity(-1, 0)     # Negative infinity
UNDEFINED = "undefined"       # Not a value, incomparable

# Cardinalities of sets, incomparable with aforementioned INFINITY
REAL_CARD = Infinity(2, 1)     # Cardinality of the set of real numbers
NAT_CARD = Infinity(1, 1)      # Cardinality of the set of natural numbers

# Irrational numbers
PI = IrrationalNumber(3.14159265)
E = IrrationalNumber(2.718281828)
