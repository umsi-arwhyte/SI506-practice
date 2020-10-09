# SI 506: Problem Set 04

## This Week's Problem Set

In this homework, you'll work with data from 2016 Summer Olympics. With these data we will code with dictionaries, looping, conditional statements, functions, and string processing.

## PROBLEM 1.0 (10 points)

###  SETUP
Below are `key,value` pairs providing information on the gymnast, Simone Biles.

```python
 KEY           VALUE
 "athlete"     Simone Biles
 "sport"       gymnastics
 "born"        1997
 "age"         # Make this the difference between the birth year
               # and the current year.You MUST do this
               # programmatically (i.e. using math operators),
               # not just writing in one number.
```

### 1.1 Assign `key,value` pairs to the < simone_biles > dictionary

Encode the following `key-value` pairs containing information about the gymnast Simone Biles into a dictionary object. Name the dictionary `simone_biles`.

:exclamation: For the value paried with the "age" key, you must do this programmatically (i.e. using math operators) and not by inputting a single number.

## PROBLEM 2.0 (10 points)

### SETUP

The `golds` dictionary contains all of the nations that obtained at least 5 gold medals in the 2016 Summer Olympics.
```python
golds = {
    "USA" : 46,
    "GBR" : 27,
    "CHN" : 26,
    "RUS" : 19,
    "GER" : 17,
    "JPN" : 12,
    "FRA" : 10,
    "KOR" : 9,
    "ITA" : 8,
    "AUS" : 8,
    "NED" : 8,
    "HUN" : 8,
    "BRA" : 7,
    "ESP" : 7,
    "KEN" : 6,
    "JAM" : 6,
    "CRO" : 5,
    "CUB" : 5
}
```

### 2.1 Assign the sum of values to 'medal_count'

Encode the sum counts of all of the medals and save that value to the variable `medal_count`.

## SETUP for PROBLEMS 3.0, 4.0, 5.0, and 6.0:

In the next four problems, you will work with the poem "Laurel of Hellas" by Aale Tynni in 1948. This poem was awarded the last gold medal for literature in the offical Olympic program.
 The text of this poem has been saved as the variable `laurel_of_hellas`.\
\
Use the starter code in Problems 3.0 and 4.0 to build functions, and then create the
`main()` function as described in Problem 5.0. In Problem 6.0 you will implement the `main()` function.

:warning: Test all of your functions regularly by calling them and using print statements.

## PROBLEM 3.0 (20 points)

### 3.1 Implement the `process_string()` function

Implement the `process_string()` function by replacing the `pass` statement with the appropriate code block. Read the function Docstring for additional implementation details.

:hint: For convenience, we have provided a list of the punctuation that you need to remove.

:exclamation: Update your parameters!

## PROBLEM 4.0 (20 points)

### 4.1 Implement the 'word_frequency()` function

Implement the `word_frequency()` function by replacing the `pass` statement with the appropriate code block. Read the function Docstring for additional implementation details.

:hint: For the purposes of this assignment, the returned object from
`process_string()` function should work here.

:exclamation: Update your parameters!

An example of this function:

```python
[input]:
word_frequency(["to", "be", "or", "not", "to", "be"])

[output]:
{"to" : 2, "be" : 2, "or" : 1, "not" : 1}
```

## PROBLEM 5.0 (20 points)

### 5.1 Implement the 'find_common_words()` function

Implement the `find_common_words()` function by replacing the `pass` statement with the appropriate code block. Read the function Docstring for additional implementation details.

:exclamation: Update your parameters!

## PROBLEM 6.0 (20 points)

### 6.1 Implement the `main()` function

This is the main operator of the script. Implement the `main()` function by replacing the `pass` statement with the appropriate code block. Read the function Docstring for additional implementation details.

:hint: If you have coded the utility functions from Problems 3.0, 4.0, and 5.0 correctly, the `main()` function should only be 4-5 lines of code.

:hint: Note that the `main()` function is called at the end of the script, so you will not call the `main()` function on your own.

:exclamation: Update your parameters!
