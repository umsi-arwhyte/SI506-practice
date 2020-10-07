# START PROBLEM SET 02

# PROBLEM 1
print("\nProblem 1:")

# BEGIN CODING HERE
def addition():
    """
    Simple function to become familiarized with function structure, paramaters, and return
    statements. This function will sum two numbers together.

    Parameters:
        a (any int or float number): A number to be summed
        b (any int or float number): A second number to be summed, with a default value of 10

    Returns:
        float or int: <a> added to <b>
    """
    pass # Implement

# END CODING

# Uncomment the below print() statement when ready.
#print(f"The sum of 5 and 10 is: {addition(5)}")


# PROBLEM 2
print("\nProblem 2:")

def filter(string,max_length):
    """
    This function filters any string passed to it. If the string contains more than <max_length> 
    characters, it will return the string "Too Long!", otherwise it will return <string>.

    Parameters:
        string (str): A string to be filtered.
        max_length (int): If the string has more than this number of characters, 
        it will be too long.

    Returns:
        str: Either "Too Long!" or <string>
    """

    num_chars = len(string)

    if num_chars > max_filter:
        out = "Too Long!"
    else:
        out = "string"

    return out

# Uncomment the following print() statements one at a time. Do not modify the code.
#print(filter("This string has thirty-nine characters!",25))
#print(filter("This string has thirty-nine characters!",40))

# END PROBLEM 2

# PROBLEM 3
print("\nProblem 3:")

# BEGIN CODING HERE
def umich_email_detection():
    """
    This function tests whether a string is a University of Michigan email address. If it is, it 
    returns the uniqname before the '@umich.edu' (e.g., 'janesmith@umich.edu' would return 
    'janesmith'). If it is not a umich email address, this function should return an empty string.

    Parameters:
        potential_email (str): The string to be tested.

    Returns:
        str: either a uniqname or an empty string.
    """
    pass

# END CODING

# When you are ready, uncomment the below lines to test your code.
#print(f"This should print 'janesmith' -> {umich_email_detection('janesmith@umich.edu')}")
#print(f"This should print nothing -> {umich_email_detection('janesmith@msu.edu')}")

# END PROBLEM 3

# PROBLEM 4
# Put what you've learned so far together.
# Refer to the README.md for instructions on this problem.

# BEGIN CODING HERE - OVERWRITE THE EXISTING FUNCTION

def count_words_or_lines():
    pass

# END CODING

# END PROBLEM 4

# PROBLEM 5
print("\nProblem 5:")

# START PROBLEM 05 SETUP (do not modify)

mission = """The mission of the University of Michigan is to serve the people of Michigan
and the world through preeminence in creating, communicating, preserving and applying knowledge,
art, and academic values, and in developing leaders and citizens who will challenge the present and 
enrich the future."""

# END SET UP

# BEGIN CODING HERE
# Replace '-999'.

num_chars = -999
num_words = -999
num_lines = -999
# END CODING

print(f"The number of characters in UM's mission statement is {num_chars}")
print(f"The number of words in UM's mission statement is {num_words}")
print(f"The number of lines in UM's mission statement is {num_lines}")

# END PROBLEM 5

# END PROBLEM SET
