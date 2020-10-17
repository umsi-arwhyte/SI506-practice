# SI 506 Problem Set 09

## Background

### INCOMING SECURE TRANSMISSION

In this problem set, you have been levereged by the First Order to help them identify
where key Resistance members, Rey and Chewbacca, have been operating. Unfortunately,
the First Order informant network consists of all kinds of unscrupulous persons, often who will simply report anything to get paid. Therefore, there are many records of different people named Rey and Chewbacca in the informant reports <informants.json>. You will need to cross-reference the informant reports with the data that already exists in the First Order databases (i.e. SWAPI). In practice, this means that if the informant report contains the same name, hair color, eye color, and species as the SWAPI record, you will flag that report and update the location of that Resistance member.

The informant.json file contains records of name, hair_color, eye_color, species_name, and location. We strongly recommend you open the file and look at it before continuing this assignment. Look for the "TO DO" comments in this assignment to see where you need to add code.

### END TRANSMISSION

## PROBLEM 01

Implement `get_swapi_resource()` replacing the `pass` statement with the appropriate code block. Read the function Docstring for additional implementation details.

:bulb: You will need to use a conditional `if` statement to determine whether or not to
include the parameters in the `requests.get()` function call.

## PROBLEM 02

Implement `read_json()` replacing the `pass` statement with the appropriate code block. Read the function Docstring for additional implementation details.

## PROBLEM 03

Implement `write_json()` replacing the `pass` statement with the appropriate code block. Read the function Docstring for additional implementation details.

## PROBLEM 04

Implement the following `Person` methods:

* `__init__()`
* `__str__()`
* `evaluate_information()`

Replace the `pass` statements with the appropriate code blocks. Read the class and method Docstrings for additional implementation details.

This class contains all of the information that the First Order has on a person.
You will need to create a constructor that takes the following arguments:

* `self`
* `name`
* `hair_color`
* `eye_color`
* `species_name`

and convert them all into instance variables. In addition, the constructor should
create an instance variable `self.location` and set its value to "unknown" for now.
We'll change that later in the `evaluate_information()` method.

Additionally, build a `__str__()` method that returns the following:

"`name` is a `species_name` with `hair_color` hair and `eye_color` eyes. Location: `location`"

Instance Variables:

* name (str): Name of the person.
* hair_color (str): Hair color of the person.
* eye_color (str): Eye color of the person.
* species_name (str): Name of the species of the person.
* location (str): Current planet the person is known to be operating on.
    The location starts out as 'unknown' until we can cross-reference our
    central databases with the information from our informants. THAT'S YOUR
    JOB!

## PROBLEM 05: Build the main() function following the cues

Implement `main()` following the hints provided below.

First, call `get_swapi_resource()` with the correct parameters (you'll likely want
to pass a parameters dictionary like so: {'search':'rey'}) to retrieve a
dictionary of data about Rey. Save it to the variable named `rey_data`. Make sure `rey_data` is a dictionary and not a list!

Now, get Rey's species name by making a request to the url that is contained in the string stored in `rey_data['species'][0]`. Save the name of that species to `rey_species`. `rey_species` should be a string. Then, add a new key/value pair to `rey_data` which has a key of "species_name" and a value of `rey_species`.

Do the same thing for Chewbacca, saving the information to `chewbacca_data` and
`chewbacca_species`.

Create instances of `Person` for both Rey and Chewbacca using the data you have stored
in the dictionaries `rey_data`, `chewbacca_data` and strings `rey_species`, `chewbacca_species`.

Read in the data from the informants using the `read_json()` function.
Make a new list `rey_info` that only contains the information on rey.
Make a new list `chewbacca_info` that only contains the information on chewbacca.
If you are confused, look at the keys of the dictionary that resulted from your
call to `read_json()`.

For each dictionary in `rey_info`, utilize the method `evaluate_information()` from the
instance of `Person` for Rey. Only one entry of `rey_info` should flag as True and update Rey's location. Then, do the same for Chewbacca.

Create a new dictionary with only two key value pairs:

```python
  {
    'Rey': <str representation of Rey's instance of Person>
    'Chewbacca': <str representation of Chewbacca's instance of Person>
  }
```

Write out your new dictionary to `updated_information.json` using `write_json()`.