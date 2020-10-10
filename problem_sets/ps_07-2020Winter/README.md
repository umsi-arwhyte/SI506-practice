# SI 506: Problem Set 07

## Background

This week, we will be working with the *coolest* part of Python: Classes! You will need to utilize two different input files, `sh_basic_info.csv` and `sh_additional_info.csv`, to gather information on three super-powered women from the Marvel universe. You will build a class with which to organize this information, and then use that class to do specific data manipulation for each heroine. The skeleton code file, `problem_set_07.py`, contains areas that need your work, which are demarcated by `pass`.

## 1.0 Problem 01 (24 Points)

Implement the constructor, `__init__()`, of the `Superheroine` class.

The constructor will take the following arguments:

* `self`
* `name`
* `full_name`
* `team`
* `eye_color`
* `hair_color`
* `base`

and assign each to an instance variable of the same name. In addition, the constructor should create two instance variables `self.powers` and `self.nemeses`, and assigning to each an empty list as the value. We'll change that later in the `add_power()` and `add_nemesis()` methods.

Instance Variables:

* `name` (str): The (superheroine) name of the heroine.
* `full_name` (str): The (given) name of the heroine.
* `team` (str): The team (if any) the heroine is a part of.
* `eye_color` (str): The eye color of the heroine.
* `hair_color` (str): The hair color of the heroine.
* `base` (str): The base of operations of the heroine.
* `powers` (list): The powers of the heroine.
* `nemeses` (list): The nemeses of the heroine.

Replace the `pass` statements with the appropriate code blocks. Read the class and method Docstrings for additional implementation details.

## 2.0 Problem 02 (24 Points)

Implement the `__str__()` method of the `Superheroine` class.

The return value must adhere to the following format:
```
< name > is a member of the < team > and possesses the following powers:\n< powers >
```

If an instance of the Superheroine class is made with the arguments:

* `name` = "Storm"
* `full_name` = "Ororo Munroe"
* `team` = "X-men"
* `eye_color` = "Blue"
* `hair_color` = "White"
* `base` = "Xavier Institute"

and the string method is called, it should return the following:

```
Storm is a member of the X-men and possesses the following powers:
< power a >, < power b >, < power c > . . .
```

:bulb: If using a formatted string literal (f-string) to format the text don't forget to use curly braces { < variable > } to indicate use of a variable in the expression.\
:bulb: Make sure the there is a new line character (`\n`) after the colon ':'.

## 3.0 Problem 03 (24 Points)

Implement the `add_power()` method of the `Superheroine` class by replacing the `pass` statement with the appropriate code block. Read the function Docstring for additional implementation details.

## 4.0 Problem 04 (24 Points)

Implement the `add_nemesis()` method of the `Superheroine` class by replacing the `pass` statement with the appropriate code block. Read the function Docstring for additional implementation details.

## 5.0 Problem 05 (24 Points)

Implement the `write_to_file()` function by replacing the `pass` statement with the appropriate code block. Read the function Docstring for additional implementation details.

## 6.0 Problem 06 (30 Points)

Implement `main()` following the hints provided below.

### 6.1 Read in `sh_basic_info.csv`

Read in the `sh_basic_info.csv` file using your `read_csv_file()` function. Save the returned list to `basic_info`. Each item in `basic_info` should be a dictionary describing one of the heroines in the data set.

### 6.2 Create instances of `SuperHeroine`

There are several steps to this section.
1. Create an empty dictionary called `heroines`.
2. Loop through the `basic_info` list and create an instance of `SuperHeroine` for each item in `basic_info`.
3. Within that loop, create a new key/value pair in `heroines` for each instance of `SuperHeroine` that you create. Make the key be the `name` of that heroine, and the value be the instance of `SuperHeroine` you created.
4. Print out `heroines`. If done correctly, it should look something like this (except that your memory addresses will be different):

    ```python
    {
    'Storm': <__main__.SuperHeroine object at 0x100b6d2e8>,
    'Scarlet Witch': <__main__.SuperHeroine object at 0x100b6d240>,
    'Jessica Jones': <__main__.SuperHeroine object at 0x100b6d208>
    }
    ```

### 6.3 Read in `sh_additional_info.csv`

Read the `sh_additional_info.csv` file using your `read_csv_file()` function. Save the returned list to the variable `additional_info`.

### 6.4 Add powers and nemesis

Loop through the lines from `sh_additional_info.csv` file (which are now stored in `additional_info`) and do the following:
1. Save the value associated with the "Heroine Name" key from each row of `additional_info` to a new variable.
2. Use that new variable as the key to retrieve the correct instance from `heroines` and save that instance to a new variable `instance_affected`
3. Save the values associated with the "Category" and "Value" keys from each row of `additional_info` to their own variables.
4. Create a conditional (`if`) statement that checks whether the "Category" variable is a 'power' or 'nemesis'.
5. Call the proper method (either `add_power()` or `add_nemesis()`) on the `instance_affected` variable.

### 6.5 Write to file

Call your `write_to_file()` function three times:
1. Encode the `storm` object as text and write it to a file named `storm.txt`.
2. Encode the `scarlet_witch` object as text and write it to a file named `scarlet_witch.txt`.
3. Encode the `jessica_jones` object as text and write it to a file named `jessica_jones.txt`.
