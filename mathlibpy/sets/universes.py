import abc
import numbers
from mathlibpy.constants import *

# TODO: documentation


class TypeUniverseSet(object):
    """
    The set that defines the universe of all items of a certain type.
    Not compatible with normal sets.
    """

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __contains__(self, item):
        """
        Boolean of whether or not item is within universe of set.
        """

    @abc.abstractmethod
    def is_sparse(self):
        """
        True if all elements finite distance from each other, False otherwise.
        """

    @abc.abstractmethod
    def is_ordered(self):
        """
        True if all elements are comparable, False otherwise.
        """

    @abc.abstractmethod
    def elems_in_range(self, low, high):
        """
        If set is ordered, sparse and lowest/highest points are not infinite, return range of elements between them.
        Otherwise, raise an error.
        """

    @abc.abstractmethod
    def cardinality(self):
        """
        Cardinality of set, including subsets.
        """


class PredefinedUniverse(TypeUniverseSet):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def card_without_subsets(self):
        """
        Number of elements in type's universe minus its declared subsets.
        """

    @abc.abstractmethod
    def get_subsets(self):
        """
        Get list of all subset universes.
        """

    @abc.abstractmethod
    def get_superset(self):
        """
        Get single superset universe of self.
        """

    def is_subset(self, other):
        if not isinstance(other, TypeUniverseSet):
            raise TypeError("Can only be subset of another TypeUniverseSet")
        superset = self
        while superset is not None:
            superset = superset.get_superset()
            if type(superset) == type(other):
                return True
        return False


class MathObjectUniverse(PredefinedUniverse):

    def __contains__(self, item):
        return True

    def is_sparse(self):
        return False

    def is_ordered(self):
        return False

    def elems_in_range(self, low, high):
        raise Exception("Universe is not ordered or sparse")

    def get_subsets(self):
        return [NumberUniverse]

    def get_superset(self):
        return None

    def card_without_subsets(self):
        return INFINITY

    def cardinality(self):
        return INFINITY


class NumberUniverse(PredefinedUniverse):

    def __contains__(self, item):
        return isinstance(item, numbers.Number)

    def is_sparse(self):
        return False

    def is_ordered(self):
        return False

    def elems_in_range(self, low, high):
        raise Exception("Universe is not sparse")

    def get_subsets(self):
        return [RealNumberUniverse]

    def get_superset(self):
        return MathObjectUniverse

    def card_without_subsets(self):
        return 0

    def cardinality(self):
        return REAL_CARD


class RealNumberUniverse(PredefinedUniverse):

    def __contains__(self, item):
        return isinstance(item, numbers.Real)

    def is_sparse(self):
        return False

    def is_ordered(self):
        return True

    def elems_in_range(self, low, high):
        raise Exception("Universe is not sparse")

    def get_subsets(self):
        return [RationalNumberUniverse, IrrationalNumberUniverse]

    def get_superset(self):
        return NumberUniverse

    def card_without_subsets(self):
        return 0

    def cardinality(self):
        return REAL_CARD


class IrrationalNumberUniverse(PredefinedUniverse):

    def __contains__(self, item):
        return isinstance(item, IrrationalNumber)

    def is_sparse(self):
        return False

    def is_ordered(self):
        return True

    def elems_in_range(self, low, high):
        raise Exception("Universe is not sparse")

    def get_subsets(self):
        return []

    def get_superset(self):
        return RealNumberUniverse

    def card_without_subsets(self):
        return REAL_CARD

    def cardinality(self):
        return REAL_CARD


class RationalNumberUniverse(PredefinedUniverse):

    def __contains__(self, item):
        return isinstance(item, float) or isinstance(item, int)

    def is_sparse(self):
        return False

    def is_ordered(self):
        return True

    def elems_in_range(self, low, high):
        raise Exception("Universe is not sparse")

    def get_subsets(self):
        return [IntegerUniverse]

    def get_superset(self):
        return RealNumberUniverse

    def card_without_subsets(self):
        return NAT_CARD

    def cardinality(self):
        return NAT_CARD


class IntegerUniverse(PredefinedUniverse):

    def __contains__(self, item):
        return isinstance(item, int)

    def is_sparse(self):
        return False

    def is_ordered(self):
        return True

    def elems_in_range(self, low, high):
        if isinstance(low, Infinity) or isinstance(high, Infinity):
            raise Exception("Cannot get infinite range")
        return range(low, high+1)

    def get_subsets(self):
        return []

    def get_superset(self):
        return RationalNumberUniverse

    def card_without_subsets(self):
        return NAT_CARD

    def cardinality(self):
        return NAT_CARD


class UniverseCombination(TypeUniverseSet):

    __metaclass__ = abc.ABCMeta

    def __init__(self, set1, set2):
        self.set1 = set1
        self.set2 = set2


class UniverseIntersect(UniverseCombination):

    def __contains__(self, item):
        return (item in self.set1) and (item in self.set2)

    def is_sparse(self):
        return self.set1.is_sparse or self.set2.is_sparse

    def is_ordered(self):
        return self.set1.is_ordered or self.set2.is_ordered

    def elems_in_range(self, low, high):
        return [x for x in self.set1.elems_in_range(low, high) if x in self.set2.elems_in_range(low, high)]

    def cardinality(self):
        if self.set1.is_subset(self.set2):
            return self.set1.cardinality()
        elif self.set2.is_subset(self.set1):
            return self.set2.cardinality()
        else:
            return 0


class UniverseUnion(UniverseCombination):

    def __contains__(self, item):
        return (item in self.set1) or (item in self.set2)

    def is_sparse(self):
        return self.set1.is_sparse and self.set2.is_sparse

    def is_ordered(self):
        # TODO: can't check if elements in both sets are comparable with each other (would make set not ordered)
        # should therefore check for if both are subsets of same ordered superset
        return self.set1.is_ordered and self.set2.is_ordered

    def elems_in_range(self, low, high):
        result = []
        for elem in self.set1.elems_in_range(low, high) + self.set2.elems_in_range(low, high):
            if elem not in result:
                result.append(elem)
        return result

    def cardinality(self):
        if self.set1.is_subset(self.set2):
            return self.set2.cardinality()
        elif self.set2.is_subset(self.set1):
            return self.set1.cardinality()
        else:
            return self.set1.cardinality() + self.set2.cardinality()


class UniverseDifference(UniverseCombination):

    def __contains__(self, item):
        return (item in self.set1) and not (item in self.set2)

    def is_sparse(self):
        return self.set1.is_sparse

    def is_ordered(self):
        return self.set1.is_ordered

    def elems_in_range(self, low, high):
        return [x for x in self.set1.elems_in_range(low, high) if x not in self.set2.elems_in_range(low, high)]

    def cardinality(self):
        if self.set1.is_subset(self.set2):
            return 0
        elif self.set2.is_subset(self.set1):
            return self.set1.card_without_subsets() + sum(s.cardinality() for s in self.set1.get_subsets()
                                                          if not isinstance(s, type(self.set2)))
        else:
            return self.set1.cardinality()
