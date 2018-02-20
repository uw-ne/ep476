# Introduction to Python

## Learning Objectives

* intepreter
* variable names
* special variables (True, False, None, NotImplemented)
* magic numbers
* string indexing 
* modules (e.g. import math)

## Textbook

Chapter 2, pgs 39-65

## Activities

1. install python
   * why Anaconda?
   * run the Anaconda installation script: `~wilsonp/Anaconda3-5.1.0-Linux-x86_64.sh`
   * select the default location, it should be `$HOME/anaconda3`

1. Project Planning - revisited
   * stages of development
     * identify milestones that incrementally increase the scope and complexity
     * e.g. if the ultimate problem is a non-linear 3-D problem, consider
       starting with a 1-D linear approximation and gradually adding
       dimensionality and the non-linear components
     * this allows reaching "working" versions at each milestone and possibly
       easier testing

1. start ipython
   * standard python REPL
   * the iPython environment
   * Jupyter notebooks
   * two windows with editor

1. comments
   * hashtag anywhere in line
   * start with liberal use of comments
   * good choices of variable names and data structure can reduce need for comments
   * document why and not what

1. variable names
   * variable assignment
   * types
   * choosing variable names
   * special variables
   * operators
   * strings
     * inndexing: zero
     * slicing: start:end:step, negative indices, empty entries
     * string math: concat, multiply
     * builtin functions - len(), upper, isdigit, strip, format

1. magic "numbers"
   * any quantity that has semantic meaning should be assigned to a variable
     that expresses that meaning
     1. provides meaning
     1. frequently used in multiple places and allows single change for consistency
     
1. importing modules
   * functionality available in modular units
   * import math
     * try cos() first
   * different imports:
     * import math  -> math.cos()
     * from math import cos()  -> cos()
       * from math import *
     * import math as m -> m.cos()
   * important modules: os, sys, math, argparse
     * finding help
