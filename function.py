import abc
import numbers


class Function(object, abc.ABCMeta):
    """
    Abstract class for all functions composed of elementary cts diff'ble ones.
    Functions are composed of parse trees, with leaf nodes being elementary functions.
    The tree includes arithmetic and compositional combinations of inner functions.
    """

    @abc.abstractmethod
    def __call__(self, x):
        """
        If x is a number, take input x and return f(x).
        If x is a function, compose self with x.
        """

    @abc.abstractmethod
    def __add__(self, other):
        """Add self to another function"""

    @abc.abstractmethod
    def __sub__(self, other):
        """Subtract self from another function"""

    @abc.abstractmethod
    def __mul__(self, other):
        """Multiply self with another function"""

    @abc.abstractmethod
    def __div__(self, other):
        """Divide self with another function"""

    def compose(self, other):
        """
        Compose self with another function.
        Cannot be done differently by another function, so implemented here.
        """
        if not isinstance(other, Function):
            raise TypeError("Can only compose Function with Function")
        return FunctionCompNode(self, other)


class FunctionBinaryTreeNode(Function, abc.ABCMeta):
    """
    Abstract node of function parse tree for combination of two functions.
    Concrete subclasses are functions themselves, and can be evaluated.
    """

    def __init__(self, f1, f2):
        if not (isinstance(f1, Function) and isinstance(f2, Function)):
            raise TypeError("Both inputs must be of type Function")
        self.f1 = f1
        self.f2 = f2

    def __call__(self, x):
        if isinstance(x, numbers.Number):
            return self._evaluate(x)
        elif isinstance(x, Function):
            return self.compose(x)
        else:
            raise TypeError("Can only be called on Function or Number")

    @abc.abstractmethod
    def _evaluate(self, x):
        """
        Take a number x, and return f(x).
        Input x is guaranteed to be a Number. This method is private.
        """

    def __add__(self, other):
        if not isinstance(other, Function):
            raise TypeError("Other must be of type Function")
        return FunctionAddNode(self, other)

    def __sub__(self, other):
        if not isinstance(other, Function):
            raise TypeError("Other must be of type Function")
        return FunctionSubNode(self, other)

    def __mul__(self, other):
        if not isinstance(other, Function):
            raise TypeError("Other must be of type Function")
        return FunctionMulNode(self, other)

    def __div__(self, other):
        if not isinstance(other, Function):
            raise TypeError("Other must be of type Function")
        return FunctionDivNode(self, other)


class FunctionAddNode(FunctionBinaryTreeNode):
    """
    Node of function parse tree for addition of two functions.
    Is a function itself, and can be evaluated.
    """
    pass


class FunctionSubNode(FunctionBinaryTreeNode):
    """
    Node of function parse tree for subtraction of two functions.
    Is a function itself, and can be evaluated.
    """
    pass


class FunctionMulNode(FunctionBinaryTreeNode):
    """
    Node of function parse tree for multiplication of two functions.
    Is a function itself, and can be evaluated.
    """
    pass


class FunctionDivNode(FunctionBinaryTreeNode):
    """
    Node of function parse tree for division of two functions.
    Is a function itself, and can be evaluated.
    """
    pass


class FunctionCompNode(FunctionBinaryTreeNode):
    """
    Node of function parse tree for composition of two functions.
    Is a function itself, and can be evaluated.
    """
    pass
