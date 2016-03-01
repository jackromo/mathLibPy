import abc


class SetPy(object):
    """
    A collection of arbitrary entities.
    """

    __metaclass__ = abc.ABCMeta

    def __init__(self, elems=None):
        self.elems = []
        if isinstance(elems, list):
            for i, e in enumerate(elems):
                if e not in self.elems:
                    self.elems.append(e)
        elif elems is not None:
            raise TypeError("Input must be of type List")

    def __contains__(self, item):
        return item in self.elems

    @property
    def elems(self):
        return self._elems

    @elems.setter
    def elems(self, x):
        if not isinstance(x, list):
            raise TypeError("Elems must be a list")
        self._elems = x

    def cardinality(self):
        return len(self.elems)

    def union(self, other):
        """
        Addition of sets is union.
        """
        if not isinstance(other, SetPy):
            raise TypeError("Can only union with another Set")
        return SetPy(self.elems + other.elems)

    def difference(self, other):
        """
        Subtraction of sets is set difference.
        """
        if not isinstance(other, SetPy):
            raise TypeError("Can only take difference with another Set")
        return SetPy([x for x in self.elems if x not in other.elems])

    def intersect(self, other):
        if not isinstance(other, SetPy):
            raise TypeError("Can only intersect with another Set")
        return SetPy([x for x in self.elems if x in other.elems])

    def is_disjoint(self, other):
        if not isinstance(other, SetPy):
            raise TypeError("Can only be disjoint with another Set")
        return all(x not in other.elems for x in self.elems)

    def is_subset(self, other):
        if not isinstance(other, SetPy):
            raise TypeError("Can only be subset of another Set")
        return all(x in other.elems for x in self.elems)

    def __eq__(self, other):
        if not isinstance(other, SetPy):
            return False
        return self.is_subset(other) and other.is_subset(self)

    def is_proper_subset(self, other):
        return self.is_subset(other) and self != other
