# SI 506: Lab Exercise 03

## This Week's Lab

This week's lab exercise includes three (3) problem, having two to three lines of code which focus on:
* function creation
* argument assignment
* string concatenation
* function calls

## Background

This week is the begining of the Chinese New Year and the Spring Festival. Let's learn more! We are writing a function with two positional arguments here. (Learn about python functions: https://www.w3schools.com/python/python_functions.asp)

## 1.0 Problem 01 (5 Points)

### 1.1 SETUP

This is your global variable that can be reached from anywhere in the program. In this class we will be using all capital letters for global variables.
LUNAR_YEAR = "2020"

:hint: Comment out or replace `pass` with your code.

### 1.2 PROBLEM

1. Write the header for the function named `lunar_new_year()`. Pass two positional arguments:
`year` (data type: integer) and `year_animal` (data type: string) in this exact order.\
Sample input to function: `lunar_new_year(2020, "rat")`\
Sample output, returns  the formatted string:
  ```python
  "2020 is the year of rat."
  ```
:warning: Indent within the function!

2. Implement the function by concatenating the arguments passed in the same order, to a string
 using `str.format()`, and set it to the global variable named `LUNAR_YEAR`.\
 Use this format "{} is the year of {}.\n" and set your values.\
:exclamation: Use the `global` keyword if you want to modify a global variable inside a function.
```python
global LUNAR YEAR
```

3. Return `LUNAR_YEAR`

:tada: You have created your first python function! Let's go further

## 2.0 PROBLEM 02 (10 points)

### 2.1 SETUP

Let's learn how to set default values for argument and return a value. When default values for the arguments are set, the function can be called without passing arguments.

We will write a function that provides information on the new year festivities.

### 2.2 PROBLEM

1. Write the header for the function named `festivities_info()` with two arguments:
`date_start` (data type: string) and `message` (data type: string).
2. Assign the default arguments "8-Feb" to `date_start` and "Lantern Festival" to `message` using '='. \
:warning: Make sure you have the arguments in this order.\
Sample input to function:\
festivities_info(date_start = "February 8", message = "Lantern Festival")\
Sample output, returns the formated string message:
```python
"February 8 is the day of Lantern Festival."
```
:warning: Make sure you indent first!

3. Implement the function by concatenating `date_start` and `message` using f-string and assign this to a new variable called `new_message`. This is your local variable. Use this formatting "{} is the day of {}.\n"

4. Return `new_message`

:tada: Great! We have two functions, now let's call them.

## 3.0 PROBLEM 03 (5 points)

### 3.1 SETUP

This is the main function that will be called when the program runs.\
Within the `main()` function we will call the `lunar_new_year()` and `festivities_info()` functions.

### 3.2 PROBLEM

1. Print the global variable `LUNAR_YEAR`.
2. Call the `lunar_new_year()` function within a print statement and pass "2020 " and "rat" in this exact order.
:exclamation: You are modifying the global variable `LUNAR_YEAR` in this function which you will see in step 4.
3. Call the `festivities_info()` function within a print statment. Pass "February 8" as an argument, we will use the default value for the second argument.
4. Print the global variable `LUNAR_YEAR` and to see its changes.

:hint: Leave an indentation as this is within the 'main' function.
