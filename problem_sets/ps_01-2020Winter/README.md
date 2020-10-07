# SI 506: Problem Set 01

## This Week's Problem Set

This week's problem set focuses on practicing the use of variables, strings, string operators, mathematical expressions, and lists.

## Background

The programming language Python was originially released in 1991 and was created by Guido van Rossum. The language emphasizes code readability and maintainability. Python is open source with programmers from all over the world working to maintain and develop the language further.

## 1.0 Problem 01 (10 Points)

Guido van Rossum is the original author of Python and former Benevolent dictator for life (BDFL) of the project.

1. Uncomment the variable name and assigned value that adheres to the Python style guide. (See https://www.python.org/dev/peps/pep-0008/#function-and-variable-names)

:bulb: Uncomment means removing the hash symbol ('#') and any leading whitespace in front of the variable name.\
:warning: Choose wisely or you will trigger a syntax error.

2. Use list indexing of the `languages` list to assign the language that Guido von Rossum authored to the variable `guido_language`.

## 2.0 Problem 02 (10 Points)

Use the appropriate string operation to concatenate Guido's current position at the Python Software Foundation (see https://www.python.org/psf/members/#officers) to the value assigned to the variable you chose in Problem 1.1. Assign the concatenated value to the variable `python_foundation_officer`.

Adopt the following format for the new string: "name, President"

## 3.0 Problem 03 (20 Points)

### 3.1 SETUP

The Zen of Python, by Tim Peters (1999)

```python
zen_of_python = """
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
```

### 3.1 Problem

Count the number of characters in the string assigned to the variable `zen_of_python` and assign the value to the variable `num_chars`.

## 4.0 Problem 04 (20 Points)

Count the number of "words" separated by whitespace in the string assigned to the variable `zen_of_python` and assign the value to the variable `num_char_chunks`.

:exclamation: "Words" is used figuratively since not all the character chunks you will encounter are actually words.

## 5.0 Problem 05 (20 Points)

Use floor division to divide `num_char_chunks` by the number of lines in the Zen of Python. Return an integer rather than a floating point value and assign the value to the variable `avg_num_chunks_per_line`.

:bulb: Use `str.splitlines()` to help determine your answer.

## 6.0 Problem 06 (20 Points)

Substitute your U-M email address for all occurrences of the word "Dutch" using the appropriate built-in function in the `zen_of_python` string. Assign the modified Zen of Python string to the variable `zen_of_python_uniqname`.
