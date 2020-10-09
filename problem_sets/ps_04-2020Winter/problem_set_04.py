# START PROBLEM SET 04
print('PROBLEM SET 04 \n')

# BACKGROUND

# In this homework, you'll work with data from 2016 Summer Olympics.
# With these data we will code with dictionaries, looping, conditional
# statements, functions, and string processing.

# PROBLEM 1.0 (10 points)

# SETUP
# Below are key,value pairs providing information on gymnast Simone
# Biles.

# KEY           VALUE
# "athlete"     Simone Biles
# "sport"       gymnastics
# "born"        1997
# "age"         < Make this the difference between the year born and the
#               current year. You MUST do this programmatically (i.e.
#               using math operators), not just writing in one number. >

# END SETUP

# Refer to Problem Set 04 README.md for instructions and tips.

# BEGIN PROBLEM 1.0 SOLUTION
# 1.1 Assign key,value pairs to the < simone_biles > dictionary

simone_biles = None

# BEGIN PROBLEM 1.0 SOLUTION

print(f"\nProblem 1: simone_biles = {simone_biles}")


# PROBLEM 2.0 (10 points)

# SETUP
# Use the < golds > dictionary, it contains all of the nations that
# obtained at least 5 gold medals in the 2016 Summer Olympics.

golds = {
    "USA" : 46,
    "GBR" : 27,
    "CHN" : 26,
    "RUS" : 19,
    "GER" : 17,
    "JPN" : 12,
    "FRA" : 10,
    "KOR" : 9,
    "ITA" : 8,
    "AUS" : 8,
    "NED" : 8,
    "HUN" : 8,
    "BRA" : 7,
    "ESP" : 7,
    "KEN" : 6,
    "JAM" : 6,
    "CRO" : 5,
    "CUB" : 5
}

# END SETUP

# BEGIN PROBLEM 2.0 SOLUTION
# 2.1 Assign values to variable < medal_count >

medal_count = None

# END PROBLEM 2.0 SOLUTION

print(f"\nProblem 2: medal_count = {medal_count}")


# SETUP for PROBLEMS 3.0, 4.0, 5.0, and 6.0

laurel_of_hellas = """
Laurel of Hellas noble-born
you tree of honoured name,
reaching over unnumbered years
your leaves extend their fame
and branches high proclaim the pride
of one who never bowed
except to place your crown upon
the victors brow.

O stately laurel noble-born
O tree severely grand
that in the soil of heroes grows,
sacred, defended land.
Let faint of heart, unmanly soul
your hard won fortune shun:
your home was at Thermopylae
and Marathon.

Laurel of Hellas noble-born,
most celebrated tree,
gazing to your lofty crown
the mind must dazzled be.
Up to the blue your head is raised,
to earth your strong root strains,
and under your shining leaves are played
the noble, timeless games.
"""

# END SETUP

# PROBLEM 3.0 (20 points)

# BEGIN PROBLEM 3.0 SOLUTION
# 3.1 Implement the < process_string() > function

def process_string(): # Missing parameters
    """
    < process_string() > will take any < string > passed as a parameter
    and perform three operations on it, in this order:
    1. Make the entire < string > lower-case.
    2. Remove all punctuation (i.e. replace all punctuation with an
    empty string like this: "")
    3. Create a list of all of the words in < string >.
    4. The < process_string() > function will return the list of words.

    Parameters:
        - string (str): The string that will be operated upon.

    Returns:
        - (list): A list of the processed words in <string>

    NOTE: For convenience, we have provided a list of the punctuation
    that you need to remove.
    """

    punctuation = ["'",",",".","?"]
    pass # Implement

# END PROBLEM 3.0 SOLUTION

# PROBLEM 4.0 (20 points)

# BEGIN PROBLEM 4.0 SOLUTION
# 4.1 Implement the < word_frequency() > function

def word_frequency(): # Missing parameters
    """
    < word_frequency() > will take a list of word strings and return a
    dictionary with the words as keys and the number of occurances of
    the word in the < list_of_words > as the values.

    Parameters:
        - list_of_words (list): A list of words strings from which to calculate
        word frequency.

    Returns:
        - (dict): A dictionary of the form {<word (str)> : <number of
        occurances of word (int)>}
    """

    pass # Implement


# END PROBLEM 4.0 SOLUTION

# PROBLEM 5: (20 points)

# BEGIN PROBLEM 5.0 SOLUTION
# 5.1 Implement the < find_common_words() > function

def find_common_words(): # Missing parameters
    """
    < find_common_words() > will take a < frequency_dictionary > that
    describes how many times a word has occurred in a list of strings, and
    return a list of the words that have occurred more than or equal
    to < cutoff > times.

    Parameters:
        - frequency_dict (dict): A dictionary of the form {< word (str) > :
                < number of occurances of word (int) >}. The returned
                object from < word_frequency() > should work here.
        - cutoff (int): The minimum number of occurances of a word in
                order for it to be included in the returned list.

    Returns:
        - (list): A list of the words that occured more than or equal
        to < cutoff > times.
    """

    pass # Implement

# END PROBLEM 5.0 SOLUTION

# PROBLEM 6.0 (20 points)

# BEGIN PROBLEM 6.0 SOLUTION
# 6.1 Implement the < main() > function

def main(): # Missing parameters
    """
    Call < process_string() >, < word_frequency() >, and < find_common_words() >
    in order to create a list of the words that occur in < poem > at least
    3 times. Return that list of common words.

    Parameters:
        - poem (str): Any string. All of the words that occur in < poem >
                at least 3 times will be included in the returned list.

    Returns:
        - (list): A list of all of the words in < poem > that occured
        at least 3 times.
        """

    pass # Implement

# END PROBLEM 6.0 SOLUTION

if __name__ == "__main__":

    result = main(laurel_of_hellas)
    print(f"\nThe final result of problems 3.0, 4.0, 5.0, and 6.0 (should be a list of 'laurel', 'of', 'noble-born', 'tree', 'your', 'and', 'the', 'to'):{result}")

# END PROBLEM SET 04
