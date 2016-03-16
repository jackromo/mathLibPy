"""
This is largely deprecated. Do not use it as a metric for correctness.
"""

from mathlibpy.discrete import *
import unittest


# class SetPyTester(unittest.TestCase):
#
#     def test_abstract(self):
#         self.assertRaises(Exception, SetPy.__init__)
#
#
# class SetPyTreeNodeTester(unittest.TestCase):
#
#     def test_abstract(self):
#         self.assertRaises(Exception, SetPyTreeNode.__init__)
#
#
# class FiniteSetPyTester(unittest.TestCase):
#
#     def setUp(self):
#         self.set1 = FiniteSetPy()
#         self.set2 = FiniteSetPy([1, 1, 2])
#         self.set3 = FiniteSetPy([1, 2, 3])
#
#     def test_eq(self):
#         self.assertEqual(self.set1, FiniteSetPy())
#         self.assertEqual(self.set2, FiniteSetPy([1, 2]))
#         self.assertEqual(self.set3, FiniteSetPy([1, 2, 3]))
#
#     def test_cardinality(self):
#         self.assertEqual(self.set1.cardinality(), 0)
#         self.assertEqual(self.set2.cardinality(), 2)
#         self.assertEqual(self.set3.cardinality(), 3)
#
#     def test_union(self):
#         self.assertEqual(self.set2.union(self.set1), self.set2)
#         self.assertEqual(self.set3.union(self.set2), self.set3)
#
#     def test_intersect(self):
#         self.assertEqual(self.set1.intersect(self.set2), self.set1)
#         self.assertEqual(self.set2.intersect(self.set3), self.set2)
#
#     def test_difference(self):
#         self.assertEqual(self.set3.difference(self.set2), FiniteSetPy([3]))
#         self.assertEqual(self.set2.difference(self.set3), FiniteSetPy())
#
#     def test_disjoint(self):
#         self.assertFalse(self.set2.is_disjoint(self.set3))
#         self.assertTrue(self.set1.is_disjoint(self.set2))
#
#     def test_is_subset(self):
#         self.assertFalse(self.set3.is_subset(self.set2))
#         self.assertTrue(self.set2.is_subset(self.set3))
#
#     def test_is_proper_subset(self):
#         self.assertFalse(self.set3.is_proper_subset(self.set2))
#         self.assertTrue(self.set2.is_proper_subset(self.set3))
#
#
# class SetPyUnionNodeTester(unittest.TestCase):
#
#     def setUp(self):
#         self.set1 = SetPyUnionNode(FiniteSetPy([1]), FiniteSetPy([2]))
#         self.set2 = SetPyUnionNode(FiniteSetPy([3]), FiniteSetPy([3]))
#
#     def test_contains(self):
#         self.assertTrue(1 in self.set1)
#         self.assertTrue(2 in self.set1)
#         self.assertTrue(3 in self.set2)
#
#     def test_cardinality(self):
#         self.assertEqual(self.set1.cardinality(), 2)
#         self.assertEqual(self.set2.cardinality(), 1)
#
#     def test_is_finite(self):
#         self.assertTrue(self.set1.is_finite())
#         self.assertTrue(self.set2.is_finite())
#
#     def test_elems(self):
#         self.assertTrue(all(x in self.set1 for x in self.set1.elems()))
#         self.assertEquals(self.set2.elems(), [3])
#
#     def test_eq(self):
#         self.assertEqual(self.set1, FiniteSetPy([1, 2]))
#         self.assertEqual(self.set2, FiniteSetPy([3]))
#
#     def test_subset(self):
#         self.assertTrue(self.set1.is_subset(FiniteSetPy([1, 2])))
#         self.assertFalse(self.set1.is_subset(FiniteSetPy([1])))
#
#     def test_proper_subset(self):
#         self.assertTrue(self.set1.is_proper_subset(FiniteSetPy([1, 2, 3, 4])))
#         self.assertFalse(self.set1.is_proper_subset(self.set1))
#         self.assertFalse(self.set1.is_proper_subset(FiniteSetPy()))
#
#
# class SetPyIntersectNodeTester(unittest.TestCase):
#
#     def setUp(self):
#         self.set1 = SetPyIntersectNode(FiniteSetPy([1, 2, 3]), FiniteSetPy([2, 3, 4]))
#         self.set2 = SetPyIntersectNode(FiniteSetPy([3]), FiniteSetPy([4, 3]))
#
#     def test_contains(self):
#         self.assertFalse(1 in self.set1)
#         self.assertTrue(2 in self.set1)
#         self.assertTrue(3 in self.set1)
#         self.assertTrue(3 in self.set2)
#         self.assertFalse(4 in self.set2)
#
#     def test_cardinality(self):
#         self.assertEqual(self.set1.cardinality(), 2)
#         self.assertEqual(self.set2.cardinality(), 1)
#
#     def test_is_finite(self):
#         self.assertTrue(self.set1.is_finite())
#         self.assertTrue(self.set2.is_finite())
#
#     def test_elems(self):
#         self.assertTrue(all(x in self.set1 for x in self.set1.elems()))
#         self.assertEquals(self.set2.elems(), [3])
#
#     def test_eq(self):
#         self.assertEqual(self.set1, FiniteSetPy([2, 3]))
#         self.assertEqual(self.set2, FiniteSetPy([3]))
#
#     def test_subset(self):
#         self.assertTrue(self.set1.is_subset(FiniteSetPy([1, 2, 3])))
#         self.assertTrue(self.set1.is_subset(self.set1))
#         self.assertFalse(self.set1.is_subset(FiniteSetPy([1])))
#
#     def test_proper_subset(self):
#         self.assertTrue(self.set1.is_proper_subset(FiniteSetPy([1, 2, 3])))
#         self.assertFalse(self.set1.is_proper_subset(self.set1))
#         self.assertFalse(self.set1.is_proper_subset(FiniteSetPy()))
#
#
# class SetPyDifferenceNodeTester(unittest.TestCase):
#
#     def setUp(self):
#         self.set1 = SetPyDifferenceNode(FiniteSetPy([1, 2, 3, 4]), FiniteSetPy([3, 4]))
#         self.set2 = SetPyDifferenceNode(FiniteSetPy([3]), FiniteSetPy([4]))
#
#     def test_contains(self):
#         self.assertTrue(1 in self.set1)
#         self.assertTrue(2 in self.set1)
#         self.assertFalse(4 in self.set1)
#         self.assertTrue(3 in self.set2)
#         self.assertFalse(4 in self.set2)
#
#     def test_cardinality(self):
#         self.assertEqual(self.set1.cardinality(), 2)
#         self.assertEqual(self.set2.cardinality(), 1)
#
#     def test_is_finite(self):
#         self.assertTrue(self.set1.is_finite())
#         self.assertTrue(self.set2.is_finite())
#
#     def test_elems(self):
#         self.assertTrue(all(x in self.set1 for x in self.set1.elems()))
#         self.assertEquals(self.set2.elems(), [3])
#
#     def test_eq(self):
#         self.assertEqual(self.set1, FiniteSetPy([1, 2]))
#         self.assertEqual(self.set2, FiniteSetPy([3]))
#
#     def test_subset(self):
#         self.assertTrue(self.set1.is_subset(FiniteSetPy([1, 2, 3])))
#         self.assertTrue(self.set1.is_subset(self.set1))
#         self.assertFalse(self.set1.is_subset(FiniteSetPy([1])))
#
#     def test_proper_subset(self):
#         self.assertTrue(self.set1.is_proper_subset(FiniteSetPy([1, 2, 3])))
#         self.assertFalse(self.set1.is_proper_subset(self.set1))
#         self.assertFalse(self.set1.is_proper_subset(FiniteSetPy()))
#
#
# if __name__ == "__main__":
#     unittest.main()
