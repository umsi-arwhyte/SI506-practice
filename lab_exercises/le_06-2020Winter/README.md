# SI 506: Lab Exercise 06

## This Week's Lab

This week's lab is midterm practice! It will focus on a new data construct, tuples, and implementing a quick function. You will complete two exercises involving tuples so that you can become familiar with how they work, and why they are so important to Python. You will also get to implement a function on your own and call it. This will be a timed activity in the lab to familiarize you with the format of the midterm.

## PART 1: Midterm Practice

The following two problems are to familiarize you with the format of the midterm. You will be asked to create a simple function and call it. This portion of the lab exercise will be timed. Please follow the intructions from your instructor.

### 1.0 Problem 01 (5 Points)

In this problem you will implement a simple function that:
1. Has two arguments: one is a default
2. Uses a local variable
3. Iterates through a list
4. Appends to a list
5. Returns a value

Implement the `calculate_exponent()` function by replacing the `pass` statement with the appropriate code block. Read the function Docstring for additional implementation details.

:bulb: You can use the exponent operator (\*\*) syntax: x\*\*y to find x to the power of y

### 2.0 Problem 02 (5 Points)

In this problem you will:
1. Call a function
2. Pass positional and keyword arguments
3. Work with lists

#### 2.1 SETUP

```python
# We provide you with a list of integers and two empty lists to start the problem

ints = [2, 4, 6, 8]

exponents_1 = []
exponents_2 = []
```

#### 2.2 Problem

1. Call the `calculate_exponent()` function that you created in problem 1 and pass `ints` as a positional argument. Store the results in `exponents_1`.
2. Call the `calculate_exponent()` fumction again and pass `ints` as a keyword argument and 3 (three) as a keyword argument. Store the results in `exponents_2`.

## PART 2: TUPLES

The following 2 problems will introduce you to working with tuples.

:exclamation: Print statements have been provided to debug your code.

### 3.0 Problem 03 (5 Points)

In this problem you will:
1. Work with tuples
2. Differentiate between tuples and lists
3. Update tuples

#### 3.1 Background

Turns out we forgot to include 'hershey milk chocolate' and  'kisses'. Unlike lists, tuples are immutable and cannot be changed or appended once they are initialized. Using tuples instead of lists can give the programmer a hint that data should not be changed. However, we are able to take existing tuples and add them to create a new tuple.

#### 3.2 SETUP

```python
# < nut_free_candy > is a tuple of nut free candies

nut_free_candy = ('skittles', 'jolly rancher', 'twizzler', 'york')
```

#### 3.3 Problem

Create a new tuple called `extra_candy` and initialize it with 'hershey milk chocolate' and  'kisses'.
Concatenate the two candy tuples by `nut_free_candy` + `extra_candy` and assign it to `updated_nut_free_candy`.

### 4.0 Problem 04 (5 Points)

In this problem, you will:
1. Use a tuple as a key in dictionaries
2. Work with dictionaries

Lists and tuples have a lot of similar features except tuples are immutable and they use parentheses instead of brackets. Because of the immutable nature, tuples can also be used as keys in dictionaries.

Create a dictionary named `candy_dict`, this dictionary will have only one key-value pair. Assign `updated_nut_free_candy` as the key and 'nut-free' as the value.

:bulb: follow this syntax `< dict > = {< key > : < value >}`
