import requests, json

# PROBLEM SET 09

ENDPOINT = 'https://swapi.py4e.com/api'

# BEGIN ASSIGNMENT:

# PROBLEM 01: Finish get_swapi_resource.
def get_swapi_resource(url, params=None):
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

    if params:
        response = requests.get(url, params=params).json()
    else:
        response = requests.get(url).json()

    return response


# PROBLEM 02: Finish read_json
def read_json(filepath):
    """This function reads a JSON document and returns a dictionary if provided with a valid
    filepath.

    Parameters:
        filepath (str): path to file.

    Returns:
        dict: dictionary representations of the decoded JSON document.
    """

    with open(filepath, 'r', encoding='utf-8') as file_obj:
        data = json.load(file_obj)

    return data


# PROBLEM 03: Finish write_json
def write_json(filepath, data):
    """Given a valid filepath writes data to a JSON file.

    Parameters:
        filepath (str): the path to the file.
        data (dict): the data to be encoded as JSON and written to the file.

    Returns:
        None
    """

    with open(filepath, 'w', encoding='utf-8') as file_obj:
        json.dump(data, file_obj, ensure_ascii=False, indent=2)


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

    def __init__(self, name, hair_color, eye_color, species_name):

        self.name = name
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.species_name = species_name
        self.location = 'unknown'

    def __str__(self):

        description =  f"{self.name} is a {self.species_name} with {self.hair_color} hair and {self.eye_color} eyes. Location: {self.location}"
        return description

    def evaluate_information(self, information_dict):
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

        if information_dict['name'] == self.name and information_dict['hair_color'] == self.hair_color and information_dict['eye_color'] == self.eye_color and information_dict['species_name'] == self.species_name:
            self.location = information_dict['location']


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

    # First, call <get_swapi_resource> with the correct parameters (you'll likely want
    # to pass a parameters dictionary like so: {'search':'rey'}) to retrieve a
    # dictionary of data about Rey. Save it to <rey_data>. Make sure <rey_data> is a
    # dictionary, and not a list!
    rey_data = get_swapi_resource(ENDPOINT + '/people', {'search':'rey'})
    rey_data = rey_data['results'][0]

    print(f"\n Rey species = {rey_data}['species']\n")

    # Now, get Rey's species name by making a request to the url that is contained in the string
    # stored in <rey_data['species'][0]>. Save the name of that species to <rey_species>.
    # <rey_species> should be a string. Then, add a new key/value pair to <rey_data>
    # which has a key of "species_name" and a value of <rey_species>.
    rey_species = get_swapi_resource(rey_data['species'][0])
    rey_species = rey_species['name']
    rey_data['species_name'] = rey_species

    # Do the same thing for Chewbacca, saving the information to <chewbacca_data> and
    # <chewbacca_species>.
    chewbacca_data = get_swapi_resource(ENDPOINT + '/people', {'search':'chewbacca'})
    chewbacca_data = chewbacca_data['results'][0]
    chewbacca_species = get_swapi_resource(chewbacca_data['species'][0])
    chewbacca_species = chewbacca_species['name']
    chewbacca_data['species_name'] = chewbacca_species

    # Create instances of <Person> for both Rey and Chewbacca using the data you have stored
    # in the dictionaries <rey_data>, <chewbacca_data> and strings <rey_species>, <chewbacca_species>
    rey = Person(rey_data['name'], rey_data['hair_color'], rey_data['eye_color'], rey_data['species_name'])
    chewbacca = Person(chewbacca_data['name'], chewbacca_data['hair_color'], chewbacca_data['eye_color'], chewbacca_data['species_name'])

    print(f"\nChewie species = {chewbacca.species_name}\n")


    # Read in the data from the informants using the <read_json> function.
    # Make a new list <rey_info> that only contains the information on rey.
    # Make a new list <chewbacca_info> that only contains the information on chewbacca.
    # If you are confused, look at the keys of the dictionary that resulted from your
    # call to <read_json>.
    informant_info = read_json('informants.json')
    rey_info = informant_info['information_on_rey']
    chewbacca_info = informant_info['information_on_chewbacca']

    # For each dictionary in <rey_info>, utilize the method <evaluate_information> from the
    # instance of <person> for Rey. Only one entry of <rey_info> should flag as True and update
    # Rey's location. Then, do the same for Chewbacca.
    for info in rey_info:
        rey.evaluate_information(info)

    for info in chewbacca_info:
        chewbacca.evaluate_information(info)

    print(rey)
    print(chewbacca)

    # Create a new dictionary with only two key value pairs:
    #
    # {
    #   'Rey': <str representation of Rey's instance of Person>
    #   'Chewbacca': <str representation of Chewbacca's instance of Person>
    # }
    out_dict = {}
    out_dict['Rey'] = str(rey)
    out_dict['Chewbacca'] = str(chewbacca)

    # Write out your new dictionary to <updated_information.json> using <write_json>
    write_json('updated_information.json',out_dict)

# END ASSIGNMENT

if __name__ == '__main__':
    main()
