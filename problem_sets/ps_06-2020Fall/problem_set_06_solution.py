# START PROBLEM SET O6
print('Problem Set 06')

# Problem 01
print('\nProblem 01')

def start_classic(game_type=None):
    """Provides information to start the game in smash mode. The function takes the parameters to
    set the game type. It checks whether an argument was passed to the parameter and returns an
    f-string based on the parameters passed.

        Parameters:
            game_type (str): contains information about the type of game (optional).

        Returns:
            str: formatted string that returns information about the type of game based on the
                 parameter < game_type >; otherwise returns None.
    """

    if game_type:
        return f"Game Type: {game_type}"
    else:
        return None

def start_smash(stage=None, game_type=None):
    """Provides information to start the game in smash mode. The function takes the parameters to
    set the stage and game type. It checks whether any arguments were passed to these parameters
    and returns an f-string based on the parameters passed.

        Parameters:
            stage (str): contains information about the location of the match (optional).
            game_type (str): contains information about the type of the game (optional).

        Returns:
            tuple: contains f-string items with information about information about both the location
                   of the match based on the paramter <stage> and the type of game based on the
                   parameter < game_type >.
            str: a formatted string concatenating information about the match is returned instead
                 of a tuple if only one of the parameters is passed.
            None: If the value for both the parameters is None, a None is returned.
    """

    if stage and game_type:
        return (f"Stage: {stage}", f"Game Type: {game_type}")
    elif game_type:
        return f"Game Type: {game_type}"
    elif stage:
        return f"Stage: {stage}"
    else:
        return None

# Problem 02
print('\nProblem 02')

def select_match(player_1, mode, player_2=None, game_type=None, stage=None):
    """This function calls the appropriate function based on the game mode and passes the arguments
       if they are provided. It returns a tuple with character names, game modes and returned values
       from function calls.

        Parameters:
            player_1 (str): character name of player 1.
            mode (str): mode of the match which can either be 'classic' or 'smash'.
            player_2 (str): contains the character name of player 2 if a name is given (optional).
            stage(str): contains the name of the location for the match.
            game_type(str): contains information about the game type (optional).

        Returns:
            tuple: A tuple with formatted strings that contains player 1 name and game mode and
                   information about other optional parameters.
    """

    if player_2:
        return_strs = (f"Player 1: {player_1}", f"Player 2: {player_2}", f"Mode: {mode}")
    else:
        return_strs = (f"Player 1: {player_1}", f"Mode: {mode}")

    if mode == "smash":
        if stage and game_type:
            return return_strs + start_smash(stage, game_type)
        elif stage:
            return return_strs + (start_smash(stage),)
        elif game_type:
            return return_strs + (start_smash(game_type=game_type),)
        else:
            start_smash()
            return return_strs
    elif mode == "classic":
        if game_type:
            return return_strs + (start_classic(game_type),)
        else:
            start_classic()
            return return_strs


# Problem 03
print('\nProblem 03')

def main():
    """The main() function serves as the entry point to the program. It makes calls to the
    < select_match > function and passes the required parameters. Recieves the return value from
    the function calls.

        Parameters:
            None

        Returns:
            tuple: A tuple that contains the variable match1, match2, match3 and the list smash_bros_brothers that contain
            all the returned values from the function calls.
    """

    match1 = start_smash("Mushroomy Kingdom")
    match2 = start_classic("training")
    match3 = select_match("Donkey Kong", "smash", "Toon Link", "Special Smash", "Princess Peachess Castle")

    smash_bros_matches = [select_match("Yoshi", "smash", stage="Paper Mario")]
    smash_bros_matches.append(select_match("Sonic", "smash", "Peach", stage="Smashville"))
    smash_bros_matches.append(select_match("Waluigi", "smash", game_type="Special Smash", stage="Smashville"))
    smash_bros_matches.append(select_match("Zelda", "classic", game_type="training"))
    smash_bros_matches.append(select_match("Kirby", "classic", "King K. Rool"))

    print(match1)
    print(match2)
    print(match3)
    print(smash_bros_matches)


# SETUP
    return match1, match2, match3, smash_bros_matches

match1, match2, match3, smash_bros_matches = main()

# END SETUP

# END PROBLEM SET
