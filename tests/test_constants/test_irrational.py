from mathlibpy.constants import *
import unittest


class IrrationalTester(unittest.TestCase):

    def setUp(self):
        self.irr1 = IrrationalNumber(1)
        self.irr2 = IrrationalNumber(2.5)

    def test_eq(self):
        self.assertEqual(self.irr1, IrrationalNumber(1))
        self.assertEqual(self.irr2, IrrationalNumber(2.5))

    def test_neq(self):
        self.assertNotEqual(self.irr1, self.irr2)
        self.assertNotEqual(self.irr1, 1)
        self.assertNotEqual(self.irr2, 2.5)

    def test_lt(self):
        self.assertLess(self.irr1, self.irr2)
        self.assertLess(self.irr1, 2)
        self.assertLess(self.irr2, 3)

    def test_gt(self):
        self.assertGreater(self.irr2, self.irr1)
        self.assertGreater(self.irr2, 1)
        self.assertGreater(self.irr1, 0)

    def test_neg(self):
        self.assertEqual(-self.irr1, IrrationalNumber(-1))
        self.assertEqual(-self.irr2, IrrationalNumber(-2.5))

    def test_add(self):
        self.assertEqual(self.irr2 + self.irr1, self.irr1 + self.irr2)
        self.assertEqual(self.irr1 + self.irr2, IrrationalNumber(3.5))
        self.assertEqual(self.irr2 + self.irr2, IrrationalNumber(5))
        self.assertEqual(self.irr1 + 1, IrrationalNumber(2))

    def test_sub(self):
        self.assertEqual(self.irr1 - self.irr2, IrrationalNumber(-1.5))
        self.assertEqual(self.irr2 - self.irr1, -(self.irr1 - self.irr2))
        self.assertEqual(self.irr1 - 1, IrrationalNumber(0))

    def test_mul(self):
        self.assertEqual(self.irr1 * self.irr1, self.irr1)
        self.assertEqual(self.irr1 * (-1), -self.irr1)
        self.assertEqual(self.irr1 * self.irr2, IrrationalNumber(2.5))
        self.assertEqual(self.irr1 * 1, self.irr1)
        self.assertEqual(self.irr1 * 3, IrrationalNumber(3))

    def test_div(self):
        self.assertEqual(self.irr1 / self.irr1, self.irr1)
        self.assertRaises(ZeroDivisionError, self.irr1.__div__, 0)
        self.assertEqual(self.irr1 / self.irr2, IrrationalNumber(1 / 2.5))
        self.assertEqual(self.irr1 / 2, IrrationalNumber(0.5))

    def test_pow(self):
        self.assertEqual(self.irr1 ** self.irr1, self.irr1)
        self.assertEqual(self.irr2 ** self.irr2, IrrationalNumber(2.5 ** 2.5))
        self.assertEqual(self.irr1 ** (-1), IrrationalNumber(1))


if __name__ == "__main__":
    unittest.main()
