# SI 506: Lab Exercise 11

#### This Week's Lab

The following lab exercise will allow you to work more with the SWAPI endpoint to get you comfortable with using 
the requests module as you work on your final assignment. This week, we are focusing on SWAPI Planet data.
We will be learning about classes, dictionary and list comprehensions.

If a problem has a set-up, do NOT modify, delete, or ignore the set-up code.

## PROBLEM 01 (2.5 Points)

In this problem you will:

1. Create a class
2. Initialize it

Create a class named `Planet` and initialize it.

## PROBLEM 02 (10 Points)

In this problem you will:
1. Create a GET request
2. Parse JSON and work with keys and values
3. Use list comprehension

Send a GET request to SWAPI using `{'search': name}` as params
and store it as dictionary.

Use the "results" key and index the dictionary representation of the decoded JSON to access the resource(s) matched by the search query return.
Store this as `result`
:bulb: response['results'][0]
:bulb: convert your response to JSON object using `response.json()`

Using list comprehension, find the values from `result` and store them in a list named `planet_props`

Create an instance of `Planet` and pass `planet_prop` list elements as arguments using the `*` operator as a 
variable args call and return the instance.

:bulb: Planet(*planet_props)

## PROBLEM 03 (2.5 Points)

In this problem you will
1. Write data to a JSON file

:bulb: for the `open()` parameters, use `encoding= 'utf-8'` and for the
`json.dump()` parameters, use `ensure_ascii= False`, `indent=2`.

## PROBLEM 04 (5 Points)

In this problem you will:

1. Use Dictionary comprehension
2. Call other functions

Use dictionary comprehension to return a dictionary comprising a set of { key < planet name > (str): value < planet > (dict)} key-value pairs. Iterate over the planet names stored in the `PLANETS` list to obtain the keys; call the `get_planets(name)` function to return the value of each key. Assign the new dictionary to the variable named `planets_data`. Call the `jsonable()` method on your planet instance in order to return a dictionary representation of the object. Write `planets_data` to a file named "swapi_planets.json" by calling the `write_json()` function.
