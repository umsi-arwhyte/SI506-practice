# START LAB EXERCISE 01

# The below line will print the string "Lab Exercise 01" to the command line, and then
# print a new line (which is what the "\n" stands for)
print('Lab Exercise 01 \n')


# PROBLEM 1 (10 points)

# Using a code editor of your choice, edit the below lines so that the variables
# <name>, <class_number>, and <editor> have a value of your name, the class number (506),
# and the editor program you used to edit this file, respectively.

# BEGIN SOLUTION 1

name = "Luke Skywalker" # <- make sure this has quotes around it so that it is a string variable
class_number = 506 # <- no quotes required here because it is an integer variable
editor = "Atom" # <- again, make sure this has quotes around it

# END SOLUTION 1


# PROBLEM 2 (10 points)

# Create a list object named <my_first_list> that contains <name>, <class_number>, and <editor>,
# in that order.

# BEGIN SOLUTION 2

my_first_list = [name, class_number, editor]

# END SOLUTION 2

# - Don't change any code below this line! - # - # - # - # - # - #
print(f"My name is {name}.\nI am enrolled in SI {class_number}.\nMy preferred editor is {editor}")
print(f"My first list:\n{my_first_list}")
# END LAB EXERCISE
