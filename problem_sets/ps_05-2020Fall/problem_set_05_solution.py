# START PROBLEM SET O5
print('Problem Set 05')

# Problem 01
print('\nProblem 1')

# SETUP
"""
Function name:
    count_vowels

Explanation:
    This function counts the number of vowels in a string and returns that number.
    It is used by the chatbot to count the score of a word in modified scrabble.

Parameters:
    word, a string.

Returns:
    A number indicating the number of vowels in that sentence.
"""
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

callously_score = count_vowels("callously")


example_words_score = 0

for word in example_words:
    example_words_score += count_vowels(word)



## PROBLEM 2
print('\nProblem 2')

def score_list(word_list):
    word_list_score = 0
    for word in word_list:
        word_list_score += count_vowels(word)
    return word_list_score



## PROBLEM 3
print('\nProblem 3')

def who_wins(player1_score, player2_score):
    if player1_score > player2_score:
        return "Player 1 wins! Yay!"
    elif player1_score < player2_score:
        return "Player 2 wins! Boo."
    else:
        return "It was a tie! Well that's boring."




## PROBLEM 4
print('\nProblem 4')

def play_blinkbot_scrabble(list_player1_words, list_player2_words):
    player1_score = score_list(list_player1_words)
    player2_score = score_list(list_player2_words)

    winner = who_wins(player1_score, player2_score)
    return winner



## PROBLEM 5
# SETUP
def how_much_sleep(hours_slept):
    hours_left = 8 - hours_slept
    if hours_left >= 0:
        return hours_left
    else:
        return 0
# END SETUP

'''
Function name:
    how_much_sleep


Explanation:
    This function calculates how much sleep the chatbot has left to sleep.
    The chatbot is supposed to sleep 8 hours a day; if the chatbot has slept fewer hours,
    the function will return how many hours the chatbot has left to sleep.

Parameters:
    hours_slept, an integer

Returns:
    An integer representing how many hours of sleep Blinkbot has left to sleep.
'''

