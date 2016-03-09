import abc
import numbers
import math
import copy
from mathlibpy.constants import *


class SetPy(object):
    """
    A collection of arbitrary entities.
    """

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __contains__(self, item):
        """
        Check if contains item.
        """

    @abc.abstractmethod
    def cardinality(self):
        """
        Return number of items in set.
        """

    @abc.abstractmethod
    def is_finite(self):
        """
        Return whether has a finite number of elements.
        """

    @abc.abstractmethod
    def elems(self):
        """
        If finite, return all elements. If not, raise an exception.
        """

    def union(self, other):
        if not isinstance(other, SetPy):
            raise TypeError("Can only union with another SetPy")
        return SetPyUnionNode(self, other)

    def difference(self, other):
        if not isinstance(other, SetPy):
            raise TypeError("Can only take difference with another SetPy")
        return SetPyDifferenceNode(self, other)

    def intersect(self, other):
        if not isinstance(other, SetPy):
            raise TypeError("Can only intersect with another SetPy")
        return SetPyIntersectNode(self, other)

    def is_disjoint(self, other):
        if not isinstance(other, SetPy):
            raise TypeError("Can only be disjoint with another SetPy")
        return self.intersect(other).cardinality() == 0

    def is_subset(self, other):
        if not isinstance(other, SetPy):
            raise TypeError("Can only be subset of another SetPy")
        return self.intersect(other).cardinality() == self.cardinality()

    def __eq__(self, other):
        if not isinstance(other, SetPy):
            return False
        return self.is_subset(other) and other.is_subset(self)

    def is_proper_subset(self, other):
        if not isinstance(other, SetPy):
            raise TypeError("Can only be proper subset of another SetPy")
        return self.is_subset(other) and (self is not other)


class SetPyTreeNode(SetPy):
    """
    Sets are organized into a tree of operations on some starting base sets.
    eg. (A U B) \ (B U C) is a tree of the Difference node, then two Union nodes holding A,B and B,C.
    This defines a generic node in such a tree.
    """

    __metaclass__ = abc.ABCMeta

    def __init__(self, s1, s2):
        if not (isinstance(s1, SetPy) and isinstance(s2, SetPy)):
            raise TypeError("Both inputs must be of type SetPy")
        self.s1 = s1
        self.s2 = s2


class SetPyUnionNode(SetPyTreeNode):

    def __contains__(self, item):
        return (item in self.s1) or (item in self.s2)

    def is_finite(self):
        return self.s1.is_finite() and self.s2.is_finite()

    def cardinality(self):
        intersect = self.s1.intersect(self.s2)
        return self.s1.cardinality() + self.s2.cardinality() - intersect.cardinality()

    def elems(self):
        if not self.is_finite():
            raise Exception("Set is infinite, cannot get all elements")
        else:
            result = []
            for x in self.s1.elems() + self.s2.elems():
                if x not in result:
                    result.append(x)
            return result


class SetPyIntersectNode(SetPyTreeNode):

    def __contains__(self, item):
        return (item in self.s1) and (item in self.s2)

    def is_finite(self):
        return self.s1.is_finite() or self.s2.is_finite()

    def cardinality(self):
        if self.s1.is_finite():
            return len(filter(lambda x: x in self.s2, self.s1.elems()))
        elif self.s2.is_finite():
            return len(filter(lambda x: x in self.s1, self.s2.elems()))
        else:
            return self.s1.cardinality() + self.s2.cardinality()

    def elems(self):
        if not self.is_finite():
            raise Exception("Set is infinite, cannot get all elements")
        else:
            result = []
            for x in self.s1.elems():
                if (x not in result) and (x in self.s2):
                    result.append(x)
            return result


class SetPyDifferenceNode(SetPyTreeNode):

    def __contains__(self, item):
        return (item in self.s1) and (item not in self.s2)

    def is_finite(self):
        return self.s1.is_finite()

    def cardinality(self):
        intersect = self.s1.intersect(self.s2)
        return self.s1.cardinality() - intersect.cardinality()

    def elems(self):
        if not self.is_finite():
            raise Exception("Set is infinite, cannot get all elements")
        else:
            result = []
            for x in self.s1.elems():
                if (x not in result) and (x not in self.s2):
                    result.append(x)
            return result


class FiniteSetPy(SetPy):
    """
    A set defined by a predetermined list of items rather than a range
    """

    def __init__(self, elems=None):
        self._elems = []
        if isinstance(elems, list):
            for i, e in enumerate(elems):
                if e not in self._elems:
                    self._elems.append(e)
        elif elems is not None:
            raise TypeError("Input must be of type List")

    def __contains__(self, item):
        return item in self._elems

    def elems(self):
        return self._elems

    def is_finite(self):
        return True

    def cardinality(self):
        return len(self._elems)

    def union(self, other):
        if not isinstance(other, SetPy):
            raise TypeError("Can only union with another SetPy")
        elif other.is_finite():
            return FiniteSetPy(self.elems() + other.elems())
        else:
            # May need to change this, prevent nested SetPyUnionNodes
            reduced_self_elems = [x for x in self.elems() if x not in other]
            return SetPyUnionNode(FiniteSetPy(reduced_self_elems), other)

    def intersect(self, other):
        if not isinstance(other, SetPy):
            raise TypeError("Can only intersect with another SetPy")
        return FiniteSetPy([x for x in self.elems() if x in other])

    def difference(self, other):
        if not isinstance(other, SetPy):
            raise TypeError("Can only make difference with another SetPy")
        return FiniteSetPy([x for x in self.elems() if x not in other])

    def is_subset(self, other):
        if not isinstance(other, SetPy):
            raise TypeError("Can only be subset of another SetPy")
        return all([x in other for x in self.elems()])


class RangesSetPy(SetPy):
    """
    A series of disjoint open ranges, consisting of either integers or real numbers.
    """

    def __init__(self, real_ranges, int_ranges):
        # real_ranges and int_ranges must be list of numbers
        if not isinstance(real_ranges, list):
            raise TypeError("Real ranges must be a list")
        elif not isinstance(int_ranges, list):
            raise TypeError("Int ranges must be a list")
        elif (len(real_ranges) % 2) != 0:
            raise ValueError("Both lists of ranges must have even length")
        elif (len(int_ranges) % 2) != 0:
            raise ValueError("Both lists of ranges must have even length")
        elif int_ranges != sorted(int_ranges):
            raise ValueError("Int ranges must be sorted")
        elif real_ranges != sorted(real_ranges):
            raise ValueError("Real ranges must be sorted")
        self.real_ranges = copy.deepcopy(real_ranges)
        self.int_ranges = copy.deepcopy(int_ranges)

    def get_real_range_pairs(self):
        return zip(self.real_ranges, self.real_ranges[1:])[::2]

    def get_int_range_pairs(self):
        return zip(self.int_ranges, self.int_ranges[1:])[::2]

    def __contains__(self, item):
        if not isinstance(item, numbers.Number):
            return False
        elif int(item) == item and any(p[0] < item < p[1] for p in self.get_int_range_pairs()):
            return True
        return any(p[0] < item < p[1] for p in self.get_real_range_pairs())

    @classmethod
    def _int_range_len(cls, lower, upper):
        length = math.ceil(upper) - math.floor(lower) - 1
        return length if length >= 0 else 0

    def cardinality(self):
        if len(self.real_ranges) > 0:
            return REAL_CARD
        elif any(isinstance(x, Infinity) for x in self.int_ranges):
            return NAT_CARD
        else:
            return sum(RangesSetPy._int_range_len(*p) for p in self.get_int_range_pairs())

    def is_finite(self):
        return not isinstance(self.cardinality(), Infinity)

    def elems(self):
        if self.is_finite():
            # If finite, no real ranges
            result = []
            for p in self.get_int_range_pairs():
                lower = p[0] + 1
                upper = RangesSetPy._int_range_len(*p) + lower
                result.append(range(lower, upper))
            return result
        else:
            raise Exception("Is infinite, cannot get all elements")

    def _absorb_ints_into_reals(self):
        """
        Reduce integer ranges to make them disjoint from real ranges.
        """
        ints_range = RangesSetPy(copy.deepcopy(self.int_ranges), [])
        reals_range = RangesSetPy(copy.deepcopy(self.real_ranges), [])
        resulting_int_range = ints_range.difference(reals_range)
        self.int_ranges = resulting_int_range.real_ranges

    def union(self, other):
        if not isinstance(other, SetPy):
            raise TypeError("Can only union with another SetPy")
        elif isinstance(other, RangesSetPy):
            # Put all ranges in one ordered list together
            # Continuously iterate over all elements, unioning them if intersecting
            # If list remains identical after iteration, finish
            ranges = []
            for range_pairs in [self.get_real_range_pairs() + other.get_real_range_pairs(),
                                self.get_int_range_pairs() + other.get_int_range_pairs()]:
                new_range_pairs = sorted(range_pairs,
                                         key=lambda p: p[0])
                old_range_pairs = []
                while new_range_pairs != old_range_pairs:
                    old_range_pairs = copy.deepcopy(new_range_pairs)
                    for p1, p2 in zip(new_range_pairs, new_range_pairs[1:]):
                        if p1[0] <= p2[0] <= p1[1] and p1[0] <= p2[1] <= p1[1]:
                            new_range_pairs.remove(p2)
                            break   # Has modified list, so zipped list being iterated over is now outdated
                        elif p2[0] <= p1[0] <= p2[1] and p2[0] <= p1[1] <= p2[1]:
                            new_range_pairs.remove(p1)
                            break
                        elif p1[0] <= p2[0] < p1[1]:
                            new_range_pairs.remove(p1)
                            new_range_pairs[new_range_pairs.index(p2)] = (p1[0], p2[1])
                            break
                        elif p1[0] < p2[1] <= p1[1]:
                            new_range_pairs.remove(p1)
                            new_range_pairs[new_range_pairs.index(p2)] = (p2[0], p1[1])
                            break
                range_ls = sorted([x[0] for x in old_range_pairs] + [x[1] for x in old_range_pairs])
                ranges.append(range_ls)
            result = RangesSetPy(*ranges)
            result._absorb_ints_into_reals()    # Doesn't work yet as difference is not finished
            return result
        elif self.is_finite():
            # other must be finite set
            return FiniteSetPy(self.elems() + other.elems())
        else:
            # TODO
            return SetPyUnionNode(self, other.difference(self))

    def intersect(self, other):
        # TODO
        return self

    def difference(self, other):
        # TODO
        return self

    def is_subset(self, other):
        if not isinstance(other, SetPy):
            raise TypeError("Can only be subset of a SetPy")
        elif isinstance(other, RangesSetPy):
            intersect = self.intersect(other)
            return sorted(intersect.real_ranges) == sorted(self.real_ranges) and \
                sorted(intersect.int_ranges) == sorted(self.int_ranges)
        elif self.is_finite():
            return FiniteSetPy(self.elems()).is_subset(other)
        elif other.is_finite():
            return False
        else:
            # Must be a union node (intersect and difference can be handled by RangesSetPy and FiniteSetPy)
            # TODO
            raise TypeError("Not able to deduce if subset")


class RealSetPy(object):

    def __new__(cls):
        return RangesSetPy([NEG_INF, INFINITY], [])


class IntegerSetPy(object):

    def __new__(cls):
        return RangesSetPy([], [NEG_INF, INFINITY])


class NaturalSetPy(object):

    def __new__(cls):
        return RangesSetPy([], [0, INFINITY])
