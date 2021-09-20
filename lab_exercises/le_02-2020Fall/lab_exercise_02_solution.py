# START LAB EXERCISE 02
print('Lab Exercise 02 \n')

# SETUP

sandwich_string = 'chicken, bread, lettuce, onion, olives'

# END SETUP

# PROBLEM 1 (4 Points)
sandwich_replace = sandwich_string.replace('olives', 'tomato')


# PROBLEM 2 (4 Points)
# Don't have heavy_cream need to replace with milk
sandwich_list = sandwich_replace.split(", ")


# PROBLEM 3 (4 Points)
sandwich_list.pop(0)


# PROBLEM 4 (4 Points)
sandwich_list.append('cheese')


#  PROBLEM 5 (4 Points)
last_item = sandwich_list[-1]

# END LAB EXERCISE