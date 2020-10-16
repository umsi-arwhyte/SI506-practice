# SI 506: Problem Set 05

## Background

This week's problem set includes problems that utilize your knowledge of tuples, conditional statements, for loops, list indexing, slicing, functions and dictionaries.

Problem 1 focuses on tuple manipulation. In Problems 2, 3 and 4, you will build utility functions to perform specific tasks. In Problem 5, you will combine your skills to craft a `main()` function that will reuse the functions defined in Problems 2, 3 and 4 in order to write code more elegantly and more efficiently.

## 1.0 Problem 01 (20 Points)

### 1.1 SETUP

```python
# We provide you with a tuple to start the problem

language1 = ("English",)
```

Replace `pass` with your code in the `problem_set_05.py` file.

### 1.2 Problem

1. Create a new tuple named `language2` with two elements "Spanish" and "German" in this exact order.
2. Join the tuples `language1` and `language2` together and assign it to a new variable called `languages`.
3. Convert the tuple `languages` to a list `languages_list`.
4. Create a new dictionary called `languages_dict` with one key-value pair, with `languages` as the key and `languages_list` as the value. The expected answer is {('English', 'Spanish', 'German'): ['English', 'Spanish', 'German']}

## 2.0 Problem 02 (20 Points)

### 2.1 SETUP

```python
# < recipe > is a list of strings. Each element of < recipe > will be called a step.
# You'll use this data for Problems 2,3,4,5

recipe = [
    'Preheat oven to 350 degrees F (175 degree C).\n',
    'Place the sliced apples in a 9x13 inch pan.\n',
    'Mix the white sugar, 1 tablespoon flour and ground cinnamon together, and sprinkle over the apples.\n',
    'Pour water evenly over all.\n',
    'Combine the oats, 1 cup of flour, brown sugar, baking powder, baking soda and melted butter together.\n',
    'Crumble evenly over the apple mixture.\n',
    'Bake at 350 degrees F (175 degrees C) for about 45 minutes.'
    ]
```

### 2.2 Problem

:exclamation: Recall that strings are immutable. You can't change existing strings, but you can create new strings.

Implement the `format_step()` function by replacing the `pass` statement with the appropriate code block. Read the function Docstring for additional implementation details.

## 3.0 Problem 03 (20 Points)

Implement the `create_step_length()` function by replacing the `pass` statement with the appropriate code block. Read the function Docstring for additional implementation details.

:bulb: if you're using `str.split()`, the seperator should be ": ", instead of just ":"

## 4.0 Problem 04 (20 Points)

The steps of a recipe whose length is larger than half of the maximum of all step lengths are called "core steps".

:exclamation: Given a < step_length > {'step1': 3, 'step2': 5, 'step3': 8} the "core steps" would be step2 and step3 because half the maximum of all step lengths is 4. Based on the definition of "core steps", only step2 and step3 have a step length larger than 4.

Implement the `filter_step_length()` function by replacing the `pass` statement with the appropriate code block. Read the function Docstring for additional implementation details.

:bulb: You can use built-in function `max()` to get the maximum value.

## 5.0 Problem 05 (20 Points)

Now let's put what we have learned together. Use the functions created in Problems 2,3,4 to find the order and content of those "core steps".

:exclamation: Read the function Docstrings to get more information on how to use them.

:bulb: You can use `enumerate()` to help generate the order. Notice that order should start at 1.\
:bulb: Be careful with formatted step and step, they are different.\
:bulb: Since tuples are immutable, elements can't be added to a tuple, but you can join two tuples together.
