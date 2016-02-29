from matrix import *
import unittest


class MatrixTester(unittest.TestCase):

    def setUp(self):
        # Generic matrices used for tests
        self.m1 = Matrix(2, 2)
        self.m2 = Matrix(2, 2, [[1, 1],
                                [2, 1]])
        self.ident = Matrix.identity(2)
        self.m3 = Matrix(3, 3, [[1, 0, 4],
                                [1, 1, 6],
                                [-3, 0, -10]])
        self.m4 = Matrix(2, 2, [[0, 1],
                                [1, 0]])

    def test_str(self):
        self.assertEquals(self.m1.__str__(), "[0 0]\n[0 0]")

    def test_eq(self):
        self.assertTrue(self.m2 == Matrix(2, 2, [[1, 1],
                                                 [2, 1]]))

    def test_neq(self):
        self.assertFalse(self.m1 == self.m2)

    def test_add(self):
        self.assertEqual(self.m1+self.m2, self.m2)

    def test_scalar_mult(self):
        self.assertEqual(self.m2*5, Matrix(2, 2, [[5, 5],
                                                  [10, 5]]))

    def test_mult_ident(self):
        self.assertEqual(self.m2*self.ident, self.m2)
        self.assertEqual(self.ident*self.m2, self.m2)

    def test_mult_col_matrix(self):
        self.assertEqual(self.m2*Matrix(2, 1, [[1],
                                               [3]]),  Matrix(2, 1, [[4],
                                                                     [5]]))

    def test_cofactor(self):
        self.assertEqual(self.m3.get_cofactor(0, 0), Matrix(2, 2, [[1, 6],
                                                                   [0, -10]]))

    def test_determinant(self):
        self.assertEqual(self.m2.get_determinant(), -1)
        self.assertEqual(self.m3.get_determinant(), 2)

    def test_invertible(self):
        self.assertFalse(self.m1.is_invertible())
        self.assertTrue(self.m2.is_invertible())
        self.assertFalse(Matrix(1, 2, [[1, 2]]).is_invertible())

    def test_get_inverse(self):
        self.assertEqual(self.m3.get_inverse(), Matrix(3, 3, [[-5, 0, -2],
                                                              [-4, 1, -1],
                                                              [1.5, 0, 0.5]]))
        self.assertEqual(self.m4.get_inverse(), self.m4)

    def test_get_echelon_form(self):
        self.assertEqual(self.m3.get_echelon_form(), Matrix(3, 3, [[1, 0, 4],
                                                                   [0, 1, 2],
                                                                   [0, 0, 2]]))

    def test_get_reduced_echelon_form(self):
        self.assertEqual(self.m3.get_reduced_echelon_form(), Matrix(3, 3, [[1, 0, 0],
                                                                           [0, 1, 0],
                                                                           [0, 0, 2]]))

    def test_get_row_reduced_echelon_form(self):
        self.assertEqual(self.m3.get_row_reduced_echelon_form(), Matrix.identity(3))

if __name__ == "__main__":
    unittest.main()
