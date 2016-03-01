from mathlibpy.functions import *
import unittest


class SequenceTester(unittest.TestCase):

    def test_abstract(self):
        self.assertRaises(Exception, Sequence.__init__)


class ArithmeticSequenceTester(unittest.TestCase):

    def setUp(self):
        self.arith_seq = ArithmeticSequence(1, 1)

    def test_eq(self):
        self.assertEqual(self.arith_seq, ArithmeticSequence(1, 1))

    def test_call(self):
        self.assertEqual(self.arith_seq(0), 1)
        self.assertEqual(self.arith_seq(2), 3)


class GeometricSequenceTester(unittest.TestCase):

    def setUp(self):
        self.geom_seq = GeometricSequence(1, 2)

    def test_eq(self):
        self.assertEqual(self.geom_seq, GeometricSequence(1, 2))

    def test_call(self):
        self.assertEqual(self.geom_seq(0), 1)
        self.assertEqual(self.geom_seq(3), 8)


class FunctionSequenceTester(unittest.TestCase):

    def setUp(self):
        self.const_seq = FunctionSequence(Constant(1))

    def test_func_seq_eq(self):
        self.assertEqual(self.const_seq, FunctionSequence(Constant(1)))

    def test_func_seq_call(self):
        self.assertEqual(self.const_seq(0), 1)
        self.assertEqual(self.const_seq(10), 1)


if __name__ == "__main__":
    unittest.main()
