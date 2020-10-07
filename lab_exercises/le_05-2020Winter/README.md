# SI 506: Lab Exercise 05

## This Week's Lab
This week's lab focuses on a new data construct, dictionaries. You will complete four
exercises involving dictionaries so that you can become familiar with how they work,
and why they are so important to python.

## Background
The following 4 problems will introduce you to working with dictionaries.
If a problem includes a setup section: Do not modify, delete or otherwise ignore
the setup code.

You will save lists and dictionaries to required variables. These variables will be graded by autograder after your submission.
Print statements have been provided for you to debug the code. You can uncomment them to see the results.

## 1.0 Problem 01 (5 Points)

In this problem you will demonstrate your ability to

1. Work with dictionaries
2. Work with lists
3. Manipulate data using dictionaries
4. Convert the values of dictionaries to lists

We provide you with a dictionary to start the lab problems.

```python
fruits = {'apple': 10, 'banana': 20, 'strawberry': 6, 'orange' : 9}
```

Save the values of the dictionary `fruits` into a list `num_fruits`. The desired
answer is [10, 20, 6, 9].

:bulb: You can do this by calling the values of the dictionary.

## 2.0 Problem 02 (5 Points)

In this problem, you will demonstrate your ability to

1. Iterate through the dictionary
2. Add the values of each pair
3. Save tha value to a variable

We provide you with a variable to start the problem.

```python
sum_fruits = 0
```

Find the sum of the values of the `fruits` dictionary. Do not use the list `num_fruits`. Save to the variable `sum_fruits`. Iterate through each key-value pair in the dictionary and add the numbers. Save the sum of the numbers to the variable `sum_fruits`.

## 3.0 Problem 03 (5 Points)

In this problem you will demonstrate your ability to

1. Work with dictionary
2. Work with the values
3. Find the largest value

We provide you with a variable to start the problem.

```python
max_fruits = 0
```

Find the largest value in the `fruits` dictionary.

:bulb: You can use some parts of Problem 02.

:warning: Do not use the list `num_fruits` and then save to the variable `max_fruits`.

Iterate through each key-value pair in the dictionary named `fruits`. Work with values and save to a variable.

## 4.0 Problem 04 (5 Points)

In this problem you will demonstrate your ability to

1. Create a new dictionary using an existing one
2. Iterate through a dictionary
3. Work with values
4. Connect the keys based on value

We provide you with a variable to start the problem.

```python
new_dict = {}
```

Create a new dictionary using the `fruits` dictionary. Save the key value pairs which has a value of more than 6 to the new dictionary named `new_dict`.

Iterate through the dictionary `fruits`. Use an if statement to check if the value is greater than 6. Add the pair to the new dictionary.