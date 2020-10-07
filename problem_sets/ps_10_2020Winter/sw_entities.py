class Entity():
    """
    Base representation of a resource.

    Attributes:
        url: resource identifier

    """
    def __init__(self):
        pass


class Film():
    properties = ("title", "episode_id", "url")
    def __init__(self, property_dict):
        super().__init__(property_dict["url"])

        self.title = property_dict["title"]

        # Assign value to the rest properties
        pass

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
        pass


class Planet(Entity):
    properties = ("name", "climate", "terrain", "url")
    def __init__(self, property_dict):
        pass

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
        pass


class Person():
    properties = ("name", "height", "mass", "homeworld", "films", "url")
    def __init__(self, property_dict):
        pass

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
        pass

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
        pass

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
        pass