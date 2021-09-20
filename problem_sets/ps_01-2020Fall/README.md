# SI 506: Problem Set 01

## This week's Problem Set

This Problem Set focuses on using comments, values and types, variables, built-in functions
(`print()`, `len()`, `type()`, etc.) and performing basic arithmetic operations using Python.

## Background

The programming language Python was originially released in 1991 and was created by Guido van Rossum.
The language emphasizes code readability and maintainability. Python is open source with programmers
from all over the world working to maintain and develop the language further.

## 1.0 Problem 01 (20 points)

1. Uncomment the given statements that are valid variable assignment statments.

   :bulb: "Uncomment" means remove the leading has (`#`) symbol from a line of code.

2. Create a list named `valid_variables` and add all valid variables that you uncommented
   to the list.

:warning: Do not include the name of the variable in quotes, we want to display the contents of the
variables.

## 2.0 Problem 02 (20 points)

1. Use the built-in `type()` function to return the data type for each of the following variables:
    `name`, `python_foundation_officers` and `zen_of_python`. Assign the values returned in three
    new variables named: `name_type`, `officers_type` and `zen_type`.

2. Use the `print()` function to print `name_type`, `officers_type` and `zen_type`.

3. Calculate the number of characters in the `zen_of_python` multiline string using `len()` and
   assign the value to a variable named `num_chars_zen`.

## 3.0 Problem 03 (20 points)

1. Use the string method `str.split()` to split the multiline string `zen_of_python` into a list of
   words (split on the white space). Then use the built-in function `len()` to count the number of
   words in the list you create. Assign the value to the variable `num_words`.

2. Calculate the average number of words _per line_ in the multiline string `zen_of_python` and save
   it to a variable named `avg_words`.

:bulb: There are 19 lines in the multiline string `zen_of_python`; use this fact to calculate the
average number of words per line.

## 4.0 Problem 04 (20 points)

The Zen of Python is a collection of 19 "guiding principles" for writing computer programs that
influence the design of the Python programming language. Software engineer Tim Peters wrote this
set of principles and posted it on the Python mailing list in 1999. Peters's list left open a
20th principle "for Guido to fill in", referring to Guido van Rossum, the original author of the
Python language. The vacancy for a 20th principle has not been filled.

Calculate the number of words in the multiline string `zen_of_python` if Guido van Rossum were to
add a 20th principle. Assume a single new line with a length equal to the value you assigned
previously to `avg_words`. Save the return value to `total_words`.

:warning: You must use the values assigned to `num_words` and `avg_words` to complete this
calculation or the autograder test for this problem will fail.

## 5.0 Problem 05 (20 points)

1. Calculate the number of characters in the `zen_of_python` multiline string using `len()` and
   assign the value to a variable named `num_chars_zen`.

2. Calculate the average number of characters per word in the multiline string `zen_of_python` using
   floor division (i.e., the `//` operator). Leverage the values assigned to `num_chars_zen` and
   `num_words`. Assign the return value to `avg_chars`.

:warning: You must use the values assigned to `num_chars_zen` and `num_words` or the autograder
test for this problem will fail.
