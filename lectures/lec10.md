# Introduction to Python

## Learning Objectives

* describe which containers are mutable and which are immutable
* use methods from eacch container type to efficiently manipulate a list
* identify a specific use case for each container type
* use a variety of containers to design the data structures for a software project

## Textbook

Chapter 3, pages 65-75

## Activities

1. mutability

1. duck typing

1. containers - iterable

1. lists
   * notation
   * indexing & slicing like strings
     * slicing on LHS of assignment
     * del slivce
   * list operators:
     * NOT mathematical arrays
   * list methods:
     * append, count, insert, remove, clear,
       extend, reverse, index, pop, sort
   * testing
     * devise a way to test each function
   * reference counting
   * use cases
     * order matters
     * mutable
 
1. tuples - imutable lists
   * notation
   * imutable struture
     * may have mutable members
   * what methods exist?
   * test how lists are different from tuples
   * use cases
     * order matters
     * immutable

1. sets - unordered lists with max one of each thing
   * notation
   * items in set must be immutable
   * test addition of things to sets vs lists
   * test methods:
     * difference vs difference_update vs symmetric_difference
   * use cases
     * collect unique list of things

1. dictionaries - powerful container type
   * notation
   * keys must be immutable
   * values can be anything - including other containers
   * explore methods
       * use what you've learned to hypothesis how they work and test those
       hypotheses

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



x
