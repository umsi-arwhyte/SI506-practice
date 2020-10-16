# SI 506: Lab Exercise 03

## This Week's Lab

This week's lab exercise includes three (3) problems that focus on creating lists, accessing and manipulating
list items, and iterating over a list using a `for` loop.

# Background:

Each item in the `umsi_faculty` list is a string containing the name, title, and email address of
the faculty member. Each piece of information relating to the faculty member is separated by a
pipe ('|') delimiter.

```python
umsi_faculty = ["Charles Severance|Clinical Professor of Information|csev@umich.edu",
                "Colleen Van Lent|Lecturer|collemc@umich.edu",
                "Chris Teplovs|Lecturer|cteplovs@umich.edu",
                "Anthony Whyte|Lecturer|arwhyte@umich.edu",
                "Christopher Brooks|Research Assistant Professor|brooksch@umich.edu"]
```

## 1.0 PROBLEM 01 (10 POINTS)

### 1.0 Setup

We provide you with a select list of UMSI faculty. In the future, such data
will be provided in a file which you will read into Python with some useful functions. However,
for today, the teaching team has provided this list for you to use.

### 1.1 Problem

Extract the second element in `umsi_faculty` using its index value and assign it to a new
variable named `collemc`.

### 1.2 Problem

Extract the last element in `umsi_faculty` using its index value and assign it to a new
 variable named `brookcsh`.

## 2.0 PROBLEM (5 POINTS)

Use list slicing to extract the 2nd, 3rd and 4th elements from the list `umsi_faculty` and save
the elements to a new list called `lecturers`.


## 3.0 PROBLEM (10 POINTS)

### 3.1 Problem

Extract each faculty member's email address from the `umsi_faculty` list and append the
extracted email address to the list named `email_addresses`.

Hint : You can use loops, `str.split()`, and list slicing to craft your solution. Use `print()` statements to debug.

### 3.2 Problem

1. Using an `if` statement, check the length of each email address in the list.

2. If the length of the email address is greater than ('>') 15 characters, extract the
email address and append it to a new list called `long_email_addresses`.


## End Problem Solution