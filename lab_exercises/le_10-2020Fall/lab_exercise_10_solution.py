import requests, json

# LAB EXERCISE 10

# SETUP CODE
ENDPOINT = 'https://swapi.py4e.com/api'

# END SETUP

# PROBLEM 01 (2.5 Points)

def get_resource(url, params=None):
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
    """

    if params:
        return requests.get(url, params).json()
    else:
        return requests.get(url).json()


# END PROBLEM 01

# PROBLEM 02 (10 Points)

class Person:
    """
    This class contains information wanted from the results of the API call.

    Instance Variables:
        name (str): Name of the person.
        hair_color (str): Hair color of the person.
        eye_color (str): Eye color of the person.
        species_name (str): Name of the species of the person.
    """

    def __init__(self, name, hair_color, eye_color, species_name):

        self.name = name
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.species_name = species_name


    def jsonable(self):
        """Return a JSON-friendly representation of the object.
        Use a dictionary literal rather than built-in dict() to avoid
        built-in lookup costs.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variable values
        """

        return {
            'name': self.name,
            'hair color': self.hair_color,
            'eye color': self.eye_color,
            'species': self.species_name,
            }


    def __str__(self):
        return self.name

# END PROBLEM 02

# PROBLEM 03 (5 Points)

def write_json(filepath, data):
    '''
    Given a valid filepath writes data to a JSON file.
    Parameters:
        filepath (str): the path to the file.
        data (dict): the data to be encoded as JSON and written to the file.
    Returns:
        None
    '''
    with open(filepath, 'w', encoding='utf-8') as file_obj:
        json.dump(data, file_obj, ensure_ascii=False, indent=2)

# END PROBLEM 03

# PROBLEM 04 (5 Points)

def main():
    '''
    This function calls <get_resource> function to retrieve SWAPI character data. Creates an instance of < Person >. 
    Then it calls <write_json> function to store data to a json file.

    parameters:
        None
    Return:
        None
    '''

    # Call < get_resource() > with the correct parameters and save results to < leia_data >
    leia_data = get_resource(ENDPOINT + '/people', {'search': 'leia organa'})
    leia_data = leia_data['results'][0]

    print(f"Leia data = {leia_data}")

    # Retrieve Leia's species and assign to < leia_species >
    leia_species = get_resource(leia_data['species'][0])
    leia_species = leia_species['name']
    leia_data['species_name'] = leia_species

    print(f"Leia data w/Species = {leia_data}")

    # Create an instance of < Person > using the data you have stored in < leia_data >

    leia = Person(leia_data['name'], leia_data['hair_color'], leia_data['eye_color'], leia_data['species_name'])

    print(f"Leia instance name = {leia.name}")

    # Write out the information produced from the instance of < Person >
    write_json("leia.json", leia.jsonable())

# END PROBLEM 04

if __name__ == '__main__':
    main()

# END OF LAB EXERCISE