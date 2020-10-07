# START PROBLEM SET 01
print('PROBLEM SET 01 \n')

# BACKGROUND

# The programming language Python was originially released in 1991 and was
# created by Guido van Rossum. The language emphasizes code readability and
# maintainability. Python is open source with programmers from all over the
# world working to maintain and develop the language further.

# PROBLEM 1 (10 points)

# SETUP - DO NOT MODIFY

languages = ['Java', 'C++', 'Javascript', 'Ruby', 'Python', 'Fortran']

# END SETUP

# BEGIN PROBLEM 1 SOLUTION

# Uncomment the variable name and assigned value that adheres to the Python style guide.

# 1st_bdfl = 'Guido van Rossum'
# benevolent_dictator_for_life! = 'Guido van Rossum'
# python author = 'Guido van Rossum'
python_author = 'Guido van Rossum'
# lambda = 'Guido van Rossum'

# Use list indexing to assign the language that Guido von Rossum
# authored to the variable < guido_language >.

guido_language = languages[-2] # Can also be an index of 4

# Note the below use of the formatted string literal (f-string) to
# incorporate a variable into a string in the print statement.
print(f'Guido van Rossum authored {guido_language}\n')

# END PROBLEM 1 SOLUTION


# PROBLEM 2 (10 points)

# START PROBLEM 2 SOLUTION

# Concatenate Guido's current position to the value of the uncommented variable.
# Assign the value to < python_foundation_officer >.

python_foundation_officer = python_author + ', President'

# Note the below use of the formatted string literal (f-string) to
# incorporate a variable into a string in the print statement.
print(f'python_foundation_officer = {python_foundation_officer}\n')

# END PROBLEM 2 SOLUTION


# PROBLEM 3 (20 points)

# SETUP - DO NOT MODIFY

# The Zen of Python, by Tim Peters (1999)

# Note the use of triple (""") quotes to denote a multi-line string.
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

print(f'zen_of_python = {zen_of_python}\n')

# END SETUP

# BEGIN PROBLEM 3 SOLUTION

# Replace 'None' with the number of characters in < zen_of_python >

num_chars = len(zen_of_python)

print(f'num_chars = {num_chars}')

# END PROBLEM 3 SOLUTION


# PROBLEM 4 (20 points)

# BEGIN PROBLEM 4 SOLUTION

# Determine the number of words in < zen_of_python >.

chunks = zen_of_python.split()
num_char_chunks = len(chunks)

print(f'num_char_chunks = {num_char_chunks}\n')

# END PROBLEM 4 SOLUTION


# PROBLEM 5 (20 points)

# BEGIN PROBLEM 5 SOLUTION

# Find the average number of cunks per line.

num_lines = len(zen_of_python.splitlines())
# num_lines = 20
avg_num_chunks_per_line = num_char_chunks // num_lines

# Notice how we can also use the string method .join() to join all of the elements
# in a list by including that string in between each element.
# Note use of the built-in < str() > function to format < avg_num_chunks_per_line > as a string.
print(''.join(['avg_num_chunks_per_line = ', str(avg_num_chunks_per_line), '\n']))

# END PROBLEM 5 SOLUTION


# PROBLEM 6 (20 points)

# BEGIN PROBLEM 6 SOLUTION

# Substitute the word "Dutch" for your umich email in < zen_of_python >
# assign this new string to < zen_of_pythin_uniqname >.

email_address = 'arwhyte@umich.edu'
zen_of_python_uniqname = zen_of_python.replace('Dutch', email_address)

print(''.join(['zen_of_python_uniqname = ', zen_of_python_uniqname, '\n']))

# END PROBLEM 6 SOLUTION

# END PROBLEM SET
