# SI 506: Lab Exercise 10

## This Week's Lab

This week's lab focuses on interacting with the SWAPI api using the requests module.

## 1.0 Problem 01 (5 Points)

In this problem you will demonstrate your understanding of the requests module by:
1. Making a request
2. Encoding the response as a JSON object

Implement the `get_people()` function by replacing the `pass` statement with the appropriate code block. Read the function Docstring for additional implementation details.

:bulb: `requests.get(url, params).json()` returns a decoded JSON object that contains a "results" list property with a maximum of 10 records per request. Use the "results" key to index the dictionary representation of the decoded JSON to access the resource(s) matched by the search query return.

## 2.0 Problem 02 (5 Points)

In this problem, you will demonstrate your understanding of:
1. working with conditional statements
2. working with dictionaries
3. working with for loops

Implement the `filter_properties()` function by replacing the `pass` statement with the appropriate code block. Read the function Docstring for additional implementation details.

## 3.0 Problem 03 (5 Points)

In this problem, you will demonstrate your ability to write data to a JSON file.

Implement the `write_json()` function by replacing the `pass` statement with the appropriate code block. Read the function Docstring for additional implementation details.

:bulb: for the `open()` parameters, use `encoding='utf-8'` and for the json.dump parameters, use `ensure_ascii=False`, `indent=2`.

## 4.0 Problem 04 (5 Points)

Implement the `main()` function following the hints provided below.

1. Call the `get_people()` function to make a request to the SWAPI endpoint to get a list of dictionaries representing people. Assign the dictionary to a variable named `people`. Use the search parameter to only return people that have "Skywalker" in their name.
2. Loop over `people` and for each dictionary encountered in the list call `filter_properties()` to get a new record of each person listed in `people`.
3. Append the new record to an accumulator list.
4. Write result of the filtering operation to a file called `swapi_people.json`.
