import abc
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
            result = 0
            for elem in self.s1.elems():
                if elem in self.s2:
                    result += 1
            return result
        elif self.s2.is_finite():
            result = 0
            for elem in self.s2.elems():
                if elem in self.s1:
                    result += 1
            return result
        else:
            # Placeholder, when infinite sets developed then will return correct infinity
            return INFINITY

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
    A set defined by a predetermined list of items rather than a comprehension
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


class InfiniteSetPy(SetPy):

    __metaclass__ = abc.ABCMeta

    def cardinality(self):
        return INFINITY

    def is_finite(self):
        return False

    def elems(self):
        raise Exception("Set is infinite, cannot get all elems")


class RealSet(InfiniteSetPy):

    def __contains__(self, item):
        return isinstance(item, float)

    def cardinality(self):
        return REAL_CARD


class RationalSet(InfiniteSetPy):

    def __contains__(self, item):
        # Technically, as all numbers on a computer have finite decimal length,
        # multiplying by a large enough power of 10 makes an integer,
        # so all possible number arguments are rational.
        return isinstance(item, float)

    def cardinality(self):
        return NAT_CARD


class IntegerSet(InfiniteSetPy):

    def __contains__(self, item):
        return isinstance(item, int)

    def cardinality(self):
        return NAT_CARD


class NaturalSet(InfiniteSetPy):

    def __contains__(self, item):
        if isinstance(item, int):
            return item > 0
        return False

    def cardinality(self):
        return NAT_CARD
