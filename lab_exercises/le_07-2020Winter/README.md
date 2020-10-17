# SI 506: Lab Exercise 07

## This Week's Lab
This week's lab exercise will focus on working with files and prepare you for this week's problem set. You will find that several of the generic functions that you will construct in this lab are very similar to what you will be asked to do on the homework (some of the functions you will be able to directly copy and paste!). Thus is the power of functions!

## Background
You work for the US Department of Transportation. You are asked to determine the top TWO(2) highly trafficked cities determined by the number of passengers passing through their airports. You have been given a CSV file of highly trafficked airports (`airports.csv`) to help you.

Build a python script that will create an output file ` airports_ranked.csv ` of cities ranked in descending order by their number of travelers passing through their airports. Your output file should have the following headers:

```python
    < city >, < number of passengers >
```

As an example, the output file should contain the following rows:

```python
    Charlotte, 46444380
    Miami, 45044312
    Houston, 43807539
```

To accomplish this objective, build out the following stubbed functions. We have provided one
function for you ` sort_dictionary_by_value `. :warning: PLEASE DON'T CHANGE ANY CODE IN THIS FUNCTION! However, please read the docstring to understand how it works and what it is doing.

## 1.0 Problem 01 (5 Points)
Implement the `read_csv_file()` function.

This function takes one argument `input_filepath`, which is the path of the file to be read. You will need to use the `csv` module in this function. The format of the returned list of dictionaries is as follows:

```python
    [
        { < column 1 header >: < row 1 column 1 value >,
            < column 2 header >: < row 1 column 2 value >,
            < column 3 header >: < row 1 column 3 value >,
            ...etc
        },
        { < column 1 header >: < row 2 column 1 value >,
            < column 2 header >: < row 2 column 2 value >,
            < column 3 header >: < row 2 column 3 value >,
            ...etc
        },
        ...etc
    ]
```

As an example, if the input file were structured like so:

```python
    Name, Age, Animal Type
    Lex, 5, Dog
    Luke, 7, Cat
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

As a final example, if your input file were structured like so:

```python
    Airport, City, Passengers
    Charlotte Douglas International Airport, Charlotte, 46444380

    Then the returned list should be:
    [
        {
            "Airport": "Charlotte Douglas International Airport",
            "City": "Charlotte",
            "Passengers": "46444380"
        }
    ]
```

:exclamation: This is the most challenging part of this problem. You may want to consider using nested loops with enumerate statements. Don't worry about converting any strings to other types here; you can handle that later.

Replace the `pass` statement with the appropriate code block. Read the function Docstring for additional implementation details.

## 2.0 Problem 02 (5 Points)
Implement the `write_csv_file()` function.

Writes a .csv file using the `csv` module. The file will contain the information from `dict_to_write`, where each row of the new .csv file is one of the key/value pairs. In other words, the output file should have two columns. Don't forget to include the header to each column, which is given to this function in the parameter < header >. The resultant file should be structured in the following way:

```python
    < header[0] >, < header[1] >
    key1, value1
    key2, value2
    key3, value3
    ...etc
```

Replace the `pass` statement with the appropriate code block. Read the function Docstring for additional implementation details.

## 3.0 Problem 03 (5 Points)
Implement the `passengers_per_city()` function.

:exclamation: You may need to cast/transform string objects into integer objects prior to returning the value.

Replace the `pass` statement with the appropriate code block. Read the function Docstring for additional implementation details.

## 4.0 Problem 04 (5 Points)
Implement the `main()` function.

There are several steps to this section.
1. Read in the data from `airports.csv`.
2. Parse that data and determine the number of passengers per city using your `passengers_per_city` function.
3. Sort the resultant dictionary by number of passengers.
4. Write the sorted dictionary to a new file `airports_ranked.csv`. Don't forget to include headers that are tuples into the `airports_ranked.csv` file!

:exclamation: You will need to call each of the functions in this script to complete this task.

Replace the `pass` statement with the appropriate code block. Read the function Docstring for additional implementation details.
