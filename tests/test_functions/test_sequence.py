from mathlibpy.functions import *
import unittest


class SequenceTester(unittest.TestCase):

    def setUp(self):
        self.arith_seq = ArithmeticSequence(1, 1)
        self.geom_seq = GeometricSequence(1, 2)
        self.const_seq = FunctionSequence(Constant(1))

    def test_arith_seq_call(self):
        self.assertEqual(self.arith_seq(0), 1)
        self.assertEqual(self.arith_seq(2), 3)

    def test_geom_seq_call(self):
        self.assertEqual(self.geom_seq(0), 1)
        self.assertEqual(self.geom_seq(3), 8)

    def test_func_seq_call(self):
        self.assertEqual(self.const_seq(0), 1)
        self.assertEqual(self.const_seq(10), 1)

if __name__ == "__main__":
    unittest.main()
