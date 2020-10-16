import requests, json

# PROBLEM SET 09

ENDPOINT = 'https://swapi.py4e.com/api'

# BEGIN ASSIGNMENT:

# PROBLEM 01: Finish get_swapi_resource.
def get_swapi_resource():
    """This function initiates an HTTP GET request to the SWAPI service in order to return a
    representation of a resource. The function defines two parameters, the resource url (str) and
    an optional params (dict) query string of key:value pairs may be provided as search terms
    (e.g., {'search': 'yoda'}). If a match is obtained from a search, be aware that the JSON object
    that is returned will include a list property named 'results' that contains the resource(s)
    matched by the search query term(s).

    Parameters:
        resource (str): a url that specifies the resource.
        params (dict): optional dictionary of querystring arguments. This parameter should
            have a default value of None.

    Returns:
        dict: dictionary representation of the decoded JSON.
    """

    pass

# PROBLEM 02: Finish read_json
def read_json():
    """This function reads a JSON document and returns a dictionary if provided with a valid
    filepath.

    Parameters:
        filepath (str): path to file.

    Returns:
        dict: dictionary representations of the decoded JSON document.
    """

    pass

# PROBLEM 03: Finish write_json
def write_json():
    """Given a valid filepath writes data to a JSON file.

    Parameters:
        filepath (str): the path to the file.
        data (dict): the data to be encoded as JSON and written to the file.

    Returns:
        None
    """

    pass

# PROBLEM 04: Create the __init__, __str__, and evaluate_information methods to Person
class Person():
    """
    This class contains all of the information that the First Order has on a person.

    Instance Variables:
        name (str): Name of the person.
        hair_color (str): Hair color of the person.
        eye_color (str): Eye color of the person.
        species_name (str): Name of the species of the person.
        location (str): Current planet the person is known to be operating on.
            The location starts out as 'unknown' until we can cross-reference our
            central databases with the information from our informants. THAT'S YOUR
            JOB!
    """

    def __init__():

        pass


    def __str__(self):

        pass


    def evaluate_information():
        """
        This method will take a dictionary <information_dict> that has the following keys:

            hair_color, eye_color, species_name, location, name

        and it will check if the values to those keys are the exact same as the
        respective instance variable (e.g. <name> should be the same as <self.name>). If
        all keys are the same, then update <self.location> to be the value of the
        <information_dict> <location> key.

        Parameters:
            information_dict (dict): A dictionary of information to compare with the instance
                variables.

        Returns:
            None, but has the potential to update self.location
        """

        pass

# PROBLEM 05: Build the main() function following the cues
def main():
    """
    This function will use various utility functions, classes, and methods to determine
    the location of two Resistance members: Rey and Chewbacca. Nothing is returned from
    this function, however a file <updated_information.json> is produced.

    Parameters:
        None

    Returns:
        None
    """
    pass

# END ASSIGNMENT

if __name__ == '__main__':
    main()
