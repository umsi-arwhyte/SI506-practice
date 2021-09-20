# SI 506: Problem Set 06

## This week's Problem Set

This problem set focuses on functions, optional parameters, tuple returns, docstrings, and
controlling execution flow via the `main()` function.

## Background

Super Smash Bros. is a series of crossover fighting video games published by Nintendo, and primarily features characters from various Nintendo franchises. The series features many popular characters, including Super Mario, Donkey Kong, The Legend of Zelda, Metroid, Star Fox, Kirby, Yoshi, and Pokémon. The fifth and latest installment, Super Smash Bros. Ultimate, was released in 2018 for the Nintendo Switch.

In this problem set, you will be implementing functions that help the players select their characters, game modes and other attributes.

## 1.0 Problem 1 (30 points)

1. Create a function named  `start_classic` and set `game_type` as an optional parameter with the default value as `None`. This function checks if arguments other than `None` were assigned to `game_type` and creates strings formatted as `"Game Type: <variable_name> "`. This formatted string is the return value from this function. If no values is assigned to the parameter, `None` is returned. (10 points)

:bulb: The following is the expected format for the return value:

```python
# if  <game_type> is not None:
    return f"Game Type: {<variable_name>}"

# if <game_type> is None:
    return None

```

2. Create a function named `start_smash` and set `stage`, `game_type`  as optional parameters. Specify `None` as the default value to all optional parameters. This function checks if arguments other than `None` were assigned to `stage` or `game_type` and creates strings formatted as `"Stage: <variable_name> "` and/or `"Game Type: <variable_name>"`for both `stage` and `game_type`. The return is a tuple with both the formatted strings. If no values are assigned to either of the parameters, `None` is returned in place of the formatted string of each parameter. If you are returning a tuple return the tuple with the f-strings of  `stage` first and then `game_type`. (15 points)

:bulb: The following is the expected format for the return value:

```python
# if <stage> and <game_type> are both not None:
    return (f"Stage: {<variable_name>}", f"Game Type: {<variable_name>}")

# if only <stage> is not None:
    return f"Stage: {<variable_name>}"

# if only <game_type> is not None:
    return f"Game Type: {<variable_name>}"

# if both <game_type> and <stage> are None:
    return None
```

3. Within the `main` function, make a function call to `start_smash` and pass the string `"Mushroomy Kingdom"` as the argument for `stage` and save the returned value to a variable named `match1` to check for the correct implementation of the `start_smash` function. If you print `match1`, your expected return should be `"Stage: Mushroomy Kingdom"`. (2.5 points)

4. Within the `main` function, make a function call to `start_classic` and pass the string `training` as the argument for `game_type` and save the returned value to a variable named `match2` to check for the correct implementation of the `start_classic` function. If you print `match2`, your expected return should be `"Game Type: training"`. (2.5 points)

## 2.0 Problem 2 (40 points)

Create a function named `select_match` and fulfill the following requirements:

1. The function `select_match` is provisioned with the following parameters: `player_1` (required), `mode` (required), `player_2` (optional), `stage`(optional) and  `game_type`(optional).  The default values of all the optional parameters are set to `None`. (0 points)

2. Create a tuple comprising of the following items. For the first item, create an f-string in the format`"Player 1: <variable_name>"`. If `player_2` is not `None`, add the f-string `"Player 2: <variable_name>"` as the second element and the f-string `"Mode: <variable_name>"` as third elements and save the tuple to `return_strs`. However, if `player_2` is `None`, add the f-string `"Mode: <variable_name>"` as the second element and save the tuple to `return_strs`.  (5 points)

:bulb: The following is the expected format of `return_strs`:

```python
# if <player_2> is not None:
    return_strs = (f"Player 1: {<variable_name>}",
    f"Player 2: {<variable_name>}",
    f"Mode: {<variable_name>}")

# if <player_2> is None:
    return_strs = (f"Player 1: {<variable_name>}",
    f"Mode: {<variable_name>}")

```

3. If the `mode` is `smash`, call the function `start_smash`. If present, the variables  `stage`, `game_type` are passed to this function. If the `mode` is `classic`, call the function `start_classic`. Pass the variable  `game_type` to this function if present. (15 points)

:bulb: You will need nested if statements, the outer if statements check for the game modes and the inner if statements check if the optional parameters are present. The following is the expected syntax (also called [pseudocode](https://www.sciencedirect.com/topics/engineering/pseudocode)):

```python
# if <mode> is 'smash':
    # if <game_type> is not None and <stage> is not None:
        make a function call to 'start_smash' and pass <stage> and <game_type> as arguments.

    # else if <stage> is not None and <game_type> is None:
        make a function call to 'start_smash' and pass <stage> as the only argument.

    # else if <game_type> is not None and <stage> is None:
        make a function call to 'start_smash' and pass <game_type> as the only argument.

    # else :
        make a function call to 'start_smash' without any arguments.

# else if <mode> is 'classic':
    # if <game_type> is not None:
        make a function call to 'start_classic' and pass <game_type>
        as the argument.
    # else:
        make a function call to 'start_classic' without any arguments.

```

4. The return value of this function is the tuple `return_value` concatenated (combined) with the return values from the function calls to `start_smash` or `start_classic`. (20 points)

:bulb: The return of the `select_match` can be sent along with the if conditionals and function calls described in problem 1 part 3. You only have to concatenate if there is a return value other than None. Also make sure you are combining two tuples together. You should create a tuple with a single item before concatenating it to `return_strs` if the return values from `start_smash` and `start_smash` are not tuples. Here is the pseudocode for this problem:

```python
    # if <mode> is 'smash':
        # if both <game_type> and <stage> are not None:
            function call
            return  <return_strs> + return from the function call

        # else if only <stage> is not None:
            function call
            create a new tuple with the returned value from the function call as the only item.
            return <return_strs>  + new tuple

        # else if only <game_type> is not None:
            function call
            create a new tuple with the returned value from the function call as the only item.
            return <return_strs>  + new tuple

        # else
            function call
            return only <return_strs>

    # else if <mode> is 'classic':
        # if <game_type> is not None:
            function call
            create a new tuple with the returned value from the function call as the only item.
            return <return_strs>  + new tuple

        # else:
            function call
            return only <return_strs>

```

## 3.0 Problem 3 (30 points)
A main function is defined with no parameters. The `main` function will serve as the entry point to the program and will orchestrate the program's workflow.

1. Test for the correct implementation of your `select_match`. Call the `select_match` function and pass the arguments `"Donkey Kong"` for `player_1`, `"smash"` for `mode`, `"Toon Link"` for `player_2`, `"Princess Peachess Castle"` for `stage` and `"Special Smash"` for `game_type` and assign the returned value to a variable named `match3`. If you print `match3` you should get a tuple with the follwing items: (5 points)
```
("Player 1: Donkey Kong", "Player 2: Toon Link", "Mode: smash", "Stage: Princess Peachess Castle", "Game Type: Special Smash")
```
2. Call the `select_match` function and pass the arguments `"Yoshi"` for `player_1`, `"smash"` for `mode` and `"Paper Mario"` for `stage`, and store the returned value to a list named `smash_bros_matches`. (5 points)

3. Call the `select_match` function and pass the arguments `"Sonic"` for `player_1`, `"smash"` for `mode`, `"Peach"` for `player_2` amd `"Smashville"` for `stage`, and append the returned value to the list `smash_bros_matches`. (5 points) 

4. Call the `select_match` function and pass the arguments `"Waluigi"` for `player_1`, `"smash"` for `mode`, `"Special Smash"` for `game_type` amd `"Smashville"` for `stage`, and append the returned value to the list `smash_bros_matches`

5. Call the `select_match` function and pass the arguments `"Zelda"` for `player_1`, `"classic"` for `mode` and `"training"` for `game_type` and append the returned value to the list `smash_bros_matches`. (5 points)

6. Call the `select_match` function and pass the arguments `"Kirby"` for `player_1`, `"classic"` for `mode` and `"King K. Rool"` for `player_2` and append the returned value to the list `smash_bros_matches`. (5 points)
