from sw_entities_solution import Entity, Film, Planet, Person
from sw_utilities_solution import get_swapi_resource, convert_resource_to_obj, write_json, read_json

# PROBLEM SET 10
# BEGIN ASSIGNMENT:


def main():
    # Pass three tests below first before you start working on <main>

    # BEGIN TEST FOR <get_swapi_resource> (Uncomment me when you're ready!)
    get_swapi_resource('http://google.com/max') # should print 404 something wrong happened
    # END TEST FOR <get_swapi_resource>

    # BEGIN TEST FOR <Entity> (Uncomment me when you're ready!)
    entity = Entity("https://swapi.co/api/people")
    print(entity.url == "https://swapi.co/api/people")# should print True
    # END TEST FOR <Entity>

    # BEGIN TEST FOR <Film> (Uncomment me when you're ready!)
    film_property_dict = {"title": "max", "episode_id": 1, "url": "www.max.com"}
    film = Film(film_property_dict)
    print(film.url == "www.max.com") # should print True
    print(film.jsonable() == film_property_dict) # should print True
    # END TEST FOR <Film>

    # Now you can work on main :)
    # We have provided other tests for you
    # Call the function <read_json> to read <Luke.json> get the resource dict
    # Call the function <convert_resource_to_obj> to create a Person instance <luke>
    resource_dict = read_json("Luke.json")
    luke = convert_resource_to_obj(resource_dict, Person)

    # BEGIN TEST FOR <convert_resource_to_obj> (Uncomment me when you're ready!)
    print(isinstance(luke, Person)) # should print True
    print(luke.name == "Luke Skywalker") # should print True
    print(luke.url == "https://swapi.py4e.com/api/people/1/") # should print True
    # END TEST FOR <convert_resource_to_obj>

    # So far luke.homeworld is still a url. Let's replace it with a Planet object
    luke.update_homeworld()
    # BEGIN TEST FOR <update_homeworld> (Uncomment me when you're ready!)
    print(isinstance(luke.homeworld, Planet)) # should print True
    # END TEST FOR <update_homeworld>

    # So far luke.films is still a list of urls. Let's replace it with a list of Film objects
    luke.update_films()
    # BEGIN TEST FOR <update_films> (Uncomment me when you're ready!)
    print(isinstance(luke.films[0], Film)) # should print True
    # END TEST FOR <update_films>

    # BEGIN TEST FOR <jsonable> (Uncomment me when you're ready!)
    print(luke.jsonable()["homeworld"]["name"] == "Tatooine") # should print True
    print(luke.jsonable()["films"][0]["title"] == "A New Hope") # should print True
    # END TEST FOR <jsonable>

    # Now write luke.jsonable() into the file <luke_updated.json>
    write_json("luke_updated.json", luke.jsonable())




# END ASSIGNMENT

if __name__ == '__main__':
    main()