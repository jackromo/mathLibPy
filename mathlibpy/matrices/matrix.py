"""
Matrix class.

Author: Jack Romo <sharrackor@gmail.com>
"""

from __future__ import division  # make division floating-point
import copy


class Matrix(object):
    """
    Generic m*n matrix.
    """

    def __init__(self, body=None, rows=1, cols=1):
        """
        Args:
            rows (int): Number of rows in matrix if None.
            cols (int): Number of columns in matrix if None.
            body (list[list], None): Matrix body as list of lists, each list being a matrix row.
        """
        if not body:
            # Default is all 0's
            self._body = [[0 for _ in range(cols)] for _ in range(rows)]
        else:
            if not isinstance(body, list):
                raise TypeError("body must be list row lists")
            elif not all(isinstance(body[i], list) for i in range(len(body))):
                raise TypeError("elements of body must be lists")
            else:
                self._body = body
        self._rows = len(self._body)
        self._cols = len(self._body[0])

    @property
    def rows(self):
        return self._rows

    @property
    def cols(self):
        return self._cols

    def __getitem__(self, key):
        """
        Index matrix as mat[x, y].

        Args:
            key (tuple(int, int)): Pair of x-y coordinates in matrix; x is column, y is row. 0-indexed.
        """
        return self._body[key[1]][key[0]]

    def __setitem__(self, key, value):
        self._body[key[1]][key[0]] = value

    def __str__(self):
        """
        Creates string of following form:

        [elem11 elem12 elem13 ...]
        [elem21 elem22 elem23 ...]
        ...
        """
        return "\n".join("[" + " ".join(str(i) for i in row) + "]" for row in self._body)

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        elif (self.rows != other.rows) or (self.cols != other.cols):
            return False
        else:
            return all(self[x, y] == other[x, y] for y in range(self.rows) for x in range(self.cols))

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Cannot add non-matrix to matrix")
        elif self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices do not have same dimensions")
        return Matrix([[self[x, y] + other[x, y] for x in range(self.cols)] for y in range(self.rows)])

    def __mul__(self, other):
        """
        Can multiply with scalar or Matrix.
        """
        if isinstance(other, type(self[0, 0])):
            return self._mul_scalar(other)
        elif isinstance(other, Matrix):
            return self._mul_matrix(other)
        else:
            raise TypeError("Can only multiply matrix with scalar or another matrix")

    @staticmethod
    def identity(cols):
        """
        Create a square identity matrix of a certain number of columns.

        Args:
            cols (int): Number of columns of produced identity matrix.

        Returns:
            Matrix: The identity matrix of prescribed number of columns.
        """
        return Matrix([[1 if r == c else 0 for c in range(cols)] for r in range(cols)])

    def _mul_scalar(self, other):
        return Matrix([[self[x, y]*other for x in range(self.cols)] for y in range(self.rows)])

    def _mul_matrix(self, other):
        # Assume that 'other' is a matrix, as tested in __mul__
        if self.cols != other.rows:
            raise ValueError("Matrix 1 must have same number of columns as rows of matrix 2")
        result = []
        for r in range(self.rows):
            result.append([])
            for c in range(other.cols):
                result[r].append(sum([self[i, r]*other[c, i] for i in range(self.cols)]))
        return Matrix(result)

    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Can only subtract matrix from matrix")
        # Addition checks dimensions are same
        return self + (other*(-1))

    def get_cofactor(self, i, j):
        """
        Get cofactor matrix from row i and column j.

        Args:
            i (int): Row to eliminate in matrix.
            j (int): Column to eliminate in matrix.

        Returns:
            Matrix: Matrix without row i and column j.
        """
        if not (isinstance(i, int) and isinstance(j, int)):
            raise ValueError("Coordinates must be integers")
        elif not (0 <= i <= (self.rows-1) and 0 <= j <= (self.cols-1)):
            raise ValueError("Must have 0<=row<=m-1 and 0<=col<=n-1")
        result = [[self[x, y] for x in range(self.cols) if x != j] for y in range(self.rows) if y != i]
        return Matrix(result)

    def get_determinant(self):
        """
        Returns:
            float: Scalar determinant of matrix.
        """
        if self.rows != self.cols:
            raise ValueError("Cannot take determinant of non-square matrix")
        elif self.rows == 1 and self.cols == 1:
            return self._body[0][0]
        else:
            return sum(((-1)**x)*(self[x, 0]*self.get_cofactor(0, x).get_determinant()) for x in range(self.cols))

    def transpose(self):
        """
        Transpose matrix in place.
        """
        self._body = [[self[y, x] for x in self.cols] for y in self.rows]

    def is_invertible(self):
        """
        Returns:
            bool: True if is an invertible matrix, False otherwise.
        """
        return (self.rows == self.cols) and (self.get_determinant() != 0)

    def get_echelon_form(self):
        """
        Returns:
             Matrix: Matrix that is echelon form of current one.
        """
        # Uses simplified version of Gauss-Jordan algorithm.
        result = copy.deepcopy(self)
        pivot_col = 0
        # Iterate through each column
        for pivot_row in range(self.rows):
            while result[pivot_col, pivot_row] == 0:
                # Check all lower rows, swap with one below
                has_swapped = False
                for r in range(pivot_row+1, result.rows):
                    if result[pivot_col, r] != 0:
                        # Found a swappable row, swap values
                        result._body[r], result._body[pivot_row] = result._body[pivot_row], result._body[r]
                        has_swapped = True
                if not has_swapped:
                    pivot_col += 1    # Skip to next column
            # Subtract multiples of current row from all lower rows to make rest of column zero
            for row in range(pivot_row+1, self.rows):
                factor = result[pivot_col, row] / result[pivot_col, pivot_row]
                result._body[row] = [result[c, row] - (factor*result[c, pivot_row])
                                     for c in range(result.cols)]
        return result

    def get_reduced_echelon_form(self):
        """
        Returns:
             Matrix: Matrix that is reduced echelon form of current one.
        """
        result = self.get_echelon_form()
        # Go up rows in reverse
        for pivot_row in range(self.rows-1, -1, -1):
            # Pivot is first nonzero element in row
            pivot = next(x for x in result._body[pivot_row] if x != 0)
            pivot_col = result._body[pivot_row].index(pivot)
            # Subtract multiples of current row from all above rows to make rest of column zero
            for row in range(pivot_row-1, -1, -1):
                factor = result[pivot_col, row] / pivot
                result._body[row] = [result[c, row] - (factor*result[c, pivot_row])
                                     for c in range(result.cols)]
        return result

    def get_row_reduced_echelon_form(self):
        """
        Returns:
             Matrix: Matrix that is row reduced echelon form of current one.
        """
        result = self.get_reduced_echelon_form()
        for row in range(result.rows):
            pivot = next(x for x in result._body[row] if x != 0)
            result._body[row] = [i / pivot for i in result._body[row]]
        return result

    def get_inverse(self):
        """
        Returns:
             Matrix: Matrix B such that self*B = B*self = Matrix.Identity(self.cols).

        Raises:
            ValueError: Matrix is not invertible.
        """
        if not self.is_invertible():
            raise ValueError("Matrix is not invertible")
        temp_self = copy.deepcopy(self)
        ident = Matrix.identity(temp_self.cols)
        # Append identity matrix to right of matrix
        for row in range(temp_self.rows):
            temp_self._body[row] = temp_self._body[row] + ident._body[row]
        # Unique update of body, must manually reset temp_self.cols
        temp_self._cols *= 2     # Is square matrix, so number of columns doubles
        rref_temp_self = temp_self.get_row_reduced_echelon_form()
        result = Matrix(None, self.rows, self.cols)
        # Identity appended on right is now inverse, as left is now identity
        for row in range(result.rows):
            result._body[row] = rref_temp_self._body[row][self.rows:]
        return result
