Homework #3
===========

EP476: Introduction to Scientific Computing for Engineering Physics
-------------------------------------------------------------------

**Due: Tuesday, April 12, 1:00 PM**

This assignment will have you read some data from a file and into data
structures in memory.  Two related but slightly different data files will be
used.

**PROBLEM 1** Start a new repository for this assignment.  Copy and paste the
text of this page into a README file for this repo, commit that file to the
`master` branch and push it to the github repository.

Element Library
~~~~~~~~~~~~~~~

The first file is a list of natural abundances for each element.  A sample
file is provided `here
<https://raw.githubusercontent.com/gonuke/ep476/master/hw/elelib.std>`_.  The
simple format has one block for each element, in which the first line of each
block contains:

* the chemical symbol
* the molar mass (g/mol)
* the atomic number
* the density at standard temperature and pressure (g/cc)
* the number of naturally occurring isotopes that make up that element

The rest of the block has one line per isotope, with each line containing:

* the mass number of the isotope
* the atomic abundance

**PROBLEM 2** Create a branch from the `master` branch called `elelib_basic`.

**PROBLEM 3** Write a module that provides functions to read an element
library into a single data structure.  Assume that there will be no blank
lines or comments.  This module should include:

* one function to parse the first line each block
* one function to parse a single isotope abundance line in a block
* one function to open the file and loop over the lines, calling the other functions

You should also write nose tests for each of the first two functions.

**PROBLEM 4** Commit any necessary files to the repository and push this
branch to github.  Do not merge this into the `master` branch.


Material Library
~~~~~~~~~~~~~~~~~

This file is a list of engineering materials.  A sample file is provided `here
<https://raw.githubusercontent.com/gonuke/ep476/master/hw/matlib.sample>`_. The
simple format has one block for each material, in which the first line of each
block contains:

* the name of the material
* the density at standard temperature and pressure (g/cc)
* the number of elements that make up the material

The rest of the block has one line per element, with each line containing:

* the chemcial symbol
* the mass fraction of that element
* the atomic number of the element

**PROBLEM 5** Create a branch from the `elelib_basic` branch called `matlib_basic`.

**PROBLEM 6** Write a module that provides functions to read a material
library into a single data structure.  Assume that there will be no blank
lines or comments.  This module should include:

* one function to parse the first line each block
* one function to parse a single element mass fraction line in a block
* one function to open the file and loop over the lines, calling the other functions

You should also write nose tests for each of the first two functions.

**PROBLEM 7** Commit any necessary files to the repository and push this
branch to github.  Do not merge this into the `master` branch.

Comments
~~~~~~~~

It is convenient to be able to add comments to these files, but it will make
it more complicated to read them.

**PROBLEM 8** Create a branch from the `matlib_basic` branch called `comments`.

**PROBLEM 9** Add the ability to recognize and ignore comments and blank lines
at any point in the element library or material library files.  You may want
to create a module of utility functions that you can use in both of the
previous modules to help.

Make your own simple element library and material library that includes the
different conditions you would like to handle and write tests that confirm
that your code works correctly.

**PROBLEM 10** Commit any necessary files, including the simple library files
you have generated, and push this branch to github.  Do not merge this into
any other branches.

Expanding the Material Composition to a List of Nuclides
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is often useful to represent a material composition in terms of its nuclide
abundances rather than its elemental mass fractions.

**PROBLEM 11** Create a branch from the `comments` branch called `expand_isos`.

**PROBLEM 12** Write a function that will take a single material as input and
use the element library to generate a list of all the nuclides in that
material and their isotopic abundances.

For nuclide, i, the atom density, N [mol/cc], can be determined by:

N_i = rho * w/o * a/o  /  MM

where:

* rho is the mass density of the material
* w/o is the mass fraction of the element in that material
* a/o is the atom fraction of the isotope in that element
* MM is the molar mass of that elemtn

To convert to the isotopic abundance of that nuclide, simply divide by the
total atom density, summing over all the nuclides.

Your function should take a material data structure as input and return a
single container that indicates the identity of each nuclide (Z & A) and its
atomic abundance.

**PROBLEM 13** Commit any necessary files, including testing files, and push
this branch to github. Do not merge this into any other branches.
