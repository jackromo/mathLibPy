"""
.. module:: sets
    :synopsis: SetPy and all its subclasses.

.. moduleauthor:: Jack Romo <sharrackor@gmail.com>
"""

# NOTE: This module is unfinished; do not use it.


import abc
from mathlibpy.constants import *


class SetPy(object):
    """
    A collection of arbitrary unordered entities.
    """

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __contains__(self, item):
        """
        Check if contains item.

        :type item: Any
        :param item: Item to be checked for presence in self.
        :rtype: bool
        :return: True if item in self, False otherwise.
        """

    @abc.abstractmethod
    def cardinality(self):
        """
        Return number of items in set.

        :rtype: number (int if finite, Infinity otherwise)
        :return: Number of elements in set.
        """

    @abc.abstractmethod
    def elems(self):
        """
        If finite, return all elements. If not, raise an exception.

        :rtype: list
        :return: List of all elements in set.
        :raise: Exception (Set is infinite, so all elements cannot be captured in a list)
        """

    @abc.abstractmethod
    def is_subset(self, other):
        """
        Check whether self is subset of other.

        :type other: SetPy
        :param other: Set being checked if self is subset of.
        :rtype: bool
        :return: True if all elements in self are in other, False otherwise.
        """

    def is_finite(self):
        """
        Return whether has a finite number of elements.

        :rtype: bool
        :return: True if set is finite, False otherwise.
        """
        return not isinstance(self.cardinality(), Infinity)

    def is_disjoint(self, other):
        """
        Check if both sets are disjoint.

        :type other: SetPy
        :param other: Set to compare with self.
        :rtype: bool
        :return: True if no elements in self are in other, False otherwise.
        """
        if not isinstance(other, SetPy):
            raise TypeError("Can only be disjoint with another SetPy")
        return SetIntersect(self, other).cardinality() == 0

    def __eq__(self, other):
        """
        Check whether sets are exactly equal.

        :type other: Any
        :rtype: bool
        :return: True if other is SetPy and both sets are subsets of each other, False otherwise.
        """
        if not isinstance(other, SetPy):
            return False
        return self.is_subset(other) and other.is_subset(self)

    def is_proper_subset(self, other):
        """
        Check whether self is proper subset of other.

        :type other: SetPy
        :param other: Set being checked against.
        :rtype: bool
        :return: True if all elements in self are elements in other and not vice versa, False otherwise.
        """
        if not isinstance(other, SetPy):
            raise TypeError("Can only be proper subset of another SetPy")
        return self.is_subset(other) and not self == other


class SetPyCombinationFactory(object):
    # TODO: declare all combination cases.

    __metaclass__ = abc.ABCMeta

    def __new__(cls, set1, set2):
        if isinstance(set1, FiniteSetPy):
            if isinstance(set2, FiniteSetPy):
                return cls._combine_finiteset_finiteset(set1, set2)
            elif isinstance(set2, IntervalSetPy):
                return cls._combine_finiteset_interval(set1, set2)
            elif isinstance(set2, UniqueSetsUnionSetPy):
                return cls._combine_finiteset_uniqueunion(set1, set2)
            else:
                raise TypeError("set2 not recognized type of set")
        elif isinstance(set1, IntervalSetPy):
            if isinstance(set2, FiniteSetPy):
                return cls._combine_interval_finiteset(set1, set2)
            elif isinstance(set2, IntervalSetPy):
                return cls._combine_interval_interval(set1, set2)
            elif isinstance(set2, UniqueSetsUnionSetPy):
                return cls._combine_interval_uniqueunion(set1, set2)
            else:
                raise TypeError("set2 not recognized type of set")
        elif isinstance(set1, UniqueSetsUnionSetPy):
            if isinstance(set2, FiniteSetPy):
                return cls._combine_uniqueunion_finiteset(set1, set2)
            elif isinstance(set2, IntervalSetPy):
                return cls._combine_uniqueunion_interval(set1, set2)
            elif isinstance(set2, UniqueSetsUnionSetPy):
                return cls._combine_uniqueunion_uniqueunion(set1, set2)
            else:
                raise TypeError("set2 not recognized type of set")
        else:
            raise TypeError("set1 not recognized type of set")

    @classmethod
    @abc.abstractmethod
    def _combine_finiteset_finiteset(cls, set1, set2):
        pass

    @classmethod
    @abc.abstractmethod
    def _combine_finiteset_interval(cls, set1, set2):
        pass

    @classmethod
    @abc.abstractmethod
    def _combine_finiteset_uniqueunion(cls, set1, set2):
        pass

    @classmethod
    @abc.abstractmethod
    def _combine_interval_finiteset(cls, set1, set2):
        pass

    @classmethod
    @abc.abstractmethod
    def _combine_interval_interval(cls, set1, set2):
        pass

    @classmethod
    @abc.abstractmethod
    def _combine_interval_uniqueunion(cls, set1, set2):
        pass

    @classmethod
    @abc.abstractmethod
    def _combine_uniqueunion_finiteset(cls, set1, set2):
        pass

    @classmethod
    @abc.abstractmethod
    def _combine_uniqueunion_interval(cls, set1, set2):
        pass

    @classmethod
    @abc.abstractmethod
    def _combine_uniqueunion_uniqueunion(cls, set1, set2):
        pass


class SetUnion(SetPyCombinationFactory):
    """
    Set of elements either in self or in other.
    """
    # TODO

    @classmethod
    def _combine_finiteset_finiteset(cls, set1, set2):
        pass

    @classmethod
    def _combine_finiteset_interval(cls, set1, set2):
        pass

    @classmethod
    def _combine_finiteset_uniqueunion(cls, set1, set2):
        pass

    @classmethod
    def _combine_interval_finiteset(cls, set1, set2):
        pass

    @classmethod
    def _combine_interval_interval(cls, set1, set2):
        pass

    @classmethod
    def _combine_interval_uniqueunion(cls, set1, set2):
        pass

    @classmethod
    def _combine_uniqueunion_finiteset(cls, set1, set2):
        pass

    @classmethod
    def _combine_uniqueunion_interval(cls, set1, set2):
        pass

    @classmethod
    def _combine_uniqueunion_uniqueunion(cls, set1, set2):
        pass


class SetIntersect(SetPyCombinationFactory):
    """
    Set of elements both in self and in other.
    """
    # TODO

    @classmethod
    def _combine_finiteset_finiteset(cls, set1, set2):
        pass

    @classmethod
    def _combine_finiteset_interval(cls, set1, set2):
        pass

    @classmethod
    def _combine_finiteset_uniqueunion(cls, set1, set2):
        pass

    @classmethod
    def _combine_interval_finiteset(cls, set1, set2):
        pass

    @classmethod
    def _combine_interval_interval(cls, set1, set2):
        pass

    @classmethod
    def _combine_interval_uniqueunion(cls, set1, set2):
        pass

    @classmethod
    def _combine_uniqueunion_finiteset(cls, set1, set2):
        pass

    @classmethod
    def _combine_uniqueunion_interval(cls, set1, set2):
        pass

    @classmethod
    def _combine_uniqueunion_uniqueunion(cls, set1, set2):
        pass


class SetDifference(SetPyCombinationFactory):
    """
    Set of elements in self but not in other.
    """
    # TODO

    @classmethod
    def _combine_finiteset_finiteset(cls, set1, set2):
        pass

    @classmethod
    def _combine_finiteset_interval(cls, set1, set2):
        pass

    @classmethod
    def _combine_finiteset_uniqueunion(cls, set1, set2):
        pass

    @classmethod
    def _combine_interval_finiteset(cls, set1, set2):
        pass

    @classmethod
    def _combine_interval_interval(cls, set1, set2):
        pass

    @classmethod
    def _combine_interval_uniqueunion(cls, set1, set2):
        pass

    @classmethod
    def _combine_uniqueunion_finiteset(cls, set1, set2):
        pass

    @classmethod
    def _combine_uniqueunion_interval(cls, set1, set2):
        pass

    @classmethod
    def _combine_uniqueunion_uniqueunion(cls, set1, set2):
        pass


class FiniteSetPy(SetPy):
    """
    A set defined by a predetermined list of items rather than a range.
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

    def cardinality(self):
        return len(self._elems)

    def is_subset(self, other):
        if not isinstance(other, SetPy):
            raise TypeError("Can only be subset of another SetPy")
        return all([x in other for x in self.elems()])


class IntervalSetPy(SetPy):
    """
    An interval from one point to another, within a universe of totally ordered entities.
    """
    # TODO: currently only supports ints and reals, must generalize to all types

    def __init__(self, range_type, lowest, highest):
        self.range_type = range_type
        self.lowest = lowest
        self.highest = highest

    def __contains__(self, item):
        if not isinstance(item, self.range_type):
            return False
        return self.lowest < item < self.highest

    def cardinality(self):
        if self.range_type == int:
            if self.is_finite():
                return max(self.highest - self.lowest - 1, 0)
            else:
                return NAT_CARD
        return REAL_CARD

    def elems(self):
        if self.is_finite():
            if self.range_type == int:
                if self.cardinality() == 0:
                    return []
                return range(self.lowest + 1, self.highest)
        raise Exception("Set is infinite, cannot collect all elements in list")

    def is_subset(self, other):
        if self.is_finite():
            return all(x in other for x in self.elems())
        elif other.is_finite():
            return False
        elif isinstance(other, IntervalSetPy):
            if self.range_type == other.range_type:
                return other.lowest <= self.lowest and other.highest >= self.highest
            elif self.range_type == int:
                return other.lowest <= self.lowest and other.highest >= self.highest
            elif self.range_type == numbers.Real:
                return False
        elif isinstance(other, UniqueSetsUnionSetPy):
            return self.is_subset(SetIntersect(self, other))


class UniqueSetsUnionSetPy(SetPy):
    """
    A union of several uniquely defined types of sets.
    """

    def __init__(self, sets_ls):
        if not all(isinstance(x, SetPy) for x in sets_ls):
            raise TypeError("Must provide list of SetPy objects")
        # Make all sets disjoint
        changed_sets_ls = True
        while changed_sets_ls:
            changed_sets_ls = False
            for i, s1 in enumerate(sets_ls):
                for j, s2 in enumerate(sets_ls[:i] + sets_ls[i+1:]):
                    if s1.is_disjoint(s2):
                        sets_ls.remove(s1)
                        sets_ls.insert(i, SetDifference(s1, s2))
                        changed_sets_ls = True
                        break
                if changed_sets_ls:
                    break
        self.sets_ls = sets_ls

    def __contains__(self, item):
        return any(item in s for s in self.sets_ls)

    def cardinality(self):
        return sum(s.cardinality() for s in self.sets_ls)

    def elems(self):
        if not self.is_finite():
            raise Exception("Set is infinite, cannot collect all elements in list")
        return sum([s.elems() for s in self.sets_ls], [])

    def is_subset(self, other):
        return all(s1.is_subset(other) for s1 in self)


class RealSetPy(object):
    """
    The set of all rational and irrational numbers.
    """

    def __new__(cls):
        return IntervalSetPy(numbers.Real, NEG_INF, INFINITY)


class IntegerSetPy(object):
    """
    The set of all integers, regardless of sign.
    """

    def __new__(cls):
        return IntervalSetPy(int, NEG_INF, INFINITY)


class NaturalSetPy(object):
    """
    The set of all non-negative integers.
    """

    def __new__(cls):
        return IntervalSetPy(int, 0, INFINITY)
