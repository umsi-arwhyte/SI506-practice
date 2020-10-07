from sw_utilities_solution import get_swapi_resource, convert_resource_to_obj

class Entity():
    """
    Base representation of a resource.

    Attributes:
        url: resource identifier

    """
    def __init__(self,url):
        self.url = url


class Film(Entity):
    properties = ("title", "episode_id", "url")
    def __init__(self, property_dict):
        super().__init__(property_dict["url"])
        self.title = property_dict["title"]
        self.episode_id = property_dict["episode_id"]

    def jsonable(self):
        """
        Return a JSON-friendly representation of the object.
        Use a dictionary literal - {} rather than built-in dict() to avoid
        built-in lookup costs.

        The key should be the name of instance variable and value should be the corresponding value.
        For example, self.title should be converted in this way:
        {"title": self.title}

        Parameters:
            None
        Returns:
            dict: dictionary of the object's instance variables
        """
        return {
            "title": self.title,
            "episode_id": self.episode_id,
            "url": self.url
        }


class Planet(Entity):
    properties = ("name", "climate", "terrain", "url")
    def __init__(self, property_dict):
        super().__init__(property_dict["url"])
        self.name = property_dict["name"]
        self.climate = property_dict["climate"]
        self.terrain = property_dict["terrain"]

    def jsonable(self):
        """
        Return a JSON-friendly representation of the object.
        Use a dictionary literal - {} rather than built-in dict() to avoid
        built-in lookup costs.

        The key should be the name of instance variable and value should be the corresponding value.
        For example, self.name should be converted in this way:
        {"name": self.name}

        Parameters:
            None
        Returns:
            dict: dictionary of the object's instance variables
        """
        return {
            "name": self.name,
            "climate": self.climate,
            "terrain": self.terrain,
            "url": self.url
        }


class Person(Entity):
    properties = ("name", "height", "mass", "homeworld", "films", "url")
    def __init__(self, property_dict):
        super().__init__(property_dict["url"])
        self.name = property_dict["name"]
        self.height = property_dict["height"]
        self.mass = property_dict["mass"]
        self.homeworld = property_dict["homeworld"]
        self.films = property_dict["films"]

    def update_homeworld(self):
        """
        self.homeworld is a url so far
        Replace it with corresponding Planet object

        HINT: You should call the functions <get_swapi_resource>,<convert_resource_to_obj> 
        to generate the object

        Parameters:
            None
        Returns:
            None, but self.homeworld has been updated
        """
        self.homeworld = convert_resource_to_obj(get_swapi_resource(self.homeworld), Planet)

    def update_films(self):
        """
        self.films is a list of urls so far
        Replace it with a list of corresponding Film objects
        You should use list comprehension to generate the list of objects

        HINT: You should call the functions <get_swapi_resource>,<convert_resource_to_obj> 
        to generate the object

        Parameters:
            None
        Returns:
            None, but self.films has been updated
        """
        self.films = [convert_resource_to_obj(get_swapi_resource(film), Film) for film in self.films]

    def jsonable(self):
        """
        Return a JSON-friendly representation of the object.
        Use a dictionary literal - {} rather than built-in dict() to avoid
        built-in lookup costs.
        The key should be the name of instance variable and value should be the corresponding value.
        For example, self.url should be converted in this way:
        {"url": self.url}

        Notice that now self.homeworld is a Planet object and self.films is a list of Film objects.
        You need to convert Planet / Film objects using their .jsonable() methods to corresponding JSON-friendly representations.
        You should use list comprehension to generate the list of JSON-friendly representations for self.films

        Parameters:
            None
        Returns:
            dict: dictionary of the object's instance variables
        """
        return {
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "homeworld": self.homeworld.jsonable(),
            "films": [film.jsonable() for film in self.films],
            "url": self.url
        }