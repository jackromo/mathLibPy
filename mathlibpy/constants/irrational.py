import numbers


class IrrationalNumber(numbers.Number):
    """
    Irrational numbers must be a different type from floats, as all floats are rational.
    (This is due to them all having finite decimal places.)
    """

    TEST_ACCURACY = 10     # number of decimal places needed to be equal for 2 irrational numbers to be equal

    def __init__(self, val):
        if not (isinstance(val, int) or isinstance(val, float)):
            raise TypeError("Irrational number requires base Number value")
        self.val = val

    def __lt__(self, other):
        if isinstance(other, IrrationalNumber):
            return self.val < other.val
        return self.val < other

    def __eq__(self, other):
        if not isinstance(other, IrrationalNumber):
            return False
        elif other.val == self.val:
            return True
        else:
            # see if both values return same number up to a degree of accuracy
            return round(other.val, IrrationalNumber.TEST_ACCURACY) == \
                   round(self.val, IrrationalNumber.TEST_ACCURACY)

    def __gt__(self, other):
        if isinstance(other, IrrationalNumber):
            return self.val > other.val
        return self.val > other

    def __float__(self):
        return self.val

    def __int__(self):
        return int(round(self.val, 0))

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return IrrationalNumber(self.val + other)
        elif isinstance(other, IrrationalNumber):
            return IrrationalNumber(self.val + other.val)
        else:
            return self.val + other

    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return IrrationalNumber(self.val - other)
        elif isinstance(other, IrrationalNumber):
            return IrrationalNumber(self.val - other.val)
        else:
            return self.val - other

    def __neg__(self):
        return IrrationalNumber(-self.val)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return 0 if other == 0 else IrrationalNumber(self.val * other)
        elif isinstance(other, IrrationalNumber):
            return IrrationalNumber(self.val * other.val)
        else:
            return self.val * other

    def __div__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            if other == 0:
                raise ZeroDivisionError()
            return IrrationalNumber(self.val / float(other))
        elif isinstance(other, IrrationalNumber):
            return IrrationalNumber(self.val / float(other.val))
        else:
            return self.val / float(other)

    def __pow__(self, power):
        if isinstance(power, int) or isinstance(power, float):
            if power == 0:
                return 1
            return IrrationalNumber(self.val ** power)
        elif isinstance(power, IrrationalNumber):
            return IrrationalNumber(self.val ** power.val)
        else:
            return self.val ** power


# Irrational numbers
PI = IrrationalNumber(3.14159265)
E = IrrationalNumber(2.718281828)

