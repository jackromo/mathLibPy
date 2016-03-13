import numbers


class Infinity(numbers.Number):

    def __init__(self, rank, grp_id):
        self.rank = rank
        self.grp_id = grp_id

    def __lt__(self, other):
        if isinstance(other, Infinity):
            return self.grp_id == other.grp_id and self.rank < other.rank
        elif isinstance(other, numbers.Number):
            return self.rank < 0
        else:
            raise TypeError("Not comparable with non-number")

    def __eq__(self, other):
        if not isinstance(other, Infinity):
            return False
        return self.grp_id == other.grp_id and self.rank == other.rank

    def __gt__(self, other):
        if isinstance(other, Infinity):
            return self.grp_id == other.grp_id and self.rank > other.rank
        elif isinstance(other, numbers.Number):
            return self.rank >= 0
        else:
            raise TypeError("Not comparable with non-number")

    def __neg__(self):
        return Infinity(-self.rank, self.grp_id)

    def __add__(self, other):
        if isinstance(other, Infinity):
            if other.grp_id == self.grp_id:
                return max(self, other)
            else:
                return self
        elif isinstance(other, numbers.Number):
            return self
        else:
            raise TypeError("Not composable with non-number")

    def __sub__(self, other):
        if isinstance(other, numbers.Number):
            return self
        else:
            raise TypeError("Not composable with non-number")

    def __mul__(self, other):
        if isinstance(other, Infinity):
            return Infinity(self.rank * (other.rank / float(abs(other.rank))), self.grp_id)
        elif isinstance(other, numbers.Number):
            if other == 0:
                return 0
            elif (other / float(abs(other))) != (self.rank / float(abs(self.rank))):
                return -self
            else:
                return self
        else:
            raise TypeError("Not composable with non-number")

    def __div__(self, other):
        if isinstance(other, Infinity):
            return Infinity(self.rank * (other.rank / float(abs(other.rank))), self.grp_id)
        elif isinstance(other, numbers.Number):
            if other == 0:
                raise ZeroDivisionError()
            elif (other / float(abs(other))) != (self.rank / float(abs(self.rank))):
                return -self
            else:
                return self
        else:
            raise TypeError("Not composable with non-number")


INFINITY = Infinity(1, 0)
NEG_INF = Infinity(-1, 0)     # Negative infinity
UNDEFINED = "undefined"       # Not a value, incomparable

# Cardinalities of sets, incomparable with aforementioned INFINITY
REAL_CARD = Infinity(2, 1)     # Cardinality of the set of real numbers
NAT_CARD = Infinity(1, 1)      # Cardinality of the set of natural numbers
