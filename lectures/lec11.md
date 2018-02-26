# Lecture #11: Numpy for Numerical Applications and Data Model/Interface Design

## Lecture Objectives

* create and manipulate numpy arrays for scientific/mathematical applicatinos
* use a variety of containers to design the data structures for a software project



## Textbook Reference

Chapter 9, pages 201-227

## Activiteis


1. What is numpy?
   * mostly about arrays that can be used mathematically
   * a lot of resemblance to Matlab

1. Importing numpy
   * common convention: `import numpy as np`

1. Common `ndarray` methods
   * initialization: `arange`, `zeros`, `ones`, `empty`, `linspace`, `logspace`
   * attributes (see table 9-1), esp:
     * `ndim`, `shape`, `size`
     * `dtype`
   * slicing
   * arithmetic & broadcasting
     * mathematical operations are elementwise by default
     * compatible arrays & broadcasting
     * experiment - formulate hypotheses and test

1. Structured Arrays
   * tables with named columns and varying data types
   * define the structure of a row: names and types
   * access slices by rows and column names

1. Designing data models and interfaces
   1. Many reason to break project into distinct pieces with well-defined
      interfaces
      * division of labor
      * separation of concerns
      * reviewability
   1. all components must share the same data model
      * how will data be shared among components
      * balance between flexibility and simplicity
      * depends heavily on features of language
        * object-oriented
        * advanced containers
   1. define interfaces
      * input, output, behavior
