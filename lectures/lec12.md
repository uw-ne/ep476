# Lecture #12: Control flow and Modularity

## Lecture Objectives

1. Identify when loops should be used to avoid manual repitition
2. Select the best loop type for a given situation
3. Implement a clear usage of loop variables and loop conditions
4. Construct clear and concise conditional expressions
5. Use comprehensions for simpler and readable code
6. Invoke exceptions for error handling
7. Write a function that returns one or more variables

## Textbook Reference

Chatper 4, pages 77-93
Chapter 5, pages 95-98

## Activities

1. Loops - Don't repeat yourself (115)
   * basic syntax: while vs for
     * when to use each one
       * for: "counting" up to fixed length known a priori
       * while: arbitrary condition, unknown length, possibly not "counting"
   * for loop patterns:
     * basic: item in list
     * counting: index in range(N)
     * counting with list: (index, item) in enumerate(list)
     * working with parallel list: (item1, item2) in zip(list1, list2)
   * while loop patterns:
     a. initialize condition
     b. while condition
     c. do things including possibly changing condition
   * keeping track of variables inside and outside loops

1. Comprehensions (120)
   * ideal when building a new container by looping through an existing one
   * A = transform(B)

1. Conditionals (107)
   * basic syntax - note indentation!
   * special operators: `in`, `not in`, `is`, `is not`
   * conditional expressions
   * compound conditions & operator precedence

1. Comprehensions revisited (122)
   * A = filter(B)

1. Exceptions (112)
   * error handling
   * a way to communicate errors without passing around error codes
   * not a substitute for full implementation
   * basic syntax: try ... except (e.g. error msg)
   * catching specific exceptions
   * raising exceptions

1. Functions (126)
   * syntax
   * scope

