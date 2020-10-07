print('Lab Exercise 05')
# LAB EXERCISE 05


# PROBLEM 1 (5 Points)

# Problem 01 SETUP - We provide you with a dictionary to start the lab problems

fruits = {'apple': 10, 'banana': 20, 'strawberry': 6, 'orange' : 9}

# Problem 01 END SETUP

# BEGIN PROBLEM 1 SOLUTION

num_fruits = []

for value in fruits.values():
    num_fruits.append(value)

# END PROBLEM 1 SOLUTION

print(f"\nProblem 1: num_fruits = {num_fruits}")


# PROBLEM 2 (5 Points)

# Problem 02 SETUP - We provide you with a variable to start the problem

sum_fruits = 0

# Problem 02 END SETUP

# BEGIN PROBLEM 2 SOLUTION

for value in fruits.values():
    sum_fruits = value + sum_fruits

# END PROBLEM 2 SOLUTION

print(f"\nProblem 2: sum_fruits = {sum_fruits}")

# PROBLEM 3 (5 Points)

# Problem 03 SETUP - We provide you with a variable to start the problem

max_fruits = 0

# Problem 03 END SETUP

# BEGIN PROBLEM 3 SOLUTION

max_fruits = -1
for value in fruits.values():
    if value > max_fruits:
        max_fruits = value

# END PROBLEM 3 SOLUTION

print(f"\nProblem 3: max_fruits = {max_fruits}")

# PROBLEM 4 (5 Points)

new_dict = {}

# Problem 04 END SETUP

# BEGIN PROBLEM 4 SOLUTION

for key in fruits:
    if fruits[key] > 6:
        new_dict[key] = fruits[key]

# END PROBLEM 4 SOLUTION

print(f"\nProblem 4: new_dict = {new_dict}\n")

# END LAB EXERCISE
