import unittest
import inspect
import re
import csv
import json
from gradescope_utils.autograder_utils.decorators import weight
from problem_set_10 import main
from sw_entities import Entity, Film, Planet, Person
from sw_utilities import get_swapi_resource, convert_resource_to_obj, write_json

# Setup variables/test files
def read_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as file_obj:
        data = json.load(file_obj)

    return data
FIXTURES = './fixtures'
# Unit tests


class ProblemSet001(unittest.TestCase):

    @weight(25)
    def test_01_get_swapi_resource(self):
        """Test function get_swapi_resource()."""

        stu_get_swapi = get_swapi_resource('https://www.google.com/max')

        self.assertEqual(stu_get_swapi, None, """
        \nERROR: We made a call to your < get_swapi_resource > function like so:

        test = get_swapi_resource('https://www.google.com/max')

        and expected the following to evaluate as true, but it didn't:

        test = None\n""")

    @weight(25)
    def test_02_entity(self):
        """Test Entity."""

        stu_entity = Entity("https://swapi.co/api/planet")
        test_entity = stu_entity.url == "https://swapi.co/api/planet"

        self.assertTrue(test_entity, """
        \nERROR: We initiated an entity instance in this way entity = Entity("https://swapi.co/api/planet").
        And expected the following to evaluate as true, but it didn't:
        test_entity = entity.url == "https://swapi.co/api/planet" \n""")

    @weight(25)
    def test_03_film(self):
        """Test Film."""

        fxt_film_property_dict = {"title": "max",
                              "episode_id": 1, "url": "www.max_test.com"}
        stu_film = Film(fxt_film_property_dict)
        test_jsonable = stu_film.jsonable() == fxt_film_property_dict

        self.assertTrue(test_jsonable, """
        \nERROR: We initiated a film instance in this way film = Film(film_property_dict)).
        And expected the following to evaluate as true, but it didn't:
         test_url = film.url == "www.max_test.com"
        test_jsonable = film.jsonable() == film_property_dict
        \n""")

    @weight(25)
    def test_04_planet(self):
        """Test Planet."""

        fxt_planet_property_dict = {
            "name": "max", "climate": "cloudy", "terrain": "flat", "url": "www.max_test.com"}
        stu_planet = Planet(fxt_planet_property_dict)
        test_jsonable = stu_planet.jsonable() == fxt_planet_property_dict

        self.assertTrue(test_jsonable, """
        \nERROR:We initiated a planet instance in this way planet = Planet(planet_property_dict)).
        And expected the following to evaluate as true, but it didn't:
        test_url = planet.url == "www.max_test.com"
        test_jsonable = planet.jsonable() == planet_property_dict
        \n""")

    @weight(50)
    def test_05_convert_resource(self):
        """Test function convert_resource_to_obj()."""
        souce_code = inspect.getsource(convert_resource_to_obj)
        stu_film_dict = read_json(f"{FIXTURES}/film3.json")
        stu_film_obj = convert_resource_to_obj(stu_film_dict, Film)
        test_title = stu_film_obj.title == "Return of the Jedi"
        test_dict_comprehension = re.search(
            r".*:.*for.*\.(items|keys)\(\).*obj_class\.properties.*", souce_code)

        self.assertTrue(test_title, """
        \nERROR: We tested your < convert_resource_to_obj > function by passing it a dict fetched from 'https://swapi.co/api/films/3/' and Film.
        And expected the following to evaluate as true, but it didn't:
        test_title = film_obj.title == "Return of the Jedi"
        .\n""")
        self.assertTrue(test_dict_comprehension, """
        \nERROR: We tested whether you used dictionary comprehension in < convert_resource_to_obj >, which means you
        should generarte property dict in one line.\n""")

    @weight(50)
    def test_06_person(self):
        """Test Person."""
        fxt_person_property_dict = {
            "name": "Luke Skywalker",
            "height": "172",
            "mass": "77",
            "homeworld": "https://swapi.py4e.com/api/planets/3/",
            "films": [
                "https://swapi.py4e.com/api/films/4/",
            ],
            "url": "https://swapi.py4e.com/api/people/1/"
        }
        souce_code = inspect.getsource(Person.update_films)
        stu_person = Person(fxt_person_property_dict)
        stu_person.update_homeworld()
        stu_person.update_films()
        ans1 = stu_person.jsonable()["homeworld"]["name"]
        ans2 = stu_person.jsonable()["films"][0]["title"]
        person_test1 =  ans1 == "Yavin IV"
        person_test2 =  ans2 == "The Phantom Menace"
        person_comprehension = re.search(r".*convert_resource_to_obj\(.*Film\).*for.*self\.films.*", souce_code)

        self.assertTrue(person_test1, f"""
        \nERROR:Your < person.jsonable()["homeworld"]["name"] > is not correct. Expect "Yavin IV", but we got {ans1}
        \n""")
        self.assertTrue(person_test2, f"""
        \nERROR: Your < person.jsonable()["films"][0]["title"] > is not correct. Expect "The Empire Strikes Back", but we got {ans2}
        \n""")
        self.assertTrue(person_comprehension, """
        \nERROR: We tested whether you used list comprehension in < update_films >, which means you
        should update self.films in one line
        \n""")


    @weight(100)
    def test_07_main(self):
        """Test function main()."""
        print("Start testing your main function")
        # call main()
        main()

        # Test the output file.
        with open('luke_updated.json', 'r') as f:
            data = json.load(f)

        correct1 = data["homeworld"]["name"] == "Tatooine" and data["homeworld"]["climate"] == "arid"
        correct2 = data["films"][0]["title"] == "A New Hope" and data["films"][-1]["title"] == "The Force Awakens"

        self.assertTrue(
            correct1, "\nERROR: Your output file < luke_updated.json > is incorrect. Double-check your code.")
        self.assertTrue(
            correct2, "\nERROR: Your output file < luke_updated.json > is incorrect. Double-check your code.")

if __name__ == "__main__":
    unittest.main(verbosity=2)
