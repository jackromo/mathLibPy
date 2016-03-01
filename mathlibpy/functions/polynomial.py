import function


class Polynomial(function.Function):

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

    def _evaluate(self, x):
        return sum(self[i]*(x**i) for i in range(self.degree+1))

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
            return all(self[i] == other[i] for i in range(self.degree))

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError("Tried to index with a non-integer")
        elif item < 0:
            raise ValueError("Tried to index term of exponent < 0")
        elif item > self.degree:
            return 0    # Polynomial has infinite terms, but ones > degree have coefficient 0
        else:
            return self.coeffs[item]

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError("Tried to index with a non-integer")
        elif key < 0:
            raise ValueError("Tried to index term of exponent < 0")
        elif key > self.degree:
            self.coeffs.extend([0 for _ in range(key - self.degree - 1)] + [value])
            # Degree automatically updated by coeffs setter
        else:
            self.coeffs[key] = value

    def get_derivative(self):
        if self.degree == 0:
            return function.Constant(0)
        else:
            return Polynomial([self.coeffs[i]*i for i in range(1, self.degree+1)])