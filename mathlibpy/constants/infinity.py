"""
Infinity class and all infinite constants.

Author: Jack Romo <sharrackor@gmail.com>
"""

import numbers


class Infinity(numbers.Number):
    """
    An infinite number. Infinite numbers can be used in arithmetic and comparisons.
    Infinities are comparable with each other, and are considered numbers.
    Thus, they support all comparison and arithmetic operations.

    Notes:
        Infinities are not technically numbers, as they disobey arithmetic laws.
        For simplicity and consistency, they are considered to be numbers here.

    Warnings:
        When working with another non-infinite number, Infinity can only override the operator if it comes first.
        ie. oo + 1 works, but 1 + oo raises an error.
    """

    def __init__(self, rank, grp_id):
        """

        Args:
            rank (int): Defines ordering of infinity within its ordering group. Comparison compares ranks of infinities.
                        If rank is negative, then infinity is also negative.
            grp_id (int): ID of group of infinities that self can be meaningfully compared with.
        """
        self.rank = rank
        self.grp_id = grp_id

    def __lt__(self, other):
        """
        Returns:
            bool: True if other is Infinity, has own grp_id and higher rank than self. False otherwise.
        """
        if isinstance(other, Infinity):
            return self.grp_id == other.grp_id and self.rank < other.rank
        elif isinstance(other, numbers.Number):
            return self.rank < 0
        else:
            raise TypeError("Not comparable with non-number")

    def __eq__(self, other):
        """
        Returns:
            bool: True if other is Infinity and has same grp_id and rank as self, False otherwise.
        """
        if not isinstance(other, Infinity):
            return False
        return self.grp_id == other.grp_id and self.rank == other.rank

    def __gt__(self, other):
        """
        Returns:
            bool: True if other is Infinity, has own grp_id and lower rank than self. False otherwise.
        """
        if isinstance(other, Infinity):
            return self.grp_id == other.grp_id and self.rank > other.rank
        elif isinstance(other, numbers.Number):
            return self.rank >= 0
        else:
            raise TypeError("Not comparable with non-number")

    def __neg__(self):
        """
        Returns:
            bool: Infinity with same grp_id and negative rank of self.
        """
        return Infinity(-self.rank, self.grp_id)

    def __add__(self, other):
        """
        Args:
            other (number): Number to be added to.

        Returns:
             number: If other is an Infinity, return max of self and other. Otherwise, return self.
        """
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
        """
        Args:
            other (number): Number to subtract from self.

        Returns:
            bool: If other is a number, return self.
        """
        if isinstance(other, numbers.Number):
            return self
        else:
            raise TypeError("Not composable with non-number")

    def __mul__(self, other):
        """
        Args:
            other (number): Number to multiply by self.

        Returns:
             number: If other is an infinity, return negative self if other has opposite sign, else positive self.
                    Otherwise, return 0 if other is 0, or -self if other's sign is opposite to self.
        """
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
        """
        Args:
            other (number): Number to multiply by self.

        Returns:
            number: Self with opposite sign if own sign different from other sign.

        Raises:
             ZeroDivisionError
        """
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
"""General purpose infinity. Used as upper bound for real numbers."""
NEG_INF = Infinity(-1, 0)
"""General purpose negative infinity. Used as lower bound for real numbers."""
UNDEFINED = "undefined"
"""Undefined value. Returned if value does not exist."""

REAL_CARD = Infinity(2, 1)
"""Cardinality of real numbers. Strictly greater than NAT_CARD. Incomparable with INFINITY or NEG_INF."""
NAT_CARD = Infinity(1, 1)
"""Cardinality of natural numbers. Strictly less than REAL_CARD. Incomparable with INFINITY or NEG_INF."""
