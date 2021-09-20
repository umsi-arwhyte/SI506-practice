# SI 506: Lab Exercise 10

#### This Week's Lab

The following lab exercise will allow you to work more with SWAPI to get you
comfortable with using requests module. This week we are retrieving information on the
Star Wars character, Leia Organa, from SWAPI.

Leia Organa was a Force-sensitive human female political and military leader who served in the Alliance to Restore the Republic during the Imperial Era and the New Republic and Resistance in the subsequent New Republic Era.

<<<<<<< HEAD
Source: https://starwars.fandom.com/
=======
Source: https://starwars.fandom.com/wiki/Leia_Skywalker_Organa_Solo
>>>>>>> 20abd03487f7c92a347cb5d7c560cfdc3ecf11be

## PROBLEM 01 (2.5 Points)

In this problem you will implement `get_resource()` by:
1. Create a GET request
2. Parse JSON and work with keys and values

Send a GET request to SWAPI using `{'search': name}` as params
and store it as dictionary.

<<<<<<< HEAD
Use the "results" key and index the dictionary representation of the decoded JSON to access the resource(s) matched by the search query return.
Store this as `result`

:bulb: response['results'][0]
:bulb: convert your response to JSON object using `response.json()`

=======
>>>>>>> 20abd03487f7c92a347cb5d7c560cfdc3ecf11be
## PROBLEM 02 (10 Points)

In this problem you will create a constructor for the `Person` class and initialize it and initialize it's variables.

Instance Variables:
* `name` (string): Name of the Star Wars character.
* `hair_color` (string): Star Wars character's hair color.
* `eye_color` (string): Star Wars character's eye color.
* `species` (string): Name of the species of the Star Wars character.

Implement `jsonable()`. This method returns a JSON-friendly representation of the object.
<<<<<<< HEAD
Use a dictionary literal rather than built-in dict() to avoid built-in lookup costs.
=======
Use a dictionary literal rather than built-in dict() to avoid built-in lookup costs. 

A dictionary literal is created by surrounding key/value pairs with curly braces (`{}`) like so:

```python
    dict = {
        'one': 1,
        'two': 2,
    }
```
>>>>>>> 20abd03487f7c92a347cb5d7c560cfdc3ecf11be

Implement `__str__()`. This method will return only the name of the character.

## PROBLEM 03 (2.5 Points)

In this problem you will implement `write_json()`. This function takes in a filepath and data to write to the filepath.

:bulb: for the `open()` parameters, use `encoding= 'utf-8'` and for the
`json.dump()` parameters, use `ensure_ascii= False`, `indent=2`.

## PROBLEM 04 (10 Points)

In this problem you will implement `main()`:

<<<<<<< HEAD
1. Call `get_resource()` with the correct parameters. Since we are retrieving information on Leia, you will pass to the function a dictionary comprising a single key-value pair: `{'search: 'leia'}`. Save the results to `leia_data`.
=======
1. Call `get_resource()` with the correct parameters. Since we are retrieving information on Leia, you will pass to the function a dictionary comprising a single key-value pair: `{'search: 'leia'}`. Use the "results" key and index the dictionary representation of the decoded JSON to access the resource(s) matched by the search query return. Save the results to `leia_data`.
>>>>>>> 20abd03487f7c92a347cb5d7c560cfdc3ecf11be
2. The species key from the response results contains a url. You will need to retrieve Leia's species by making another request to the url within the species key. Assign the name of Leia's species to the variable `leia_species` then update `leia_data` by adding Leia's species name as a key/value pair.
3. Create an instance of `Person` for Leia using the data you have stored in `leia_data` and `leia_species`.
4. Write out the information produced from the instance of `Person` you have created for Leia as a dictionary to a new file `leia.json`.

<<<<<<< HEAD
:hint: Use the `jsonable()` method to transform the class instance into a dictionary.
=======
:bulb: Use the `jsonable()` method to transform the class instance into a dictionary.
>>>>>>> 20abd03487f7c92a347cb5d7c560cfdc3ecf11be
