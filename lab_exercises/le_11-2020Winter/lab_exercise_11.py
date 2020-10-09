import requests, json

# LAB EXERCISE 11

# The following lab exercise will allow you to work more with SWAPI to get you
# comfortable with using requests module as you work on your final assignement.
# This week, we are looking at the planets in the SWAPI. We will
# be learning about classes, dictionary and list comprehensions.

# If a problem has a set-up, do NOT modify, delete, or ignore
# the set-up code.

# SETUP CODE
ENDPOINT = 'https://swapi.py4e.com/api'
PLANETS = ["Tatooine", "Yavin", "Coruscant", "Hoth"]

# END SETUP

# PROBLEM 01 (2.5 Points)

class Planet():
    '''
    This is a class that stores information about Planets in the Star Wars universe

    Attributes:
        name(str) -- The name of this planet.
        diameter(str) -- The diameter of this planet in kilometers.
        rotation_period(str) -- The number of standard hours it takes for this planet to complete a single rotation on its axis.
        orbital_period(str) -- The number of standard days it takes for this planet to complete a single orbit of its local star.
        gravity(str) -- A number denoting the gravity of this planet, where "1" is normal or 1 standard G. "2" is twice or 2 standard Gs. "0.5" is half or 0.5 standard Gs.
        population(str) -- The average population of sentient beings inhabiting this planet.
        climate(str) -- The climate of this planet. Comma separated if diverse.
        terrain(str) -- The terrain of this planet. Comma separated if diverse.
        surface_water(str) -- The percentage of the planet surface that is naturally occurring water or bodies of water.
        residents(list) -- An array of People URL Resources that live on this planet.
        films(list) -- An array of Film URL Resources that this planet has appeared in.
        created(str) -- the ISO 8601 date format of the time that this resource was created.
        edited(str) -- the ISO 8601 date format of the time that this resource was edited.
        url(str) -- the hypermedia URL of this resource.
    '''

    def __init__(self
                # put your parameters here
    ):
        '''
        This is the initialization function of the <Planet> class. Here you will 
        need to create the instance variables for the parameters described in this docstring. 
        Note that the attributes mentioned in the class definition are defined by parameters 
        passed to this constructor method.

        Parameters:
            name(str) -- The name of this planet.
            diameter(str) -- The diameter of this planet in kilometers.
            rotation_period(str) -- The number of standard hours it takes for this planet to complete a single rotation on its axis.
            orbital_period(str) -- The number of standard days it takes for this planet to complete a single orbit of its local star.
            gravity(str) -- A number denoting the gravity of this planet, where "1" is normal or 1 standard G. "2" is twice or 2 standard Gs. "0.5" is half or 0.5 standard Gs.
            population(str) -- The average population of sentient beings inhabiting this planet.
            climate(str) -- The climate of this planet. Comma separated if diverse.
            terrain(str) -- The terrain of this planet. Comma separated if diverse.
            surface_water(str) -- The percentage of the planet surface that is naturally occurring water or bodies of water.
            residents(list) -- An array of People URL Resources that live on this planet.
            films(list) -- An array of Film URL Resources that this planet has appeared in.
            created(str) -- the ISO 8601 date format of the time that this resource was created.
            edited(str) -- the ISO 8601 date format of the time that this resource was edited.
            url(str) -- the hypermedia URL of this resource.

        Returns:
            None

        '''

        def jsonable(self):
        '''
        Return a JSON-friendly representation of the object.
        Use a dictionary literal rather than built-in dict() to avoid
        built-in lookup costs.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variable values
        '''

        return {
            'url': self.url,
            'name': self.name,
            'rotational_period': self.rotation_period,
            'orbital_period': self.orbital_period,
            'diameter': self.diameter,
            'climate': self.climate,
            'gravity': self.gravity,
            'terrain': self.terrain,
            'surface_water': self.surface_water,
            'population': self.population,
            'residents': self.residents,
            'films': self.films,
            'created': self.created,
            'edited': self.edited
            }

    def __str__(self):
        '''Human-readable string representation of the object.'''

        return f"{self.name} ({self.url})"
        pass

# END PROBLEM 01

# PROBLEM 02 (10 Points)

def get_planets(name):
    '''
    This method send a GET reuest to the SWAPI and creates an instance
    of <Planet> class and returns the instance.

    Parameters:
        name(str): Name of the planet

    Returns:
        returns a <Planet> object instance
    '''

    pass

# END PROBLEM 02

# PROBLEM 03 (2.5 Points)

def write_json(filepath, data):
    '''
    Given a valid filepath writes data to a JSON file.
    Parameters:
        filepath (str): the path to the file.
        data (dict): the data to be encoded as JSON and written to the file.
    Returns:
        None
    '''
    pass

# END PROBLEM 03

# PROBLEM 04 (5 Points)

def main():
    '''
    This function calls <get_planet> function to retrieve SWAPI planer data. Then it
    calls <write_json> function to store the data to a json file.

    parameters:
        None
    Return:
        None
    '''

    pass

# END PROBLEM 04


    print('Write completed')
if __name__ == '__main__':
    main()

# END OF LAB EXEFRCISE