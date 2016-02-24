

class Polynomial(object):

    def __init__(self, coeffs):
        """
        1 parameter:
        coeff (list): coeff[n] = coefficient of nth degree term
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
            self._coeffs = c


def main():
    p1 = Polynomial([1]) # p = 1
    p2 = Polynomial([2, 3, 4])  # p = 2 + 3x + 4x^2
    assert(p1.degree == 0)
    assert(p2.degree == 2)
    assert(p2.coeffs == [2, 3, 4])

if __name__ == "__main__":
    main()
