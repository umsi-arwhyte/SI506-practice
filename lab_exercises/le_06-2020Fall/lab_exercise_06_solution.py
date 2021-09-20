# START LAB EXERCISE 06
print('Lab Exercise 06 \n')

#SETUP
mario_kart_game = [
('Peach', 49), ('Mario', 35), ('Yoshi', 23),
('Wario', 20), ('Daisy', 18), ('Luigi', 10)
]

# END SETUP

# PROBLEM 1 (5 points)
def scores(game):
    team_one_score = game[0][1] + game[1][1] + game[2][1]
    team_two_score = game[3][1] + game[4][1] + game[5][1]
    return team_one_score, team_two_score

# PROBLEM 2 (5 points)
def blue_shell(game):
    game.insert(2, game.pop(0))
    return game

# PROBLEM 3 (5 points)
# SETUP
new_mario_kart_game = [
('Donkey Kong', 45), ('Mario', 30), ('Yoshi', 22),
('Wario', 20), ('Toad', 18), ('Peach', 15)
]

# END SETUP

# PROBLEM 4 (5 points)

def top_three(game):
    return [player[0] for player in game[:3]]

# main()
def main():
    # Call < scores() > and assign to < team_scores >
    team_scores = scores(mario_kart_game)
    print(f'Scores: {team_scores}')

    # Call < blue_shell() > and assign to < blue_shell_players >
    blue_shell_players = blue_shell(mario_kart_game)
    print(f'Player positions after blue shell: {blue_shell_players}')

    # Insert the new character tuple as the first element of < new_mario_kart_game >
    player = ('Bowser', 60)
    new_mario_kart_game.insert(0, player)
    print(f'Updated new game: {new_mario_kart_game}')

    # Call < top_three() > and assign to < top_three_players >
    top_three_players = top_three(new_mario_kart_game)
    print(f'Top three players: {top_three_players}')

    # END LAB EXERCISE

if __name__ == '__main__':
    main()