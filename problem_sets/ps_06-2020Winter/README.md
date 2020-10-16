# SI 506: Problem Set 06

## This Week's Problem Set

This week's problem set will have you build a function-first python script. You will build out
four utility functions (an additional one will be provided), and then call them all in the
correct order in a `main()` function in order to solve a task. Note that the functions you build
in this assignment may be useful in future assignments, particularly the `read_csv()` and
`write_csv()` functions.

## Background

You have been asked to determine which US state has the largest area of national parks, given
a CSV file ("parks.csv") that contains information on all of the national parks in the US.
Build a python script that will create an output file ("parkarea.csv") that contains rows
in the following format:

<state two-letter identifier>,<area of national parks in km^2 contained in that state>

As an example, the output file should contain the following rows:

```python
MI,2287.16
TN,2085.96
CO,1575.536
```

To accomplish this task, build out the following stubbed functions. We have provided one function
for you `sort_dictionary_by_value()`.

:warning: PLEASE DO NOT CHANGE ANY CODE IN THIS FUNCTION, however, please read the docstring to
understand how it works and what it is doing!

## 1.0 PROBLEM 01 (40 Points)

Implement `read_csv_file()` replacing the `pass` statement with the appropriate code block. Read
the function Docstring for additional implementation details.

The format of the returned list of dictionaries is as follows:

```python
        [
            { <column 1 header>: <row 1 column 1 value>,
              <column 2 header>: <row 1 column 2 value>,
              <column 3 header>: <row 1 column 3 value>,
              ...etc
            },

            { <column 1 header>: <row 2 column 1 value>,
              <column 2 header>: <row 2 column 2 value>,
              <column 3 header>: <row 2 column 3 value>,
              ...etc
            },

            ...etc
        ]
```

As an example, if the input file is structured as the following:

```python
    Name,Age,Animal Type
    Lex,5,Dog
    Luke,7,Cat
```

Then the returned list would be:

```python
    [
        {
            "Name": "Lex",
            "Age": "5",
            "Animal Type": "Dog"
        },
        {
            "Name": "Luke",
            "Age": "7",
            "Animal Type": "Cat"
        }
    ]
```

As a final example, if your input file was structured like so:

Park Code,Park Name,State,Acres,Latitude,Longitude
ACAD,Acadia National Park,ME,47390,44.35,-68.21

Then the returned list should be:

```python
    [
        {
            "Park Code": "ACAD",
            "Park Name": "Acadia National Park",
            "State": "ME",
            "Acres": "47390",
            "Latitude": "44.35",
            "Longitude": "-68.21"
        }
    ]
```

:hint: This is the most challenging part of this problem. You may want to consider using nested
loops with enumerate statements.

## 2.0 PROBLEM 02 (15 Points)

Implement `write_csv_file()` replacing the `pass` statement with the appropriate code block. Read
the function Docstring for additional implementation details.

Don't forget to include the header to each column, which is given to this function in the parameter
< header >. The resultant file should be structured in the following way:

```python
        < header[0] >,< header[1] >
        key1,value1
        key2,value2
        key3,value3
        ...etc
```

## 3.0 PROBLEM 03 (15 Points)

Implement `acres_to_km2()` replacing the `pass` statement with the appropriate code block. Read the
function Docstring for additional implementation details.

## 4.0 PROBLEM 04 (15 Points)

Implement `km2_by_state()` replacing the `pass` statement with the appropriate code block. Read the
function Docstring for additional implementation details.

NOTE: Don't worry about states that don't have any national parks in the dataset we have provided.
Your returned dictionary should only include the states that are present in the data.

:hint: You'll need to use an accumulator pattern here to build a new dictionary. You will also need
to call `acres_to_km2` to convert the park areas into km^2.

## 5.0 PROBLEM 05 (15 Points)

Implement `main()` replacing the `pass` statement with the appropriate code block. Read the function
Docstring for additional implementation details.

:warning: Don't forget to include headers into the `parkarea.csv` file!

:hint: You will need to call each of the functions in this script to complete this task.
