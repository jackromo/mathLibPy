"""
SetPy and all its subclasses.

Author: Jack Romo <sharrackor@gmail.com>
"""

# NOTE: This module is unfinished; do not use it.

import set_combinations
import universes
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

        Args:
            item: Item to be checked for presence in self.

        Returns:
            bool: True if item in self, False otherwise.
        """

    @abc.abstractmethod
    def cardinality(self):
        """
        Returns:
            number: Number of elements in set. int if finite, Infinity otherwise.
        """

    @abc.abstractmethod
    def elems(self):
        """
        If finite, return all elements. If not, raise an exception.

        Returns:
            list: List of all elements in set.

        Raises:
            Exception: Set is infinite, so all elements cannot be captured in a list.
        """

    @abc.abstractmethod
    def is_subset(self, other):
        """
        Check whether self is subset of other.

        Args:
            other (SetPy): Set being checked if self is subset of.

        Returns:
            bool: True if all elements in self are in other, False otherwise.
        """

    def is_finite(self):
        """
        Returns:
             bool: True if set is finite, False otherwise.
        """
        return not isinstance(self.cardinality(), Infinity)

    def is_disjoint(self, other):
        """
        Check if both sets are disjoint.

        Args:
            other (SetPy): Set to compare with self.

        Returns:
            bool: True if no elements in self are in other, False otherwise.
        """
        if not isinstance(other, SetPy):
            raise TypeError("Can only be disjoint with another SetPy")
        return set_combinations.SetIntersect(self, other).cardinality() == 0

    def __eq__(self, other):
        """
        Check whether sets are exactly equal.

        Args:
            other (SetPy): Other set to check against.

        Returns:
            bool: True if other is SetPy and both sets are subsets of each other, False otherwise.
        """
        if not isinstance(other, SetPy):
            return False
        return self.is_subset(other) and other.is_subset(self)

    def is_proper_subset(self, other):
        """
        Check whether self is proper subset of other.

        Args:
            other (SetPy): Set being checked against.

        Returns:
            bool: True if all elements in self are elements in other and not vice versa, False otherwise.
        """
        if not isinstance(other, SetPy):
            raise TypeError("Can only be proper subset of another SetPy")
        return self.is_subset(other) and not self == other


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
    # TODO: documentation

    def __init__(self, range_type, lowest, highest):
        if not isinstance(range_type, universes.TypeUniverseSet):
            raise TypeError("Range_type must be a TypeUniverseSet")
        self.range_type = range_type
        self.lowest = lowest
        self.highest = highest

    def __contains__(self, item):
        if not isinstance(item, self.range_type):
            return False
        return self.lowest < item < self.highest

    def cardinality(self):
        if self.range_type.is_sparse():
            if not (isinstance(self.lowest, Infinity) or isinstance(self.highest, Infinity)):
                return len(self.elems())
            else:
                return self.range_type.cardinality()
        else:
            # Assume cardinality of smaller range is same as total when not sparse (not always true)
            return self.range_type.cardinality()

    def elems(self):
        return self.range_type.elems_in_range(self.lowest, self.highest)

    def is_subset(self, other):
        if self.is_finite():
            return all(x in other for x in self.elems())
        elif other.is_finite():
            return False
        elif isinstance(other, IntervalSetPy):
            if self.range_type.is_subset(other.range_type):
                return self.lowest >= other.lowest and self.highest <= other.highest
            else:
                return False
        elif isinstance(other, universes.UniverseIntersect):
            return self.is_subset(other.set1) and self.is_subset(other.set2)
        elif isinstance(other, universes.UniverseUnion):
            return set_combinations.SetDifference(self, other.set2).is_subset(other.set1) and\
                   set_combinations.SetDifference(self, other.set1).is_subset(other.set2)
        elif isinstance(other, universes.UniverseDifference):
            return self.is_subset(other.set1) and self.is_disjoint(other.set2)
        elif isinstance(other, UniqueSetsUnionSetPy):
            return self.is_subset(set_combinations.SetIntersect(self, other))


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
                    if not s1.is_disjoint(s2):
                        sets_ls.remove(s1)
                        sets_ls.insert(i, set_combinations.SetDifference(s1, s2))
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
        return IntervalSetPy(universes.RealNumberUniverse(), NEG_INF, INFINITY)


class IntegerSetPy(object):
    """
    The set of all integers, regardless of sign.
    """

    def __new__(cls):
        return IntervalSetPy(universes.IntegerUniverse(), NEG_INF, INFINITY)


class NaturalSetPy(object):
    """
    The set of all non-negative integers.
    """

    def __new__(cls):
        return IntervalSetPy(universes.IntegerUniverse(), 0, INFINITY)
