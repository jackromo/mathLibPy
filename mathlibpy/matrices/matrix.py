from __future__ import division  # make division floating-point
import copy


class Matrix(object):
    """
    Generic m*n matrix.
    """

    def __init__(self, rows, cols, body=None):
        """
        @note: Provision of number of rows and columns will soon be deprecated.
        @type rows: int
        @param rows: Number of rows in matrix.
        @type cols: int
        @param cols: Number of columns in matrix.
        @type body: list
        @param body: Matrix body as list of lists, each list being a matrix row.
        """
        self.rows = rows
        self.cols = cols
        if not body:
            # Default is all 0's
            self.body = [[0 for _ in range(cols)] for _ in range(rows)]
        else:
            if not isinstance(body, list):
                raise TypeError("body must be list row lists")
            elif not all(isinstance(body[i], list) for i in range(len(body))):
                raise TypeError("elements of body must be lists")
            elif rows != len(body):
                raise ValueError("number of rows supplied inconsistent with body")
            elif not all(cols == len(body[i]) for i in range(self.rows)):
                raise ValueError("body columns inconsistent with supplied value")
            else:
                self.body = body

    @property
    def rows(self):
        return self._rows

    @rows.setter
    def rows(self, r):
        assert(isinstance(r, int))
        self._rows = r

    @property
    def cols(self):
        return self._cols

    @cols.setter
    def cols(self, c):
        assert(isinstance(c, int))
        self._cols = c

    @property
    def body(self):
        """
        @note: This will soon be deprecated in favor of __getitem__ on tuples.
        """
        return self._body

    @body.setter
    def body(self, b):
        """
        @note: This will soon be deprecated in favor of __setitem__ on tuples.
        """
        if not isinstance(b, list):
            raise TypeError("body must be a list")
        elif not all(isinstance(b[i], list) for i in range(len(b))):
            raise TypeError("elements of body must be lists")
        elif not all(len(b[0]) == len(b[i]) for i in range(len(b))):
            raise TypeError("all rows must be of same length")
        else:
            self.rows = len(b)
            self.cols = len(b[0])
            self._body = b

    def __str__(self):
        """
        Creates string of following form:

        [elem11 elem12 elem13 ...]
        [elem21 elem22 elem23 ...]
        ...
        """
        return "\n".join("[" + " ".join(str(i) for i in row) + "]" for row in self.body)

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        elif (self.rows != other.rows) or (self.cols != other.cols):
            return False
        else:
            return all(self.body[r][c] == other.body[r][c] for r in range(self.rows) for c in range(self.cols))

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Cannot add non-matrix to matrix")
        elif self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices do not have same dimensions")
        return Matrix(self.rows, self.cols, [[self.body[r][c]+other.body[r][c] for c in range(self.cols)]
                                             for r in range(self.rows)])

    def __mul__(self, other):
        """
        Can multiply with scalar or Matrix.
        """
        if isinstance(other, type(self.body[0][0])):
            return self._mul_scalar(other)
        elif isinstance(other, Matrix):
            return self._mul_matrix(other)
        else:
            raise TypeError("Can only multiply matrix with scalar or another matrix")

    @staticmethod
    def identity(cols):
        """
        Create a square identity matrix of a certain number of columns.

        @type cols: int
        @param cols: Number of columns of produced identity matrix.
        @rtype: Matrix
        @return: The identity matrix of prescribed number of columns.
        """
        return Matrix(cols, cols, [[1 if r == c else 0 for c in range(cols)]
                                   for r in range(cols)])

    def _mul_scalar(self, other):
        return Matrix(self.rows,
                      self.cols,
                      [[self.body[r][c]*other for c in range(self.cols)]
                       for r in range(self.rows)])

    def _mul_matrix(self, other):
        # Assume that 'other' is a matrix, as tested in __mul__
        if self.cols != other.rows:
            raise ValueError("Matrix 1 must have same number of columns as rows of matrix 2")
        m1 = self.body
        m2 = other.body
        result = []
        for r in range(self.rows):
            result.append([])
            for c in range(other.cols):
                result[r].append(sum([m1[r][i]*m2[i][c] for i in range(self.cols)]))
        return Matrix(self.rows, other.cols, result)

    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Can only subtract matrix from matrix")
        # Addition checks dimensions are same
        return self + (other*(-1))

    def get_cofactor(self, i, j):
        """
        Get cofactor matrix from row i and column j.

        @type i: int
        @param i: Row to eliminate in matrix
        @type j: int
        @param j: Column to eliminate in matrix
        @rtype: Matrix
        @return: Matrix without row i and column j.
        """
        if not (isinstance(i, int) and isinstance(j, int)):
            raise ValueError("Coordinates must be integers")
        elif not (0 <= i <= (self.rows-1) and 0 <= j <= (self.cols-1)):
            raise ValueError("Must have 0<=row<=m-1 and 0<=col<=n-1")
        result = [[self.body[r][c] for c in range(self.cols) if c != j] for r in range(self.rows) if r != i]
        return Matrix(self.rows-1, self.cols-1, result)

    def get_determinant(self):
        """
        @rtype: float
        @return: Scalar determinant of matrix.
        """
        if self.rows != self.cols:
            raise ValueError("Cannot take determinant of non-square matrix")
        elif self.rows == 1 and self.cols == 1:
            return self.body[0][0]
        else:
            return sum(((-1)**c)*(self.body[0][c]*self.get_cofactor(0, c).get_determinant()) for c in range(self.cols))

    def transpose(self):
        """
        Transpose matrix in place.

        @return: Nothing.
        """
        self.body = [[self.body[c][r] for c in self.cols] for r in self.rows]

    def is_invertible(self):
        """
        @rtype: bool
        @return: True if is an invertible matrix, False otherwise.
        """
        return (self.rows == self.cols) and (self.get_determinant() != 0)

    def get_echelon_form(self):
        """
        @rtype: Matrix
        @return: Matrix that is echelon form of current one.
        """
        # Uses simplified version of Gauss-Jordan algorithm.
        result = copy.deepcopy(self)
        pivot_col = 0
        # Iterate through each column
        for pivot_row in range(self.rows):
            while result.body[pivot_row][pivot_col] == 0:
                # Check all lower rows, swap with one below
                has_swapped = False
                for r in range(pivot_row+1, result.rows):
                    if result.body[r][pivot_col] != 0:
                        # Found a swappable row, swap values
                        temp_row = result.body[r]
                        result.body[r] = result.body[pivot_row]
                        result.body[pivot_row] = temp_row
                        has_swapped = True
                if not has_swapped:
                    pivot_col += 1    # Skip to next column
            # Subtract multiples of current row from all lower rows to make rest of column zero
            for row in range(pivot_row+1, self.rows):
                factor = result.body[row][pivot_col] / result.body[pivot_row][pivot_col]
                result.body[row] = [result.body[row][c] - (factor*result.body[pivot_row][c])
                                    for c in range(result.cols)]
        return result

    def get_reduced_echelon_form(self):
        """
        @rtype: Matrix
        @return: Matrix that is reduced echelon form of current one.
        """
        result = self.get_echelon_form()
        # Go up rows in reverse
        for pivot_row in range(self.rows-1, -1, -1):
            # Pivot is first nonzero element in row
            pivot = next(x for x in result.body[pivot_row] if x != 0)
            pivot_col = result.body[pivot_row].index(pivot)
            # Subtract multiples of current row from all above rows to make rest of column zero
            for row in range(pivot_row-1, -1, -1):
                factor = result.body[row][pivot_col] / pivot
                result.body[row] = [result.body[row][c] - (factor*result.body[pivot_row][c])
                                    for c in range(result.cols)]
        return result

    def get_row_reduced_echelon_form(self):
        """
        @rtype: Matrix
        @return: Matrix that is row reduced echelon form of current one.
        """
        result = self.get_reduced_echelon_form()
        for row in range(result.rows):
            pivot = next(x for x in result.body[row] if x != 0)
            result.body[row] = [i / pivot for i in result.body[row]]
        return result

    def get_inverse(self):
        """
        @raise ValueError: Matrix is not invertible.
        @rtype: Matrix
        @return: Matrix B such that self*B = B*self = Matrix.Identity(self.cols).
        """
        if not self.is_invertible():
            raise ValueError("Matrix is not invertible")
        temp_self = copy.deepcopy(self)
        ident = Matrix.identity(temp_self.cols)
        # Append identity matrix to right of matrix
        for row in range(temp_self.rows):
            temp_self.body[row] = temp_self.body[row] + ident.body[row]
        # Unique update of body, must manually reset temp_self.cols
        temp_self.cols *= 2 # Is square matrix, so number of columns doubles
        rref_temp_self = temp_self.get_row_reduced_echelon_form()
        result = Matrix(self.rows, self.cols)
        # Identity appended on right is now inverse, as left is now identity
        for row in range(result.rows):
            result.body[row] = rref_temp_self.body[row][self.rows:]
        return result
