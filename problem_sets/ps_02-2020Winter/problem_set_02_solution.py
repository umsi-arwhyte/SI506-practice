# START PROBLEM SET 02

# PROBLEM 1
print("\nProblem 1:")
# Use the below <addition> function stub to create a function with the specifications given in the
# docstring.

# BEGIN CODING HERE
def addition(a, b=10): # <-- Don't forget to fill out the function arguments!
    """
    Simple function to become familiarized with function structure, paramaters, and return
    statements. This function will sum to numbers together.

    Parameters:
        a (any int or float number): A number to be summed
        b (any int or float number): A second number to be summed, with a default value of 10

    Returns:
        (float or int): <a> added to <b>
    """

    c = a + b

    return c
# END CODING

# When you are finished with the <addition> function, uncomment the below line of code to see
# if it works!
print(f"The sum of 5 and 10 is: {addition(5)}")


# PROBLEM 2
print("\nProblem 2:")
# First, analyze the below <filter> function. Look at its docstring, arguments, and code body.
# Then, uncomment the indicated lines of code below the function definition. If you run this
# code, you will get a traceback error. Locate the source of the errors and fix them.

def filter(string,max_length):
    """
    This function filters any string passed to it. If the string contains more than
    <max_length> characters, it will return the string "Too Long!", otherwise it will
    return <string>.

    Parameters:
        string (str): A string to be filtered.
        max_length (int): If the string has more than this number of characters,
            it will be too long.

    Returns:
        (str): Either "Too Long!" or <string>
    """

    num_chars = len(string)

    if num_chars > max_length: # first fix
        out = "Too Long!"
    else:
        out = string # second fix

    return out

# Uncomment the following two lines of code, one at a time. The first will throw an exception, and the
# second will fail silently (in other words, the code will work, but not produce the
# output we desire). Fix both errors by modifying the code in the function <filter>. You
# need not modify any of the code in the following two lines, save for uncommenting them.

print(filter("This string has thirty-nine characters!",25))
print(filter("This string has thirty-nine characters!",40))

# END PROBLEM 2

# PROBLEM 3
print("\nProblem 3:")
# Fill out the <umich_email_detection> function, given the function stub and docstring.
# Test your code below the function by uncommenting the test lines of code.
# You will need to use a conditional statement.
# HINT: use a string method to identify which strings end with "@umich.edu".
# A list of string methods is available here:
# https://www.w3schools.com/python/python_ref_string.asp

# BEGIN CODING HERE
def umich_email_detection(potential_email):
    """
    This function tests whether a string is a University of Michigan email address.
    If it is, it returns the uniqname before the '@umich.edu' (e.g., 'janesmith@umich.edu'
    would return 'janesmith'). If it is not a umich email address, this function should return
    an empty string.

    Parameters:
        potential_email (str): The string to be tested.

    Returns:
        (str): either a uniqname or an empty string.
    """

    if potential_email.endswith('@umich.edu'):
        return potential_email.split('@')[0]
    else:
        return ''
# END CODING

# When you are ready, uncomment the below lines to test your code.
print(f"This should print 'janesmith' -> {umich_email_detection('janesmith@umich.edu')}")
print(f"This should print nothing -> {umich_email_detection('janesmith@msu.edu')}")

# END PROBLEM 3

# PROBLEM 4
# Put what you've learned so far together.
# Write a function from scratch that fulfills the below specifications:
"""
Function name: count_words_or_lines

Parameters:
    string (str): A string that will be operated upon.
    operation (str): Accepts either "lines" or "words". Should have a default value
        of "words".

Returns:
    (int): The number of lines or words in <string>, depending on the choice
        of <operation>

Explanation:
    You should use conditionals to determine what is returned by this function.
    If <operation> is "words", return the number of words in <string>. If
    <operation> is "lines", return the number of lines in <string>. If <operation>
    is neither, this function should return "Choose a correct operation".
    Make sure your function has the default value of "words" for <operation>.
"""

# BEGIN CODING HERE
def count_words_or_lines(string,operation="words"):

    if operation == "words":
        return len(string.split())
    elif operation == "lines":
        return len(string.splitlines())
    else:
        return "Choose a correct operation"
# END CODING

# END PROBLEM 4

# PROBLEM 5
print("\nProblem 5:")
# Using your <count_words_or_lines> function, determine the number of
# words and lines in the University of Michigan mission statement (provided below)
# and assign those numbers to <num_words> and <num_lines>, respectively. Also, determine
# the number of characters in <mission> and assign it to <num_chars>.

mission = """The mission of the University of Michigan is to serve the people of Michigan
and the world through preeminence in creating, communicating, preserving and applying knowledge, art,
and academic values,
and in developing leaders and citizens who will challenge the present and enrich the future."""

# BEGIN CODING HERE
num_chars = len(mission)
num_words = count_words_or_lines(mission)
num_lines = count_words_or_lines(mission,operation="lines")
# END CODING

print(f"The number of characters in UM's mission statement is {num_chars}")
print(f"The number of words in UM's mission statement is {num_words}")
print(f"The number of lines in UM's mission statement is {num_lines}")

# END PROBLEM 5

# END PROBLEM SET
