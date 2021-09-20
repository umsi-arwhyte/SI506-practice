# SI 506: Problem Set 02

## This week's Problem Set

This week's problem set focuses on sequence indexing, list methods, string methods and formatting
values as strings using a formatted string literal (f-string).

## Background

How many Coronavirus tests have been conducted? How many positive cases have been reported? In this
problem set, we'll use data from the [COVID-19 Dashboard](https://campusblueprint.umich.edu/dashboard/)
to get a better idea of how Covid-19 has been handled on campus.

## 1.0 Problem 01 (20 points)

In the last five weeks (from 08/09 - 09/06), UM has reported **11, 10, 38, 19, 27** positive cases
weekly. We provide a list of positive cases named `cases`.

1. Use list indexing to return the latest positive case number in `cases` and assign it to a variable
   named `cases_latest`.

2. Assume an error exists in the data. The first element of `cases` is actually **9** instead of
   **11**. Please update the list with correct value using list indexing.

## 2.0 Problem 02 (20 points)

In the last five weeks (from 08/09 - 09/06), UM has conducted **867, 854, 1494, 1712, 1667** tests
weekly.

1. Create an empty list named `tests`. Append the weekly test numbers to `tests` in chronological
   order.

2. What's the maximum value in `tests`? Assign the maximum value to a variable named `tests_max`.

   :bulb: You can use the built-in function `max()` to get the max value.

3. What's the maximum value's index in `tests`? Assign the maximum value's index to a variable
   named `tests_max_index`.

   :bulb: You can use the list method  `list.index()` to get the index value.

## 3.0 Problem 03 (20 points)

We provide a string named `weeks` with weekly start date of last five weeks separated by comma `,`
for you. Note, that at the start and the end of `weeks` there are two spaces.

Use the string methods (`str.replace()`, `str.split()`, `str.strip()`) to create a list of strings
that matches the list `['Aug09', 'Aug16', 'Aug23', 'Aug30', 'Sep06']`. Assign the list of strings to
a variable named `week_list`.

## 4.0 Problem 04 (20 points)

In this problem, you will use the `weeks_list` that you created in problem 03.

1. Use the `str.join()` method on `weeks_list` to generate a new string `weeks_new` where the
   start date of each week is separated by a pipe symbol (`|`). In other words, the value assigned
   to `weeks_new` _must_ match the string `'Aug09|Aug16|Aug23|Aug30|Sep06'`.

2. Use the `str.count()` method on `weeks_new` to return a count of weekly start dates in August.
   Assign the value to a variable named `aug_count`.

## 5.0 Problem 05 (20 points)

1. Use a formatted string literal (f-string) to generate a string named `most_tests` that summarizes
   the weekly start date, number of tests performed, and number of positive cases detected for the week that saw the highest number of tests conducted over the last five weeks.

   The value assigned to `most_tests` _must_ implement the following text format:

    ```commandline
    In the week starting on < date >, UM has conducted < test_num > tests and reported < case_num > cases.
    ```

    :exclamation: Use of `< some_var >` indicates that a variable expression is to be inserted into the
    string.

   :bulb: `date` is an element of `week_list`, `test_num` is an element of `tests`, while `case_num`
   is an element of `cases`.

2. Similarly, use a formatted string literal (f-string) to generate the string `most_cases` that
   summarize the weekly start date, number of tests performed, and number of positive cases detected
   for the week that saw the highest number of positive cases reported over the last five weeks. Use
   the same text format as described above in problem 5.1.
