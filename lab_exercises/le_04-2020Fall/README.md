# SI 506: Lab Exercise 04

## This week's Lab Exercise

This week's lab exercise includes three (3) problems that focus on loops
and conditional statements.

## Background
We provide you with a select list of cities and states in the U.S. In the future, such data
will be provided in a file which you will read into Python with some useful functions. However,
for today, the teaching team has provided this list for you to use.

# Data description:

Each element in the `city_state` list is a string containing cities and their corresponding state.

city_state = ["Detroit|MI", "Philadelphia|PA", "Hollywood|CA",
            "Oakland|CA", "Boston|MA", "Atlanta|GA",
            "Phoenix|AZ", "Birmingham|AL", "Houston|TX", "Tampa|FL"]

## 1.0 Problem 01 (5 Points).

Use list slicing to extract the 3rd and 4th elements from the city list
then save the elements to a new list called `cali`.

## 2.0 Problem 02 (5 Points).

Extract each city from the `city_state` list and append the extracted cities to the new list named `us_cities`.

:bulb: Considered using a for loop. Try the built-in `split()` function and split on the delimiter.

## 3.0 Problem 03 (10 Points).

 Use the elements from the `us_cities` list to return the index of each element. As you loop over `us_cities` return the index value of each city encountered and assign it to a local variable named `index`. Write an `if` conditional statement inside the loop that tests if the current index value is greater than 4. If the expression evaluates to True, append the city to a new list named `southern_cities`.
