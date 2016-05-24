# MathLibPy

This is a math library for Python.

It's a work in progress, but if you're interested in contributing, feel free to contact me at sharrackor@gmail.com.

## License

MathLibPy is licensed under the [MIT License (MIT)](LICENSE).

## Requirements

This library uses Python 2.7x, along with Sphinx and reStructuredText for documentation.

## Documentation

The documentation can be built into HTML. To do this, enter the 'docs' folder and type

```bash
make html
```

in the command prompt. After this, open up 'index.html' in 'docs/_build' in your browser.

## Installation

To install mathLibPy, clone the repository, navigate to the project's root directory and enter

```bash
python setup.py install
```

into the command prompt. Please ensure that python is on your PATH before doing this.

## Features

* Matrices
    * Arithmetic on matrices
    * Determinants and cofactors
    * Inverses (can handle zeros on main diagonal)
    * Echelon and (row) reduced Echelon form
* Functions
    * Polynomials
    * Trigonometric functions
    * Exponential function, logarithm
        * Arbitrary powers and logarithm bases
    * Function combination and composition (addition, division, etc.)
    * Differentiation
    * Exact function equality test (equal if internal structures equal)
* Sequences
    * Arithmetic and Geometric sequences
    * Generic sequence, takes any Function
* Sets (UNFINISHED)
    * Finite Sets
    * Union, intersect, difference
    * Universe sets for different types (eg. universe of all numbers)
    * Interval sets within ordered universe sets
    * Cardinality, subset, proper subset and equality tests
        * Returns different infinities for different infinite sets
* Infinities
    * Comparison of different infinities and with finite numbers
    * Addition, subtraction, multiplication and division
* Irrational numbers from base values (pi, e, etc.)
