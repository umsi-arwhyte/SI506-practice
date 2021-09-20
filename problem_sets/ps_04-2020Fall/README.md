# SI 506: Problem Set 04

## This week's Problem Set

This Problem Set focuses on built-in methods, slicing, loops and conditional statements.

## Background

Scrambled eggs is a dish made from eggs (usually chicken eggs) stirred or beaten together in a pan while being gently heated, typically with salt, butter and sometimes other ingredients ([wiki](https://en.wikipedia.org/wiki/Scrambled_eggs)).

Today we'll be working a recipe adapted from [How to Scramble Eggs: A Step-by-Step Guide](https://www.foodnetwork.com/how-to/articles/how-to-scramble-eggs-a-step-by-step-guide).

## Set up

`summary` is a list of strings and every string summarizes each step.
`recipe` is a list of strings and every string describes a specific step for making scrambled eggs.

## 1.0 Problem 01 (30 Points)

1. Create an empty list `step_length`. Loop over every step in `recipe`, count the length of each step in terms of characters and append the length to `step_length`.

    :bulb: Space `' '`, single quote `'` etc are all valid characters

2. Loop over `step_length`, count the number of steps with a length greater than (`>`) 100 and assign the values to the variable `gte_100` and count the number of steps with a length less than (`<`) 100 and assign the values to the variable `less_100`

3. If a step with a length greater than 100 would take 10 minutes and a step with a length less than 100 would take 5 minutes, how many minutes in total does it take to complete steps 2-5? Assign the total number of minutes to the variable `step_25_mins`
   :bulb: In order to pass the autograder, you must use loops to solve this question.

## 2.0 Problem 02 (30 Points)

1. Use string methods to generate the formatted step order `'STEP3'` from its original step summary `'Step 3: Add the Eggs'`. Assign the generated string to the variable `step_order_3`

2. Use an f-string to concatenate the step order of step3 and the step details of step3 in recipe per the following format: `'{step_order}: {step_detail}'`. For step3, the expected answer should be `"STEP3: Then, pour in the eggs. Pause to let them heat slightly — gentle heat is essential."`. Assign the concatenated string to the variable `recipe_summary_3`

3. Create an empty list `recipe_summary`. Now expand the operation of Problem 2.2 to every step of this recipe and append the concatenated string to the list `recipe_summary`
    :bulb: You can either use the built-in function `enumerate()` or loop on the list index

## 3.0 Problem 03 (40 Points)

1. Count the occurrence of the character `'r'` in the second element of `recipe` and assign the value to the variable `step2_r_num`

    :bulb: Loop over the string and check whether the value of the character is equal to `'r'`. If so, increase the count.

2. Create an empty list `step_r_num`. Now expand the operation of Problem 3.1 to every step in `recipe` using loop and append the occurrence of the character `'r'` in every step to the list `step_r_num`

3. Loop over `step_r_num`, find the step that has the maximum occurrence. Assign its index to the variable `max_r_index` and assign the maximum occurrence to the variable `max_r_num`.