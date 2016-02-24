

class Polynomial(object):

    def __init__(self, coeffs):
        """
        1 parameter:
        coeffs (list): coeffs[n] = coefficient of nth degree term
        """
        self.coeffs = coeffs

    @property
    def coeffs(self):
        return self._coeffs

    @property
    def degree(self):
        return len(self.coeffs) - 1

    @coeffs.setter
    def coeffs(self, c):
        if not isinstance(c, list):
            raise TypeError("must provide list as arg")
        elif len(c) == 0:
            raise ValueError("arg length must be > 0")
        else:
            for i, d in enumerate(list(reversed(c))):
                if d != 0:
                    self._coeffs = c[:len(c) - i]
                    break

    def __str__(self):
        result = ""
        for i, c in enumerate(self.coeffs):
            if i == 0:
                result += str(c)
            elif c == 0:
                continue
            elif c < 0:
                result += " - {0}x^{1}".format(-c, i)
            else:
                result += " + {0}x^{1}".format(c, i)
        return result

    def __eq__(self, other):
        if not isinstance(other, Polynomial):
            return False
        elif self.degree != other.degree:
            return False
        else:
            return all(self.coeffs[i] == other.coeffs[i] for i in range(self.degree))


def main():
    p1 = Polynomial([1])        # p = 1
    p2 = Polynomial([2, 3, 4])  # p = 2 + 3x + 4x^2
    p3 = Polynomial([2, 3, 4, 0, 0])
    assert(p1.degree == 0)
    assert(p2.degree == p3.degree == 2)
    assert(p2.coeffs == p3.coeffs == [2, 3, 4])
    assert(p2.__str__() == "2 + 3x^1 + 4x^2")
    assert(p2 != p1)
    assert(p2 == p3 == Polynomial([2, 3, 4]))

if __name__ == "__main__":
    main()
