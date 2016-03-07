from mathlibpy.constants import *
import unittest


class InfinityTester(unittest.TestCase):

    def setUp(self):
        self.inf1 = Infinity(1, 0)
        self.inf2 = Infinity(-1, 0)
        self.inf3 = Infinity(1, 1)

    def test_eq(self):
        self.assertEqual(self.inf1, Infinity(1, 0))
        self.assertEqual(self.inf3, Infinity(1, 1))
        self.assertNotEqual(self.inf1, self.inf2)

    def test_lt(self):
        self.assertLess(self.inf2, self.inf1)
        self.assertFalse(self.inf2 < self.inf3)
        self.assertLess(0, self.inf1)
        self.assertLess(self.inf2, 0)

    def test_gt(self):
        self.assertGreater(self.inf1, self.inf2)
        self.assertFalse(self.inf3 > self.inf2)
        self.assertGreater(self.inf1, 0)
        self.assertGreater(0, self.inf2)

    def test_add_to_inf(self):
        self.assertEqual(self.inf1 + self.inf1, self.inf1)
        self.assertEqual(self.inf2 + self.inf1, self.inf1)

    def test_add_to_finite(self):
        self.assertEqual(self.inf1 + 0, self.inf1)
        self.assertEqual(self.inf2 + 4, self.inf2)

    def test_sub_to_inf(self):
        self.assertEqual(self.inf1 - self.inf1, self.inf1)
        self.assertEqual(self.inf2 - self.inf1, self.inf2)

    def test_sub_to_finite(self):
        self.assertEqual(self.inf1 - 0, self.inf1)
        self.assertEqual(self.inf2 - 3, self.inf2)

    def test_neg(self):
        self.assertEqual(-self.inf1, Infinity(-1, 0))
        self.assertEqual(-self.inf2, self.inf1)

    def test_mul_to_inf(self):
        self.assertEqual(self.inf1 * self.inf1, self.inf1)
        self.assertEqual(self.inf2 * self.inf1, self.inf2)

    def test_mul_to_finite(self):
        self.assertEqual(self.inf1 * 1, self.inf1)
        self.assertEqual(self.inf1 * (-1), -self.inf1)

    def test_div_by_inf(self):
        self.assertEqual(self.inf1 / self.inf1, self.inf1)
        self.assertEqual(self.inf2 / self.inf1, self.inf2)

    def test_div_by_finite(self):
        self.assertEqual(self.inf1 / 2, self.inf1)
        self.assertRaises(ZeroDivisionError, self.inf1.__div__, 0)


if __name__ == "__main__":
    unittest.main()
