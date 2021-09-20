# SI 506: Problem Set 05

## This week's Problem Set

This problem set focuses on functions and documentation. The goal of this problem set is to develop the following skills:
(1) Calling on functions with proper input
(2) Processing the output of functions
(3) Become familiar with reading function documentation, and
(4) Writing functions.


## Background
Here we will be working with a newly created chatbot Blinkbot. Among other things, Blinkbot is super interested in playing Scrabble. Scrabble is a popular board game whereby players get tiles, each title having a different letter; depending on the words a player creates, they get a different number of points.

Blinkbot is a simple chatbot, and can only play a modified version of Scrabble. The way Blinkbot plays, a word's score is based on how many vowels (aeiou) it uses: so "hello" has 2 vowels and would get 2 points; "dog" would get 1 point; "rhythm" would get 0 points; and "onomatopeia" would get a full 7 points.

## 1.0 Problem 1 (15 points)
Blinkbot has created a function to help it play Scrabble. The function, called `count_vowels`, takes in a string, and counts how many vowels it has; in other words, what score it gets in Blinkbot's Scrabble. It then returns this score.

1. Find the function in the program file. Read through the documentation and the function carefully to understand how the function works.
<br />

2. Call on `count_vowels` to see how many points the word `"callously"` would get. Store this number in the variable `callously_score`
<br />

3. Using a for loop, call on `count_vowels` to count how many points a player would get if they played all the words in the list `example_words`. Store this score in the variable `example_words_score`
:bulb: Hint: Try using the for loop to call `count_vowels` on each element of `example_words`, and add all of these numbers together!
<br />

```
example_words = ["Scrabble",
"puppies",
"kittens",
"mellifluous",
"Supercalifragilisticexpialidocious"
]
```


## Problem 2 (15 points)
Counting the score of a list of words will be super useful when playing Scrabble -- Blinkbot thinks a function is due! Blinkbot wants a function that takes in a list, and computes the total score of that list. Blinkbot liked the code you wrote in Problem 1.3, but wants a function to generalize this behavior so that it works for _any_ list of strings.

Write the function `score_list` that takes in a list of words, and repeatedly calls on `count_vowels` to compute the total score that all the words in the list have. Here is the documentation for the function:

```
Function name: score_list

Explanation:
    This function takes in a list of words. For each word, it computes its score by counting how many vowels the word has. It then returns the added up total of each word in the list.

Parameters:
    word_list, a list of strings.

Returns:
    An integer representing the added score of each word in the list word_list.
```

This is what example output would look like:

```
val = score_list(["hello", "there", "!"])
print(val)
> 4

val2 = score_list(["this", "was", "a", "triumph"])
print(val2)
> 5
```


## Problem 3 (30 points)
Blinkbot needs to know who wins a game based on their score. It wants to develop a function that, taking two player's scores, announces the winner.

Blinkbot has already written the documentation for the function, but needs help implementing it.

Create the function `who_wins` that takes in two players' scores, and returns a string announcing who is the winner.

The function must work as follows:

If player 1 wins (their score is larger than that of player 2), the function will return "Player 1 wins! Yay!"
If player 2 wins (their score is larger than that of player 1), the function will return "Player 2 wins! Boo."
If the scores are equal, the function will return "It was a tie! Well that's boring."

:warning: The function must _return_ a string, not _print_ a string. In your main program, you can print the output of the function by assigning the output of `who_wins` to a variable and then printing out that variable --> but the function itself should not print anything.

```
Function name: who_wins

Explanation:
    This function determines who has won the game of scrabble based on their player scores, and returns a string appropiately. It returns "Player 1 wins! Yay!" if player 1 wins, "Player 2 wins! Boo." if player 2 wins, and "It was a tie! Well that's boring." if the scores are tied.

Parameters:
    player1_score, an integer representing the score of player 1
    player2_score, an integer representing the score of player 2

Returns:
    A string that shows the results of who has won.
```


This is what example output would look like:
```
val = who_wins(32, 0)
print(val)
> Player 1 wins! Yay!

val2 = who_wins(0, 32)
print(val2)
> Player 2 wins! Boo.

a_draw = who_wins(0, 0)
print(a_draw)
> It was a tie! Well that's boring.
```


## Problem 4 (30 points)
Blinkbot is excited! Now that it can count how many vowels are in a word (and so assign a score to a word); score a list of words; and can tell who wins depending on their score; it is time to join these functions together! Blinkbot is absolutely _thrilled_ about this, and keeps screaming __MUAHAHAHAHA__ to anyone who will listen.

_(We are slightly concerned about Blinkbot's enthusiasm with Scrabble.)_

Complete the function `play_blinkbot_scrabble` that allows Blinkbot to play Scrabble and determine a winner. It takes in two lists of strings: each list represents the words created by player 1 and 2 accordingly. The function then returns a string announcing the winner. Blinkbot has already written the documentation; now it's time to implement it.

The function should call on both `score_list` and `who_wins`, and use their outputs to determine who wins the game. The function must then output "Player 1 wins! Yay!" if player 1 wins, "Player 2 wins! Boo." if player 2 wins, and "It was a tie! Well that's boring." if the players are tied.

:warning: Notice that we have not written the function definition for you; you will have to write it yourself!


```
Function name: play_blinkbot_scrabble

Explanation:
    This function takes in a list of scrabble words from player 1 and player 2, and determines who is the winner, after computing their score. It must output "Player 1 wins! Yay!" if player 1 wins, "Player 2 wins! Boo." if player 2 wins, and "It was a tie! Well that's boring." if the players are tied.

Parameters:
    list_player1_words, a list of strings
    list_player2_words, a list of strings

Returns:
    A string that shows the results of who has won.
```

This is what example output would look like:

```
game1 = play_blinkbot_scrabble(["many", "vowels", "many", "words"], ["fewer"])
print(game1)
> Player 1 wins! Yay!

game2 = play_blinkbot_scrabble(["not", "fair"], ["Hahahahahahaha", "Loser"])
print(game2)
> Player 2 wins! Boo.

game3 = play_blinkbot_scrabble(["we're", "tied"], ["of", "course"])
print(game3)
> It was a tie! Well that's boring.
```


## Problem 5 (10 points)
We finally figured out why Blinkbot was so excited -- it had not gotten enough sleep, meaning it had drunk a _lot_ of coffee and was pumped up on caffeine. To help Blinkbot get more sleep, we developed a function called `how_much_sleep`. Blinkbot tells the function how many hours it has slept, and the function outputs how many more hours Blinkbot needs to sleep, with the idea that Blinkbot should get 8 hours of sleep every night.

In our rush, we forgot to complete the documentation for the function, and Blinkbot is unsure of how to use `how_much_sleep`! Complete the documentation for the function `how_much_sleep`. Remember to include the function name, the parameters, and what the function returns!


:bulb: Feel free to look at the documentation for the other functions in the problem set ands use them as inspiration / a template.

```
def how_much_sleep(hours_slept):
    hours_left = 8 - hours_slept
    if hours_left >= 0:
        return hours_left
    else
        return 0
```