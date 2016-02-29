from polynomial import *
from function import FunctionAddNode
import unittest


class PolynomialTester(unittest.TestCase):

    def setUp(self):
        self.p1 = Polynomial([1])        # p = 1
        self.p2 = Polynomial([2, 3, 4])  # p = 2 + 3x + 4x^2
        self.p3 = Polynomial([2, 3, 4, 0, 0])

    def test_degree(self):
        self.assertEqual(self.p1.degree, 0)
        self.assertEqual(self.p2.degree, 2)
        self.assertEqual(self.p3.degree, 2)

    def test_coeffs(self):
        self.assertEqual(self.p2.coeffs, [2, 3, 4])
        self.assertEqual(self.p3.coeffs, [2, 3, 4])

    def test_str(self):
        self.assertEqual(self.p2.__str__(), "2 + 3x^1 + 4x^2")

    def test_neq(self):
        self.assertNotEqual(self.p1, self.p2)

    def test_eq(self):
        self.assertEqual(self.p2, Polynomial([2, 3, 4]))
        self.assertEqual(self.p2, self.p3)

    def test_getitem(self):
        self.assertEqual(self.p1[0], 1)
        self.assertEqual(self.p2[10], 0)

    def test_setitem(self):
        self.p3[1] = 2
        self.p3[10] = 10
        self.assertEqual(self.p3[1], 2)
        self.assertEqual(self.p3[10], 10)
        self.assertEqual(self.p3.degree, 10)

    def test_call(self):
        self.assertEqual(self.p1(0), 1)
        self.assertEqual(self.p2(1), 9)

    def test_add(self):
        self.assertTrue(isinstance(self.p1 + self.p1, FunctionAddNode))

    def test_add_call(self):
        self.assertEqual((self.p1+self.p2)(1), 10)

    def test_sub_call(self):
        self.assertEqual((self.p1-self.p2)(1), -8)

    def test_mul_call(self):
        self.assertEqual((self.p1*self.p2)(1), 9)

    def test_div_call(self):
        self.assertEqual((self.p1/self.p2)(1), 1 / 9)

    def test_compose_call(self):
        self.assertEqual(self.p1(self.p2)(1), 1)
        self.assertEqual(self.p2(self.p1)(2), 9)

    def test_get_derivative(self):
        self.assertEqual(self.p2.get_derivative(), Polynomial([3, 8]))

    def test_get_derivative_call(self):
        self.assertEqual(self.p2.get_derivative()(1), 11)
        self.assertEqual(self.p1.get_derivative()(1), 0)

if __name__ == "__main__":
    unittest.main()
