# All universal constants in MathLibPy.


class Infinity(object):

    def __init__(self, rank, grp_id):
        # Rank defines partial ordering of infinities
        self.rank = rank
        # Only infinities with same group ID (grp_id) are comparable
        self.grp_id = grp_id

    def __lt__(self, other):
        if not isinstance(other, Infinity):
            return False
        return self.grp_id == other.grp_id and self.rank < other.rank

    def __eq__(self, other):
        if not isinstance(other, Infinity):
            return False
        return self.grp_id == other.grp_id and self.rank == other.rank

    def __gt__(self, other):
        if not isinstance(other, Infinity):
            return False
        return self.grp_id == other.grp_id and self.rank > other.rank


INFINITY = Infinity(1, 0)
NEG_INF = Infinity(-1, 0)     # Negative infinity
UNDEFINED = "undefined"       # Not a value, incomparable

# Cardinalities of sets, incomparable with aforementioned INFINITY
REAL_CARD = Infinity(2, 1)     # Cardinality of the set of real numbers
NAT_CARD = Infinity(1, 1)      # Cardinality of the set of natural numbers
