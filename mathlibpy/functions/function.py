"""
.. module:: function
    :synopsis: Function class and all FunctionBinaryTreeNode subclasses.

.. moduleauthor:: Jack Romo <sharrackor@gmail.com>
"""


import abc
import numbers


class Function(object):
    """
    Abstract class for all functions composed of elementary continuous differentiable ones.
    """

    __metaclass__ = abc.ABCMeta

    def __call__(self, x):
        """
        :type x: Function, Number
        :param x: Either number from domain fed into self, or function to compose with self.
        :rtype: Function if x is Function, Number otherwise
        :return: Self composed with x if x is Function, self applied to x if x is Number
        """
        if isinstance(x, numbers.Number):
            return self._evaluate(x)
        elif isinstance(x, Function):
            return FunctionCompNode(self, x)
        else:
            raise TypeError("Can only be called on Function or Number")

    @abc.abstractmethod
    def _evaluate(self, x):
        """
        Take a number x, and return f(x).
        Input x is guaranteed to be a Number.

        @type x: Number
        @param x: Value to be mapped by self to result.
        """

    def __add__(self, other):
        """
        :type other: Function
        :param other: A Function to be combined with self by addition.
        :rtype: Function
        :return: Self combined with another Function by addition.
        """
        if not isinstance(other, Function):
            raise TypeError("Other must be of type Function")
        return FunctionAddNode(self, other)

    def __sub__(self, other):
        """
        :type other: Function
        :param other: A Function to be combined with self by subtraction.
        :rtype: Function
        :return: Self combined with another Function by subtraction.
        """
        if not isinstance(other, Function):
            raise TypeError("Other must be of type Function")
        return FunctionSubNode(self, other)

    def __mul__(self, other):
        """
        :type other: Function
        :param other: A Function to be combined with self by multiplication.
        :rtype: Function
        :return: Self combined with another Function by multiplication.
        """
        if not isinstance(other, Function):
            raise TypeError("Other must be of type Function")
        return FunctionMulNode(self, other)

    def __div__(self, other):
        """
        :type other: Function
        :param other: A Function to be combined with self by division.
        :rtype: Function
        :return: Self combined with another Function by division.
        """
        if not isinstance(other, Function):
            raise TypeError("Other must be of type Function")
        return FunctionDivNode(self, other)

    @abc.abstractmethod
    def __eq__(self, other):
        """
        .. note ::

            Currently checks for exact equivalences between functions. Requires intelligent search for identities.
        """

    @abc.abstractmethod
    def get_derivative(self):
        """
        Return own derivative as a function.

        :rtype: Function
        :return: A function that, for input x, gets own gradient at (x, f(x)).
        """


class FunctionBinaryTreeNode(Function):
    """
    Abstract node of function parse tree for combination of two functions.
    Concrete subclasses are functions themselves, and can be evaluated, derived, etc.
    """

    __metaclass__ = abc.ABCMeta

    def __init__(self, f1, f2):
        if not (isinstance(f1, Function) and isinstance(f2, Function)):
            raise TypeError("Both inputs must be of type Function")
        self.f1 = f1
        self.f2 = f2

    def __eq__(self, other):
        if not isinstance(other, FunctionBinaryTreeNode):
            return False
        return (self.f1 == other.f1) and (self.f2 == other.f2)


class FunctionAddNode(FunctionBinaryTreeNode):
    """
    Node of function parse tree for addition of two functions.
    Is a function itself, and can be evaluated.
    """

    def _evaluate(self, x):
        return self.f1(x) + self.f2(x)

    def get_derivative(self):
        return self.f1.get_derivative() + self.f2.get_derivative()


class FunctionSubNode(FunctionBinaryTreeNode):
    """
    Node of function parse tree for subtraction of two functions.
    Is a function itself, and can be evaluated.
    """

    def _evaluate(self, x):
        return self.f1(x) - self.f2(x)

    def get_derivative(self):
        return self.f1.get_derivative() - self.f2.get_derivative()


class FunctionMulNode(FunctionBinaryTreeNode):
    """
    Node of function parse tree for multiplication of two functions.
    Is a function itself, and can be evaluated.
    """

    def _evaluate(self, x):
        return self.f1(x) * self.f2(x)

    def get_derivative(self):
        # Use product rule
        u = self.f1
        v = self.f2
        du = self.f1.get_derivative()
        dv = self.f2.get_derivative()
        return (du * v) + (u * dv)


class FunctionDivNode(FunctionBinaryTreeNode):
    """
    Node of function parse tree for division of two functions.
    Is a function itself, and can be evaluated.
    """

    def _evaluate(self, x):
        if self.f2(x) == 0:
            raise Exception("Division by Zero detected")
        else:
            return self.f1(x) / float(self.f2(x))

    def get_derivative(self):
        # Use quotient rule
        u = self.f1
        v = self.f2
        du = self.f1.get_derivative()
        dv = self.f2.get_derivative()
        return ((du * v) - (u * dv)) / (v * v)


class FunctionCompNode(FunctionBinaryTreeNode):
    """
    Node of function parse tree for composition of two functions.
    Is a function itself, and can be evaluated.
    """

    def _evaluate(self, x):
        return self.f1(self.f2(x))

    def get_derivative(self):
        return self.f2.get_derivative() * FunctionCompNode(self.f1.get_derivative(), self.f2)


class Constant(Function):
    """
    A constant value, ie. f(x) = c.
    Used for containing constant values in function tree.
    """

    def __init__(self, val):
        self.val = val

    def _evaluate(self, x):
        return self.val

    def get_derivative(self):
        return Constant(0)

    def __eq__(self, other):
        if not isinstance(other, Constant):
            return False
        return self.val == other.val
