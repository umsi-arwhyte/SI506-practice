# SI 506: Problem Set 02

## This Week's Lab Exercise

This week's problem set includes five (5) problems that work with functions, parameters, exceptions,
 and conditionals. You will construct three (3) functions from scratch, debug a function, and
 practice calling functions.

## 1.0 Problem 01 (20 points)

Implement the `addition()` function by replacing the `pass` statement with the appropriate code
block. Read the function docstring for additional implementation details.

:bulb: Don't forget to fill out the function arguments.

When you are finished with the `addition()` function, uncomment the `print()` statement to see if it
works. It should return 15.

## 2.0 Problem 02 (20 points)

First, analyze the `filter()` function and look at its docstring, arguments, and code body. Then,
uncomment the `print()` statements below the function one at a time.

The first `print()` statement will throw an exception. The second `print()` statement will fail
silently (in other words, the code will work, but not produce the desired output). Fix both errors
by modifying the code in the `filter()` function.

The first test should return as too long, and the second should return the initial string.

:warning: Do not modify any of the `print()` statements.

## 3.0 Problem 03 (20 points)

Implement the `umich_email_detection()` function by replacing `pass` statement with appropriate
code block. Read the function docstring for additional implementation details.

Test your code by uncommenting the two `print()` statements.

:bulb: You will need to use a conditional statement.

:bulb: Use a string method to identify which strings end with "@umich.edu". A list of string methods
is available [here](https://www.w3schools.com/python/python_ref_string.asp).

## 4.0 Problem 04 (20 points)

Put together what you've learned so far by writing a function from scratch that fulfills the
following specifications:

```python
"""
Function name: count_words_or_lines

Parameters:
    string (str): A string that will be operated upon.
    operation (str): Accepts either 'lines' or 'words'. Should have a default value of 'words'.

Returns:
    int: The number of lines or words in <string>, depending on the choice of operation.

Explanation:
    You should use conditionals to determine what is returned by this function:

    If <operation> is 'words', return the number of words in <string>.
    If <operation> is 'lines', return the number of lines in <string>.
    If <operation> is neither, return 'Choose a correct operation'.
"""
```

## 5.0 Problem 05 (20 points)

### 5.1 SET UP

You will work with the University of Michigan mission statement for Problem 5. The `mission`
variable contains the mission statement string.

```python
mission = """The mission of the University of Michigan is to serve the people of Michigan
and the world through preeminence in creating, communicating, preserving and
applying knowledge, art, and academic values, and in developing leaders and
citizens who will challenge the present and enrich the future."""
```

### 5.2 Problem

Using your `count_words_or_lines()` function, determine the number of words and lines in the
University of Michigan mission statement (provided below) and assign those numbers to `num_words`
and `num_lines`, respectively (replace '-999'). Also, determine the number of characters in
`mission` and assign it to `num_chars`.