# SI 506: Lab Exercise 04

## This Week's Lab
This week's lab exercise includes five (5) problems that focus on list indexing, list slicing, and function calls discussed in the lectures and the readings.

## Background
The mission of CAPS is to foster the psychological development and emotional well-being of students. If you or someone you know is feeling overwhelmed, depressed, and/or in need of support, services are available. For help, contact Counseling and Psychological Services (CAPS) at (734) 764-8312 and https://caps.umich.edu/ during and after hours, on weekends and holidays.

We provide you with a select list of Counseling And Psychological Services (CAPS) embedded staff members at different schools across the University of Michigan. In the future, the teaching team will provided you such data in a file which you will read into Python with some useful functions. However, for today, the teaching team has provided this list for you.

:exclamation: Replace `None` with your code for problems 1-3.

## 1.0 Problem 01 (Points 2.5)

### 1.1 SETUP

Each item in the `caps_staff` list is a string containing the name, the degree, the school, and email address of each CAPS staff member. Each data point relating to the staff member is separated by a pipe ("|") delimiter.

```python
caps_staff = [
    "Nidaa Shaikh|Psychologist|College of Engineering|nfkazi@umich.edu",
    "Laura Monschau|Psychologist|Rackham Gradate School|lauralm@umich.edu",
    "Meaghan Narula|Social Worker|School of Public Health|mbnarula@umich.edu",
    "Julie Kaplan|Social Worker|Ross School of Business|jrkaplan@umich.edu",
    "Alejandro Rojas|Social Worker|School of Social Work|aroja@umich.edu"
    ]
```

Extract the first staff member in `caps_staff` using their index value and assign them to a new variable named `nfkazi`.

## 2.0 Problem 02 (Points 2.5)

Extract the last staff member in `caps_staff` using their index value and assign them to a new variable named `aroja`.

## 3.0 Problem 03 (Points 5)

Use list slicing to extract the social workers from the list `caps_staff` and save the items to a new list called `social_workers`.

## 4.0 Problem 04 (Points 5)

Extract each CAPS staff member's name from the `caps_staff` list and append the extracted names to the list named `names_of_staff`. You can use loops, `str.split()` and list slicing to craft your solution.

:hint: Use print() statements to debug.

## 5.0 Problem 05 (Points 5)

Let's put everything you have learned about functions and lists together.

Implement the `thank_you_caps_staff()` function by replacing the `pass` statement with the appropriate code block. Read the function Docstring for additional implementation details.

:hint: Using for loops and an f-string will be helpful here.
:hint: Call your function to see if it prints all five messages.
