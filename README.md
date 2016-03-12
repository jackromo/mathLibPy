# MathLibPy

This is a basic math library for Python.

It's a work in progress, but if you're interested in contributing, feel free to contact me at sharrackor@gmail.com.

## License

MathLibPy is licensed under the [MIT License (MIT)](LICENSE).

## Requirements

This library uses Python 2.7x, along with Epydoc for documentation.

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
* Discrete math
    * Finite Sets
    * Infinite sets
        * Real, Integer and Natural number sets
        * Sets of disjoint ranges (real and integer ranges)
    * Union, intersect, difference
    * Cardinality, subset, proper subset and equality tests
        * Returns different infinities for different infinite sets
* Infinities
    * Comparison of different infinities and with finite numbers
    * Addition, subtraction, multiplication and division
* Irrational numbers from base values (pi, e, etc.)

## Future features

* Matrices
    * Eigenvectors and eigenvalues
    * Diagonalization
* Functions
    * Intelligent function equality test (identities)
    * Find roots and fixed points
    * Limits
    * Integration (symbolic and definite)
    * Find max and min values
    * Taylor and Maclaurin series
    * Multivariate functions
* Discrete math
    * Graphs
        * Directed and undirected
        * Test for acyclicity
        * Minimum spanning trees
        * Searches and shortest paths
        * Relation to digraph conversion and vice versa
    * Sets
        * Power sets and partitions
    * Relations
        * Produce range from domain and codomain
        * Tests for totality, function, surjectivity and injectivity
        * Composition and combination
        * Conversion from total functions on real numbers to Functions
    * Logical statements
        * Parse strings of logical statements
        * Generate truth tables
        * Generate proofs and counter examples
* Abstract algebra
    * Groups (finite)
        * Test if set is group under operator
        * Find identity and inverses of elements
        * Find subgroups
        * Test if two groups are isomorphic
    * Permutations (finite)
        * Test if function is permutation on a finite set
        * Decompose permutation into disjoint cycles
        * Find if permutation is even or odd
        * Compose permutations
        * Find order of permutation
* Number theory
    * Greatest common divisor / lowest common multiple
        * Euclid's algorithm
    * Modular arithmetic
    * Coprime and prime tests
* Sequences
    * Infinite sums
        * Tests for convergence and divergence
* Geometric shapes
    * Circles and ellipses
    * Arbitrary polygons
    * Area, perimeter
    * Solving for angles
    * Finding symmetries
* Random variables
    * Discrete and continuous
    * Expected value, variance, median and mode
    * Arithmetic on variables
* Distributions
    * Binomial, Gaussian, Chi squared, etc.
* Graphics and plotting support
    * Plotting functions
    * Drawing shapes
    * Drawing distributions
    * Drawing graphs
    * Venn diagrams of sets