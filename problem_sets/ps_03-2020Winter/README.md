# SI 506: Problem Set 03

## This Week's Problem Set

This week's problem set includes five (5) problems that utilize your knowledge of for loops, indexing, slicing, and functions. Problems 1 and 2 review how slicing and for loops work. In Problems 3 and 4, you will build utility functions to perform specific tasks given the data available. In Problem 5, you will combine your skills to craft a `main()` function that will call the functions from Problems 3 and 4 in order to perform a useful analysis.

## Background

You will use a Video game console sales dataset based on: ([source](https://en.wikipedia.org/wiki/Video_game_console))

## 1.0 Problem 01 (20 Points)

### 1.1 SETUP

You will work with a list of Nintendo consoles for problems 1 and 2. The list contains an element for each Nintendo television console released followed by information on when that console was released. For example, the first element of the `nintendo_consoles` list describes the "Famicom/Nintendo Entertainment System" console which was released in 1983.

```python
nintendo_consoles = [
    "Famicom/Nintendo Entertainment System (NES), released: 1983",
    "Super Famicom/Super Nintendo Entertainment System (SNES), released: 1990",
    "Nintendo 64 (N64), released: 1996",
    "GameCube, released: 2001",
    "Wii, released: 2006",
    "Wii U, released: 2012",
    "Nintendo Switch, released: 2017"
    ]
```

Using the `nintendo_consoles` list and your knowledge of list slicing and indexing, create new list variables as directed. Each list should contain the entire strings from `nintendo_consoles` that meet the criteria described. You should not have to use any list concatenation methods or operators. Replace `pass` with your code.

### 1.2 Problem

1. `eighties_consoles` should include all the Nintendo consoles that were released from 1980 - 1989
2. `nineties_consoles` should include all the Nintendo consoles that were released from 1990 - 1999
3. `oughts_consoles` should include all the Nintendo consoles that were released from 2000 - 2009
4. `teens_consoles` should include all the Nintendo consoles that were released from 2010 - 2019

## 2.0 Problem 02 (20 Points)

 Using `nineties_consoles`, a for loop, and string/list methods, create a new list called `release_years` that contains all of the years in which Nintendo released a television-based video game console. The following is an example of what your `release_years` list should look like: [ "1983", "1990", ... etc. ]

## 3.0 Problem 03 (20 Points)

### 3.1 SETUP

For Problems 3, 4, and 5, you will be implementing loops, conditionals, and methods within the function stubs provided. You will be working with another video game console dataset, similar to `nintendo_consoles`, but expanded. The `vg_consoles` list contains data on the most popular video game consoles from each computing technological era (called "generations" in the dataset).

Each element of `vg_consoles` is a string with data separated by commas (you'll see this format of data storage again soon!) in the following order:\
Console name | Production company | Generation | Release year | Approx. # units sold

```python
vg_consoles = [
    "Odyssey,Magnavox,1st Generation,1972,100000",
    "Atari 2600,Atari,2nd Generation,1977,30000000",
    "ColecoVision,Coleco Industries,2nd Generation,1980,2000000",
    "Intellivision,Mattel Electronics,2nd Generation,1982,3000000",
    "Famicom/Nintendo Entertainment System (NES),Nintendo,3rd Generation,1983,61910000",
    "Master System,Sega,3rd Generation,1985,13000000",
    "Atari 7800,Atari,3rd Generation,1986,3770000",
    "Super Famicom/Super Nintendo Entertainment System (SNES),Nintendo,4th Generation,1990,49100000",
    "Mega Drive/Genesis,Sega,4th Generation,1988,30750000",
    "Saturn,Sega,5th Generation,1994,9260000",
    "PlayStation,Sony,5th Generation,1994,102490000",
    "Nintendo 64 (N64),Nintendo,5th Generation,1996,32930000",
    "Dreamcast,Sega,6th Generation,1998,9130000",
    "PlayStation 2,Sony,6th Generation,2000,155000000",
    "GameCube,Nintendo,6th Generation,2001,21740000",
    "Xbox,Microsoft,6th Generation,2001,24000000",
    "Xbox 360,Microsoft,7th Generation,2005,84700000",
    "PlayStation 3,Sony,7th Generation,2006,87400000",
    "Wii,Nintendo,7th Generation,2006,101630000",
    "Wii U,Nintendo,8th Generation,2012,13560000",
    "PlayStation 4,Sony,8th Generation,2013,102800000",
    "Xbox One,Microsoft,8th Generation,2013,46900000",
    "Nintendo Switch,Nintendo,9th Generation,2017,47300000"
    ]
```

### 3.2 Problem

Implement the `filter_by_units_sold()` function by replacing the `pass` statement with the appropriate code block. Read the function Docstring for additional implementation details.

:bulb: Use string methods to isolate the number of units sold, convert that number into an integer, and then perform your conditional operation.

## 4.0 Problem 04 (20 Points)

Implement the `format_string()` function by replacing the `pass` statement with the appropriate code block. Read the function Docstring for additional implementation details.

:bulb: f-strings will be helpful here.

## 5.0 Problem 05 (20 Points)

Implement the `main()` function by replacing the `pass` statement with the appropriate code block. Read the function Docstring for additional implementation details.

:bulb: You will need to call both `filter_by_units_sold()` and `format_string()` in this function. You will also need to use a for loop.
