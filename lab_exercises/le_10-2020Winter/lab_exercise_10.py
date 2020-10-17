import requests, json

# START LAB EXERCISE 10
print('Lab Exercise 10 \n')

# THIS WEEK'S LAB:
# The following problems will introduce you to the requests module and
# to SWAPI API.  If a problem has a set-up, do NOT modify, delete, or ignore
# the set-up code.

ENDPOINT = 'https://swapi.py4e.com/api'

PERSON_PROPERTIES = (
    "name", "height", "mass", "hair_color", "skin_color",
    "eye_color", "birth_year", "gender", "homeworld", "films",
    "species", "starships", "url"
    )

# PROBLEM 1 (5 POINTS)

def get_people(url, params=None):
    """
    This function initiates an HTTP GET request to a url to return a
    list of dictionaries. The function defines two parameters,
    the resource url (str) and an optional params (dict) query string of
    key:value pairs that may be provided as search terms (e.g., {'search': 'yoda'}).

    Parameters:
        url (str): the base url to look for response
        params (dict): the parameters to specify the query.

    Returns:
        people (list): a list of dictionaries, each of which describes a person

    HINT: < requests.get(url, params).json() > returns a JSON Object that contains
    a "results" list property with a maximum of 10 records per request.
    Use the "results" key to index the dictionary representation of the
    decoded JSON to access the resource(s) matched by the search query return.
    """

    pass # Implement


# PROBLEM 2 (5 points)

def filter_properties(person, PERSON_PROPERTIES):
    """
    Extract specific properties of the given person into a new dictionary.

    Parameters:
        person (dict): the dictionary containing properties of a person.
        PERSON_PROPERTIES (tupl): a tuple containing the characteristics of a person

    Returns:
        record (dict): a dictionary containing filtered key-value pairs
        of characteristics of the person.
    """

    pass # Implement


# PROBLEM 3 (5 points)

def write_json(filepath, data):
    """
    Given a valid filepath writes data to a JSON file.

    Parameters:
        filepath (str): the path to the file.
        data (dict): the data to be encoded as JSON and written to the file.

    Returns:
        None

    HINT: for the open parameters, use encoding='utf-8' and for the
    json.dump parameters, use ensure_ascii=False, indent=2.
    """

    pass # Implement


# PROBLEM 4 (5 POINTS)

def main():
    """
    Refer to Lab Excersie 10 README.md for instructions and tips.

    Parameters:
        None

    Returns:
        None

    HINT: Review SWAPI documentation on how to make a call to people section.
    """

    pass # Implement


if __name__ == '__main__':
    main()

# END LAB EXERCISE
