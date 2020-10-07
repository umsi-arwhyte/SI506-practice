from sw_entities import Film, Planet, Person
from sw_utilities import get_swapi_resource, convert_resource_to_obj, write_json, read_json
import requests, json

# PROBLEM SET 10
# BEGIN ASSIGNMENT:

def main():

    # BEGIN TEST FOR <get_swapi_resource> (Uncomment me when you're ready!)
    # get_swapi_resource('http://google.com/max')
    # END TEST FOR <get_swapi_resource>

    # BEGIN TEST FOR <Entity> (Uncomment me when you're ready!)
    # entity = Entity("https://swapi.co/api/people")
    # print(entity.url == "https://swapi.co/api/people")
    # END TEST FOR <Entity>

    # BEGIN TEST FOR <Film> (Uncomment me when you're ready!)
    # film_property_dict = {"title": "max", "episode_id": 1, "url": "www.max.com"}
    # film = Film(film_property_dict)
    # print(film.url == "www.max.com")
    # print(film.jsonable() == film_property_dict)
    # END TEST FOR <Film>

    # BEGIN TEST FOR <convert_resource_to_obj> (Uncomment me when you're ready!)
    # print(isinstance(luke, Person))
    # print(luke.name == "Luke Skywalker")
    # print(luke.url == "https://swapi.py4e.com/api/people/1/")
    # END TEST FOR <convert_resource_to_obj>

    # BEGIN TEST FOR <update_homeworld> (Uncomment me when you're ready!)
    # print(isinstance(luke.homeworld, Planet))
    # END TEST FOR <update_homeworld>

    # BEGIN TEST FOR <update_films> (Uncomment me when you're ready!)
    # print(isinstance(luke.films[0], Film))
    # END TEST FOR <update_films>

    # BEGIN TEST FOR <jsonable> (Uncomment me when you're ready!)
    # print(luke.jsonable()["homeworld"]["name"] == "Tatooine")
    # print(luke.jsonable()["films"][0]["title"] == "A New Hope")
    # END TEST FOR <jsonable>


# END ASSIGNMENT

if __name__ == '__main__':
    main()