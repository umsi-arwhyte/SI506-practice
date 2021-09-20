# SI 506: Lab Exercise 05

## This week's Lab Exercise

This week's lab exercise includes three (4) problems that focus on building and applying functions.

## Data description

Each element in `record` is a string containing UMich team's win/loss record from 2000-2019.
Each element includes the year, number of wins, number of losses, win percentage, whether
the team has had a bowl appearance and if they had won that bowl.

## 1.0 Problem 01 (5 Points)

Write a function, `calculate_win_percentage`, to calculate win percentage, this function will
take wins and losses as parameters. This can be calculated as wins divided by total games. Round
this value to three decimal places.

:bulb: In North America, winning percentages are expressed as decimal values to three decimal places.
It is the same value, but without the last step of multiplying by 100% in the formula above.
Furthermore, they are usually read aloud as if they were whole numbers (e.g. 1.000, "a thousand" or
0.500, "five hundred"). In this case, the name "winning percentage" is actually a misnomer, since
it is not expressed as a percentage. A winning percentage such as .536 ("five thirty-six") expressed
as a percentage would be 53.6%. See https://en.wikipedia.org/wiki/Winning_percentage.

## 2.0 Problem 02 (5 Points)

Use `calculate_win_percentage` created in the previous problem to find the win percentage for each
element in `record`. Insert the win percentage into each record replacing `None` with the calculated
win percentage.

## 3.0 Problem 03 (5 Points)

Calculate the total wins and losses from 2000-2019 and find the win percentage for all years. Assign
the win percentage to  `record_win_percent`.

:bulb: loop over `record` and save the total wins to a variable named `record_wins` and the total losses to a variable named `record_losses`

## 4.0 Problem 04 (5 Points)

Write two functions to identify the best year and worst year. The function `calculate_best_year` will
find the year with the best win percentage and `calculate_worst_year` will find the year with the
worst win percentage. Assign the output of the best year to `best_year` and the output for worst
year to `worst_year`.

:bulb: If there is a tie between two years, consider looking at factors other than win percentage to
break the tie.