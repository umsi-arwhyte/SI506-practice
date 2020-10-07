# START LAB EXERCISE 06
print('Lab Exercise 06 \n')

# PART 1: Midterm Practice

# The following two problems are to familiarize you with the format
# of the midterm. You will be asked to create a simple function and call it.
# This portion of the lab exercise will be timed. Please follow the intructions
# from your instructor.

# PROBLEM 1 (5 Points)

# In this problem you will implement a simple function that:
# 1) Has two arguments: one is a default
# 2) Uses a local variable
# 3) Iterates through a list
# 4) Appends to a list
# 5) Returns a value

# BEGIN PROBLEM 1 SOLUTION

# Create a function named < calculate_exponent > based on the docstring provided.
# You will be calling this function in problem 2.

def calculate_exponent(): # Missing parameters
    """
    This function calculated the power for a given list of integers. You will have
    to iterate through the list and apply the operation.

    Parameters:
        nums (list of int): A list of numbers whose power has to be calculated.
        power (int): This is the value used to compute power.
            Its default value is 2 (power=2)

    Returns:
        list: Returns a list of integers whose exponents have been calculated

    Use a local variable named < num_power > to calculate the result of raising
    a number to it's exponent < power >, use < exponents > to store the computed powers
    and return the < exponents > variable.

    Hint : you can use the exponent operator (**) syntax: x**y to find x to the power of y
    """

    pass # Implement


# END PROBLEM 1 SOLUTION


# PROBLEM 2 (5 Points)

# In this problem you will:
# 1) Call a function
# 2) Pass positional and keyword arguments
# 3) Work with lists

# SETUP - DO NOT MODIFY

# We provide you with a list of integers and two empty lists to start the problem

ints = [2, 4, 6, 8]

exponents_1 = []
exponents_2 = []

# END SETUP

# BEGIN PROBLEM 2 SOLUTION

# Problem 2 part 1:
# Call the < calculate_exponent() > function that you created in problem 1 and
# pass < ints > as a positional argument.
# Store the results in < exponents_1 >


# Problem 2 part 2:
# Call the < calculate_exponent() > function that you created in problem 1 and
# pass < ints > as a keyword argument and 3 (three) as a keyword argument.
# Store the results in < exponents_2 >


# END PROBLEM 2 SOLUTION

print(f"\nProblem 2: exponents_1 = {exponents_1}\n")
print(f"\nProblem 2: exponents_2 = {exponents_2}\n")


# PART 2: TUPLES

# The following 2 problems will introduce you to working with tuples.
# If a problem includes a setup section: Do not modify, delete or otherwise ignore the setup code.

# Print statements have been provided to debug your code.

# PROBLEM 3 (5 Points)

# In this problem you will:
# 1) Work with tuples
# 2) Differentiate between tuples and lists
# 3) Update tuples

# BACKGROUND

# Turns out we forgot to include 'hershey milk chocolate' and  'kisses'.
# Unlike lists, tuples are immutable and cannot be changed or appended once they are initialized.
# Using tuples instead of lists can give the programmer a hint that data should not be changed.
# However, we are able to take existing tuples and add them to create a new tuple.

# SETUP - DO NOT MODIFY

# < nut_free_candy > is a tuple of nut free candies

nut_free_candy = ('skittles', 'jolly rancher', 'twizzler', 'york')

# END SETUP

# BEGIN PROBLEM 3 SOLUTION

# Create a new tuple called < extra_candy > and initialize it with 'hershey milk chocolate' and  'kisses'.


# Concatenate the two candy tuples by < nut_free_candy > + < extra_candy >
# and assign it to < updated_nut_free_candy >.
updated_nut_free_candy = ()

# END PROBLEM 3 SOLUTION

print(f"\nProblem 3: updated_nut_free_candy = {updated_nut_free_candy}")


# PROBLEM 4 (5 Points)

# In this problem, you will:
# 1) Use a tuple as a key in dictionaries
# 2) Work with dictionaries

# Lists and tuples have a lot of similar features except tuples are immutable and they use parentheses instead of brackets.
# Because of the immutable nature, tuples can also be used as keys in dictionaries.

# BEGIN PROBLEM 4 SOLUTION

# Create a dictionary named < candy_dict >, this dictionary will have only one key-value pair.
# Assign < updated_nut_free_candy > as the key and 'nut-free' as the value.
# hint: follow this syntax < dict > = {< key > : < value >}
candy_dict = {}

# END PROBLEM 4 SOLUTION

print(f"\nProblem 4: candy_dict = {candy_dict}")

# END PART 2


# END LAB EXERCISE
