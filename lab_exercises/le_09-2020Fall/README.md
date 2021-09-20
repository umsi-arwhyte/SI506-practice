# SI 506: Lab Exercise 08

## This Week's Lab

This week's lab focuses on creating classes, instantiating classes, class variables, the initialization function and other helper functions.

## 1.0 Problem 01 (5 Points)

In this problem, you will:
1. Create a constructor for the `Dog` class
2. Initialize variables

Instance Variables:

* `name` (string): Name of the Dog for the instance.
* `age` (float): Age od the Dog for the instance.

The constructor will take the following arguments:

* `self`
* `name`
* `age`

and assign each to an instance variable of the same name. In addition, the constructor should create an instance variable called `tricks` and assign its value to an empty list. We'll change that later when calling the `update_tricks()` method.

Replace the `pass` statements with the appropriate code blocks. Read the class and method Docstrings for additional implementation details.

## 2.0 Problem 02 (2.5 Points)

In this problem you will:
1. Create a method to update a class variable

Implement the `increment_age()` method of the `Dog` class by replacing the `pass` statement with the appropriate code block. Read the function Docstring for additional implementation details.

## 3.0 Problem 03 (5 Points)

In this problem you will:
1. Create a helper method
2. Use a positional argument to update class instance

Implement the `update_tricks()` method of the `Dog` class by replacing the `pass` statement with the appropriate code block. Read the function Docstring for additional implementation details.

## 4.0 Problem 04 (2.5 Points)

In this problem you will:
1. Override the `__str__()` method to represent the dog class

Implement the `__str__()` method of the `Dog` class by replacing the `pass` statement with the appropriate code block. Read the function Docstring for additional implementation details.

## 5.0 Problem 05 (5 Points)

In this problem, you will:
1. Instantiate an object
2. Update the instance's variables.

### 5.1: Create Fido

1. Set "Fido" to a variable named `name`.
2. Set "3" to a variable named `age`. Do not set it as a string.
3. Instantiate a `Dog` object with `name` and `age` and assign it to a variable named `fido`.
4. Call the `incerement_age()` method on `fido` and then call the `update_tricks()` method and pass "sit" as a keyword argument. Print `fido` to see how he has grown.

### 5.2: Create Spot

1. Instantiate another `Dog` object with "Spot" as it's name and "1" as it's age, then assign it to a variable named `spot`.
2. Call the `incerement_age()` method on `spot` 3 (three) times.\
:bulb: You can use a for loop and `range()` to help repeat functions/methods several times.
3. Call the `update_tricks()` method twice to add 2 (two) tricks of your choice to Spot's list of tricks.
4. Call the object representation of `spot` using the `__str__()` method and save it to variable called `spot_str`, then print `spot_str`.
