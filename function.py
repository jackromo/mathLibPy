import abc


class Function(object, abc.ABCMeta):
    """
    Abstract class for all functions composed of elementary cts diff'ble ones.
    Functions are composed of parse trees, with leaf nodes being elementary functions.
    The tree includes arithmetic and compositional combinations of inner functions.
    """

    @abc.abstractmethod
    def __call__(cls, x):
        """
        If x is a number, take input x and return f(x).
        If x is a function, compose self with x.
        """

    @abc.abstractmethod
    def __add__(cls, other):
        """Add self to another function"""

    @abc.abstractmethod
    def __sub__(cls, other):
        """Subtract self from another function"""

    @abc.abstractmethod
    def __mul__(cls, other):
        """Multiply self with another function"""

    @abc.abstractmethod
    def __div__(cls, other):
        """Divide self with another function"""


class FunctionAddNode(Function):
    """
    Node of function parse tree for addition of two functions.
    Is a function itself, and can be evaluated.
    """
    pass


class FunctionSubNode(Function):
    """
    Node of function parse tree for subtraction of two functions.
    Is a function itself, and can be evaluated.
    """
    pass


class FunctionMulNode(Function):
    """
    Node of function parse tree for multiplication of two functions.
    Is a function itself, and can be evaluated.
    """
    pass


class FunctionDivNode(Function):
    """
    Node of function parse tree for division of two functions.
    Is a function itself, and can be evaluated.
    """
    pass


class FunctionCompNode(Function):
    """
    Node of function parse tree for composition of two functions.
    Is a function itself, and can be evaluated.
    """
    pass
