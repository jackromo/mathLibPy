from mathlibpy.discrete import *
import unittest


class SetPyTester(unittest.TestCase):

    def test_abstract(self):
        self.assertRaises(Exception, SetPy.__init__)


class FiniteSetPyTester(unittest.TestCase):

    def setUp(self):
        self.set1 = FiniteSetPy()
        self.set2 = FiniteSetPy([1, 1, 2])
        self.set3 = FiniteSetPy([1, 2, 3])

    def test_eq(self):
        self.assertEqual(self.set1, FiniteSetPy())
        self.assertEqual(self.set2, FiniteSetPy([1, 2]))
        self.assertEqual(self.set3, FiniteSetPy([1, 2, 3]))

    def test_cardinality(self):
        self.assertEqual(self.set1.cardinality(), 0)
        self.assertEqual(self.set2.cardinality(), 2)
        self.assertEqual(self.set3.cardinality(), 3)

    def test_union(self):
        self.assertEqual(self.set2.union(self.set1), self.set2)
        self.assertEqual(self.set3.union(self.set2), self.set3)

    def test_intersect(self):
        self.assertEqual(self.set1.intersect(self.set2), self.set1)
        self.assertEqual(self.set2.intersect(self.set3), self.set2)

    def test_difference(self):
        self.assertEqual(self.set3.difference(self.set2), FiniteSetPy([3]))
        self.assertEqual(self.set2.difference(self.set3), FiniteSetPy())

    def test_disjoint(self):
        self.assertFalse(self.set2.is_disjoint(self.set3))
        self.assertTrue(self.set1.is_disjoint(self.set2))

    def test_is_subset(self):
        self.assertFalse(self.set3.is_subset(self.set2))
        self.assertTrue(self.set2.is_subset(self.set3))

    def test_is_proper_subset(self):
        self.assertFalse(self.set3.is_proper_subset(self.set2))
        self.assertTrue(self.set2.is_proper_subset(self.set3))


if __name__ == "__main__":
    unittest.main()
