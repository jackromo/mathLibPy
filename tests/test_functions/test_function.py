from mathlibpy.functions import *
import unittest


class FunctionTester(unittest.TestCase):

    def test_abstract(self):
        self.assertRaises(Exception, Function.__init__)


class ConstantTester(unittest.TestCase):

    def setUp(self):
        self.c1 = Constant(1)
        self.c2 = Constant(2)

    def test_eq(self):
        self.assertNotEqual(self.c1, self.c2)
        self.assertEqual(self.c1, Constant(1))

    def test_call(self):
        self.assertEqual(self.c1(3), 1)
        self.assertEqual(self.c2(5), 2)

    def test_get_derivative_call(self):
        self.assertEqual(self.c1.get_derivative()(5), 0)
        self.assertEqual(self.c2.get_derivative()(3), 0)


class FunctionBinaryTreeNodeTester(unittest.TestCase):

    def test_abstract(self):
        self.assertRaises(Exception, FunctionBinaryTreeNode.__init__)


class FunctionAddNodeTester(unittest.TestCase):

    def setUp(self):
        self.add1 = FunctionAddNode(Constant(1), Constant(2))
        self.add2 = FunctionAddNode(Constant(0), Constant(-2))

    def test_eq(self):
        self.assertNotEqual(self.add1, self.add2)
        self.assertEqual(self.add1, FunctionAddNode(Constant(1), Constant(2)))

    def test_call(self):
        self.assertEqual(self.add1(1), 3)
        self.assertEqual(self.add2(1), -2)

    def test_add_call(self):
        self.assertEqual((self.add1 + self.add2)(1), self.add1(1) + self.add2(1))

    def test_get_derivative_call(self):
        self.assertEqual(self.add1.get_derivative()(1), 0)
        self.assertEqual(self.add2.get_derivative()(1), 0)


class FunctionSubNodeTester(unittest.TestCase):

    def setUp(self):
        self.sub1 = FunctionSubNode(Constant(1), Constant(2))
        self.sub2 = FunctionSubNode(Constant(0), Constant(-2))

    def test_eq(self):
        self.assertNotEqual(self.sub1, self.sub2)
        self.assertEqual(self.sub1, FunctionSubNode(Constant(1), Constant(2)))

    def test_call(self):
        self.assertEqual(self.sub1(1), -1)
        self.assertEqual(self.sub2(1), 2)

    def test_sub_call(self):
        self.assertEqual((self.sub1 - self.sub2)(1), self.sub1(1) - self.sub2(1))

    def test_get_derivative_call(self):
        self.assertEqual(self.sub1.get_derivative()(1), 0)
        self.assertEqual(self.sub2.get_derivative()(1), 0)


class FunctionMulNodeTester(unittest.TestCase):

    def setUp(self):
        self.mul1 = FunctionMulNode(Constant(1), Constant(2))
        self.mul2 = FunctionMulNode(Constant(0), Constant(-2))

    def test_eq(self):
        self.assertNotEqual(self.mul1, self.mul2)
        self.assertEqual(self.mul1, FunctionMulNode(Constant(1), Constant(2)))

    def test_call(self):
        self.assertEqual(self.mul1(1), 2)
        self.assertEqual(self.mul2(1), 0)

    def test_mul_call(self):
        self.assertEqual((self.mul1 * self.mul2)(1), self.mul1(1) * self.mul2(1))

    def test_get_derivative_call(self):
        self.assertEqual(self.mul1.get_derivative()(1), 0)
        self.assertEqual(self.mul2.get_derivative()(1), 0)


class FunctionDivNodeTester(unittest.TestCase):

    def setUp(self):
        self.div1 = FunctionDivNode(Constant(1), Constant(2))
        self.div2 = FunctionDivNode(Constant(0), Constant(-2))
        self.div3 = FunctionDivNode(Constant(3), Constant(0))

    def test_eq(self):
        self.assertNotEqual(self.div1, self.div2)
        self.assertEqual(self.div1, FunctionDivNode(Constant(1), Constant(2)))

    def test_call(self):
        self.assertEqual(self.div1(1), 0.5)
        self.assertEqual(self.div2(1), 0)
        self.assertRaises(Exception, self.div3.__call__, 1)     # Division by zero

    def test_div_call(self):
        self.assertEqual((self.div2 / self.div1)(1), self.div2(1) / self.div1(1))

    def test_get_derivative_call(self):
        self.assertEqual(self.div1.get_derivative()(1), 0)
        self.assertEqual(self.div2.get_derivative()(1), 0)


class FunctionCompNodeTester(unittest.TestCase):

    def setUp(self):
        self.comp1 = FunctionCompNode(Constant(1), Constant(2))
        self.comp2 = FunctionCompNode(Constant(0), Constant(-2))

    def test_eq(self):
        self.assertNotEqual(self.comp1, self.comp2)
        self.assertEqual(self.comp1, FunctionCompNode(Constant(1), Constant(2)))

    def test_call(self):
        self.assertEqual(self.comp1(1), 1)
        self.assertEqual(self.comp2(1), 0)

    def test_comp_call(self):
        self.assertEqual((self.comp1(self.comp2))(1), self.comp1(self.comp2(1)))

    def test_get_derivative_call(self):
        self.assertEqual(self.comp1.get_derivative()(1), 0)
        self.assertEqual(self.comp2.get_derivative()(1), 0)


if __name__ == "__main__":
    unittest.main()
