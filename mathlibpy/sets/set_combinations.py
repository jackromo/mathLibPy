import sets
import abc


class SetPyCombinationFactory(object):

    __metaclass__ = abc.ABCMeta

    def __new__(cls, set1, set2):
        if isinstance(set1, sets.FiniteSetPy):
            if isinstance(set2, sets.FiniteSetPy):
                return cls._combine_finiteset_finiteset(set1, set2)
            elif isinstance(set2, sets.IntervalSetPy):
                return cls._combine_finiteset_interval(set1, set2)
            elif isinstance(set2, sets.UniqueSetsUnionSetPy):
                return cls._combine_finiteset_uniqueunion(set1, set2)
            else:
                raise TypeError("set2 not recognized type of set")
        elif isinstance(set1, sets.IntervalSetPy):
            if isinstance(set2, sets.FiniteSetPy):
                return cls._combine_interval_finiteset(set1, set2)
            elif isinstance(set2, sets.IntervalSetPy):
                return cls._combine_interval_interval(set1, set2)
            elif isinstance(set2, sets.UniqueSetsUnionSetPy):
                return cls._combine_interval_uniqueunion(set1, set2)
            else:
                raise TypeError("set2 not recognized type of set")
        elif isinstance(set1, sets.UniqueSetsUnionSetPy):
            if isinstance(set2, sets.FiniteSetPy):
                return cls._combine_uniqueunion_finiteset(set1, set2)
            elif isinstance(set2, sets.IntervalSetPy):
                return cls._combine_uniqueunion_interval(set1, set2)
            elif isinstance(set2, sets.UniqueSetsUnionSetPy):
                return cls._combine_uniqueunion_uniqueunion(set1, set2)
            else:
                raise TypeError("set2 not recognized type of set")
        else:
            raise TypeError("set1 not recognized type of set")

    @classmethod
    @abc.abstractmethod
    def _combine_finiteset_finiteset(cls, set1, set2):
        """
        Combine a FiniteSetPy with a FiniteSetPy.
        """

    @classmethod
    @abc.abstractmethod
    def _combine_finiteset_interval(cls, set1, set2):
        """
        Combine a FiniteSetPy with an IntervalSetPy.
        """

    @classmethod
    @abc.abstractmethod
    def _combine_finiteset_uniqueunion(cls, set1, set2):
        """
        Combine a FiniteSetPy with a UniqueUnionSetPy.
        """

    @classmethod
    @abc.abstractmethod
    def _combine_interval_finiteset(cls, set1, set2):
        """
        Combine an IntervalSetPy with a FiniteSetPy.
        """

    @classmethod
    @abc.abstractmethod
    def _combine_interval_interval(cls, set1, set2):
        """
        Combine an IntervalSetPy with an IntervalSetPy.
        """

    @classmethod
    @abc.abstractmethod
    def _combine_interval_uniqueunion(cls, set1, set2):
        """
        Combine an IntervalSetPy with a UniqueUnionSetPy.
        """

    @classmethod
    @abc.abstractmethod
    def _combine_uniqueunion_finiteset(cls, set1, set2):
        """
        Combine a UniqueUnionSetPy with a FiniteSetPy.
        """

    @classmethod
    @abc.abstractmethod
    def _combine_uniqueunion_interval(cls, set1, set2):
        """
        Combine a UniqueUnionSetPy with an IntervalSetPy.
        """

    @classmethod
    @abc.abstractmethod
    def _combine_uniqueunion_uniqueunion(cls, set1, set2):
        """
        Combine a UniqueUnionSetPy with a UniqueUnionSetPy.
        """


class SetUnion(SetPyCombinationFactory):
    """
    Set of elements either in self or in other.
    """

    @classmethod
    def _combine_finiteset_finiteset(cls, set1, set2):
        return sets.FiniteSetPy(set1.elems() + set2.elems())

    @classmethod
    def _combine_finiteset_interval(cls, set1, set2):
        return sets.UniqueSetsUnionSetPy([set1, set2])

    @classmethod
    def _combine_finiteset_uniqueunion(cls, set1, set2):
        return sets.UniqueSetsUnionSetPy([set1] + set2.sets_ls)

    @classmethod
    def _combine_interval_finiteset(cls, set1, set2):
        return cls._combine_finiteset_interval(set1, set2)

    @classmethod
    def _combine_interval_interval(cls, set1, set2):
        if set1.is_subset(set2):
            return set2
        elif set2.is_subset(set1):
            return set1
        else:
            set1_diff = SetDifference(set1, set2)
            return sets.UniqueSetsUnionSetPy([set1_diff, set2])

    @classmethod
    def _combine_interval_uniqueunion(cls, set1, set2):
        return sets.UniqueSetsUnionSetPy([set1] + set2.sets_ls)

    @classmethod
    def _combine_uniqueunion_finiteset(cls, set1, set2):
        return cls._combine_finiteset_uniqueunion(set1, set2)

    @classmethod
    def _combine_uniqueunion_interval(cls, set1, set2):
        return cls._combine_interval_uniqueunion(set1, set2)

    @classmethod
    def _combine_uniqueunion_uniqueunion(cls, set1, set2):
        return sets.UniqueSetsUnionSetPy(set1.sets_ls + set2.sets_ls)


class SetIntersect(SetPyCombinationFactory):
    """
    Set of elements both in self and in other.
    """

    @classmethod
    def _combine_finiteset_finiteset(cls, set1, set2):
        return sets.FiniteSetPy([x for x in set1.elems() if x in set2])

    @classmethod
    def _combine_finiteset_interval(cls, set1, set2):
        return sets.FiniteSetPy([x for x in set1.elems() if x in set2])

    @classmethod
    def _combine_finiteset_uniqueunion(cls, set1, set2):
        return sets.FiniteSetPy([x for x in set1.elems() if x in set2])

    @classmethod
    def _combine_interval_finiteset(cls, set1, set2):
        return cls._combine_finiteset_interval(set1, set2)

    @classmethod
    def _combine_interval_interval(cls, set1, set2):
        if set1.range_type.is_subset(set2.range_type):
            min_val = set1.lowest if set2.lowest not in set1 else max(set1.lowest, set2.lowest)
            max_val = set1.highest if set2.highest not in set1 else min(set1.highest, set2.highest)
            return sets.IntervalSetPy(set1.range_type, min_val, max_val)
        elif set2.range_type.is_subset(set1.range_type):
            min_val = set2.lowest if set1.lowest not in set2 else max(set2.lowest, set1.lowest)
            max_val = set2.highest if set1.highest not in set2 else min(set2.highest, set1.highest)
            return sets.IntervalSetPy(set2.range_type, min_val, max_val)
        else:
            return sets.FiniteSetPy([])

    @classmethod
    def _combine_interval_uniqueunion(cls, set1, set2):
        return reduce(
            lambda accum, new: SetUnion(accum, SetIntersect(set1, new)),
            set2.sets_ls,
            sets.FiniteSetPy([])
        )

    @classmethod
    def _combine_uniqueunion_finiteset(cls, set1, set2):
        return cls._combine_finiteset_uniqueunion(set1, set2)

    @classmethod
    def _combine_uniqueunion_interval(cls, set1, set2):
        return cls._combine_interval_uniqueunion(set1, set2)

    @classmethod
    def _combine_uniqueunion_uniqueunion(cls, set1, set2):
        return reduce(
            lambda accum, new: SetUnion(accum, SetIntersect(set2, new)),
            set1.sets_ls,
            sets.FiniteSetPy([])
        )


class SetDifference(SetPyCombinationFactory):
    """
    Set of elements in self but not in other.
    """

    @classmethod
    def _combine_finiteset_finiteset(cls, set1, set2):
        return sets.FiniteSetPy([x for x in set1.elems() if x not in set2])

    @classmethod
    def _combine_finiteset_interval(cls, set1, set2):
        return sets.FiniteSetPy([x for x in set1.elems() if x not in set2])

    @classmethod
    def _combine_finiteset_uniqueunion(cls, set1, set2):
        return sets.FiniteSetPy([x for x in set1.elems() if x not in set2])

    @classmethod
    def _combine_interval_finiteset(cls, set1, set2):
        final_sets = []
        intersecting_elems = SetIntersect(set1, set2).elems()
        if len(intersecting_elems) == 0:
            return set1
        # All intersecting elements are in an interval set, implies is orderable
        next_lowest = set1.lowest
        for next_highest in [set1.lowest] + sorted(intersecting_elems) + [set1.highest]:
            final_sets.append(sets.IntervalSetPy(set1.range_type, next_lowest, next_highest))
        return reduce(
            lambda accum, new: SetUnion(accum, new),
            final_sets,
            sets.FiniteSetPy([])
        )

    @classmethod
    def _combine_interval_interval(cls, set1, set2):
        # TODO
        pass

    @classmethod
    def _combine_interval_uniqueunion(cls, set1, set2):
        return reduce(
            lambda accum, new: SetDifference(accum, new),
            set2.sets_ls,
            set1
        )

    @classmethod
    def _combine_uniqueunion_finiteset(cls, set1, set2):
        return sets.UniqueSetsUnionSetPy([SetDifference(x, set2) for x in set1.sets_ls])

    @classmethod
    def _combine_uniqueunion_interval(cls, set1, set2):
        return sets.UniqueSetsUnionSetPy([SetDifference(x, set2) for x in set1.sets_ls])

    @classmethod
    def _combine_uniqueunion_uniqueunion(cls, set1, set2):
        return sets.UniqueSetsUnionSetPy([SetDifference(x, set2) for x in set1.sets_ls])
