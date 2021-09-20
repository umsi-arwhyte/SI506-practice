# SI 506: Lab Exercise 06

## This week's Lab Exercise

This week's lab exercise includes four (4) problems that focus on functions, tuples, and controlling
execution flow via the `main()` function.

## Data description

The variable `mario_kart_game` is a list of tuples. Each tuple consists of a Mario Kart video game
player and their current points in the game.

## 1.0 Problem 01 (5 Points)

Create a function `scores()` that returns a tuple of the total score obtained by two competing
teams. The first three players in the game are team one and the last three players are team two. Sum
the scores for each team and return as a tuple containing the two score totals. The function `scores()` will take a list of tuples as a parameter.

In `main()`, call the function `scores()` and assign the return value to the variable `team_scores`.

An example of how to call `scores()`:

```python
team_scores = scores(mario_kart_game)
```

The output of `team_scores` will have different values than what is shown below but will be formatted as:

```python
(130, 30)
```

The first value is the total score from team one and the second value is the total score from team two.

## 2.0 Problem 02 (5 Points)

In this game, a blue shell item will place the player in first place in third. Create a function
`blue_shell()` that will move the person in first place into third. The function `blue_shell()` will take in a list of tuples as a parameter.

In `main()`, call the function `blue_shell()` and assign the return value to the variable
`blue_shell_players`.

An example of how `blue_shell()` alters the players in the game:

```python
current_game = [('Mario', 43), ('Peach', 32), ('Yoshi', 28), ('Bowser', 25), ('Toad', 18)]
```

Output after `blue_shell()` alters `current_game`:

```python
[('Peach', 32), ('Yoshi', 28), ('Mario', 43), ('Bowser', 25), ('Toad', 18)]
```

## 3.0 Problem 03 (5 Points)

The variable `new_mario_kart_game`, is a new list of players and their points. In `main()`, Add
another tuple with the character, "Bowser", who has 60 points in the game.

## 4.0 Problem 04 (5 Points)

Create a function `top_three()` that returns a list of the top three players' names from `new_mario_kart_game` The function `top_three()` will take in a list of tuples as a parameter.

An example of how  `top_three()` works

```python
mario_kart= [('Donkey Kong', 45), ('Mario', 30), ('Yoshi', 22), ('Wario', 20)]
top_three(mario_kart) 
# should return ['Donkey Kong', 'Mario', 'Yoshi']
``` 

In `main()`, call the function `top_three()` and assign the return value to the variable
`top_three_players`.