# START PROBLEM SET O5
print('Problem Set 05')

# Problem 01
print('\nProblem 1')

# SETUP
def count_vowels(word):
    lower_word = word.lower()
    num_a = lower_word.count("a")
    num_e = lower_word.count("e")
    num_i = lower_word.count("i")
    num_o = lower_word.count("o")
    num_u = lower_word.count("u")
    total_vowels = num_a + num_e + num_i + num_o + num_u
    return total_vowels

example_words = ["Scrabble",
"puppies",
"kittens",
"mellifluous",
"Supercalifragilisticexpialidocious"
]
# END SETUP

callously_score = None

example_words = None



## PROBLEM 2
print('\nProblem 2')

def score_list(word_list):
    # DELETE PASS AND WRITE IN YOUR OWN CODE
    pass



## PROBLEM 3
print('\nProblem 3')

def who_wins(player1_score, player2_score):
    # DELETE PASS AND WRITE YOUR OWN FUNCTION HERE.
    pass



## PROBLEM 4
print('\nProblem 4')




## PROBLEM 5

# SETUP
def how_much_sleep(hours_slept):
    hours_left = 8 - hours_slept
    if hours_left >= 0:
        return hours_left
    else:
        return 0
# END SETUP

# COMPLETE THE FOLLOWING DOCUMENTATION
'''
Function name:

Explanation:
    This function calculates how much sleep the chatbot has left to sleep.
    The chatbot is supposed to sleep 8 hours a day; if the chatbot has slept fewer hours,
    the function will state how many hours the chatbot has left to sleep.

Parameters:

Returns:

'''