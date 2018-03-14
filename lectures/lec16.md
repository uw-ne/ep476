# Lecture #16: Introduction to SciPy and Linear Algebra Review

## Lecture Objectives

1. Become aware of the problem solving utilities in the SciPy library
2. Identify the functions that correspond to previously seen utilites from
   other language libraries, e.g. MATLAB's `fsolve`, `ode45`, `\`-operator, etc.
3. Be able to translate mathematical summation over an index to loops
4. Be able to write a second-order difference equation as a matrix/banded-matrix
5. Be able to handle Dirichlet boundary conditions for a second-order difference equation

## Textbook Reference

## Activities

1. Tour of [SciPy library](https://docs.scipy.org/doc/scipy/reference/)
    * [Discrete Fourier transforms (scipy.fftpack)](
        https://docs.scipy.org/doc/scipy/reference/fftpack.html)
    * [Integration and ODEs (scipy.integrate)](
        https://docs.scipy.org/doc/scipy/reference/integrate.html)
    * [Linear algebra (scipy.linalg)](
        https://docs.scipy.org/doc/scipy/reference/linalg.html)
    * [Optimization and root finding (scipy.optimize)](
        https://docs.scipy.org/doc/scipy/reference/optimize.html)
    * [Special functions (scipy.special)](
        https://docs.scipy.org/doc/scipy/reference/special.html)
2. Review of basic linear algebra
    * matrix multiplication
    * Gaussian elimination
3. Turning the second order difference equation into a matrix
    * banded matrix
        * identify the structure and define the translation from a full matrix
        * [scipy.linalg.solve_banded](
            https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.solve_banded.html#scipy.linalg.solve_banded)
    * Dirichlet boundary conditions
        1. write out difference equations involving boundary nodes
        2. move known values to the right hand side
