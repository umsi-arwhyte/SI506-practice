# SI 506: Problem Set 10

## This week's problem set
This week's problem set introduces the [Star Wars API (SWAPI)](https://swapi.py4e.com/about), the requests library and JSON objects. We will also continue working with classes and objects, dictionaries, file input and output, functions, class methods, etc.


## Background
[Star Wars](https://www.starwars.com/) is one of the most popular media franchises  in the world featuring nine films as well as other media, including several TV series, video games, novel, theme parks, etc. about an epic space saga of humans, several alien species, and robots or 'droids' who co-exist 'A long time ago in a galaxy far, far away.' These characters travel around different planets in the galaxy using starships that can travel through 'hyperspaces' in speed of light. A mystical power known as the 'Force' exists as an energy field created by all living beings that binds the galaxy together. Those whom 'the force is strong with' possess various superpowers. The Force is often used by two major knightly orders who are at conflict with each other: the Jedi, who are the peacekeepers of the Galaxy use the light side of the force and the Sith who use the dark side of the force to manipulate fear and destruction. The Galactic Empire is in control of the Sith and the rebellion forces are in a civil war with the Empire that spans several years and timelines. Learn more about the Star Wars Universe on [Wookiepedia](https://starwars.fandom.com/wiki/Main_Page).

In this problem set, you will be working with a JSON file `'people.json'` which contains incomplete information on the characters: `Rey`, `Finn`, `C-3PO` and `Chewbacca`. You will be calling the `SWAPI API` to get basic information on these characters and link them to the films that they appear in.

## 1.0 Problem  01 (25 points)
Implement the `get_swapi_resource()` function. When making an HTTP GET request, `params` do not need to be passed if it is using the default value `None`. Follow the docstring for further implementation details.

:bulb: Use an `if condition` to check if the `params` dictionary is `None` while making the request.<br>
:bulb: To convert your response to a JSON object, use the `<response>.json()` function.

## 2.0 Problem 02 (25 points)
Implement the `convert_resource_to_obj()` function. This function should use the `resource_dict` to find and pass tha appropriate arguments while creating an object of the given `obj_class`. The classes will each have a `properties` tuple that contains the name of all the properties that would be needed to instantiate the class objects. You can use `obj_class.properties` to find the relevant keys in `resource_dict.keys()`. The return of this function is provided for you, please do not change this. Iterate through the `resource_dict` and find all the relevant properties. Append the values from the relevant keys in `resource_dict.keys()` to the `obj_properties` list.

:bulb: Within a `for` loop iterating over `resource_dict.keys()`, use an `if condition` to check if the dictionary key is present in `obj_class.properties`. If the key is present, append the corresponding value to the `obj_properties` list.

## 3.0 Problem 03 (10 points)
Implement the `read_json()` function. Use `json.load()` to parse the file into a json object and return it. Read the docstring for more details.

## 4.0 Problem 04 (15 points)
Implement the `write_json()` function. Use the `json.dump()` function with an argument `indent=2`. Read the docstring for more details.

## 5.0 Problem 05 (25 points)
Implement the `Film` class with the following methods:
1. Implement the `__init__()` method using the parameters described in the docstring. (7.5 points)

2. Read the docstring and implement the `__str__()` method. (7.5 points)

3. Implement the `jsonable()` method. The `jsonable()` method returns a JSON friendly implementation of the object. Use a dictionary literal - {} rather than built-in dict() to avoid built-in lookup costs.The return of this method is a dictionary with the following format: (10 points)
```
{
    "title": < title >,
    "episode_id": < episode_id >,
    "url": < url >
}
```

## 6.0 Problem 06 (40 points)
Implement the `Person` class with the following methods:
1. Implement the `__init__()` method using the parameters described in the docstring. (7.5 points)

2. Read the docstring and implement the `__str__()` method. (7.5 points)

3. Implement the `update_films()` method. This method converts the `films` property from a list of URLs to a list of Objects. For each film URL, call the function `get_swapi_resource()` to create a property dictionary.  Pass the property dictionary and the class `Film` as arguments to `convert_resource_to_obj` to create an object for each film. You can store the returned objects to a local list.  Assign this list of `Film` objects to the `films` property. (15 points)

4. Implement the `jsonable()` method. The `jsonable()` method returns a JSON friendly implementation of the object. Use a dictionary literal - {} rather than built-in dict() to avoid built-in lookup costs.The return of this method is a dictionary with the following format: (10 points)
```
{
    "name": < name >,
    "hair_color": < hair_color >,
    "skin_color": < skin_color >,
    "eye_color": < eye_color >,
    "gender": < gender >,
    "films": [ < films > ],
    "url": < url >
}
```
## 7.0 Problem 07 (60 points)
Complete Problem 07 in the `main()` function:

### 7.1 (5 points)
1. Call the `read_json` function to parse the json file `people.json`  and assign the return value to a variable named `people_info`.
2. Create an empty dictionary named `people_objects`.

### 7.2 (20 points)
1. For each person on `people_info`, use their `name` and `get_swapi_resource()` function to send a GET request to SWAPI using `ENDPOINT + '/people'` as `resource` and  `{'search': < name >}` as the `params`.

2. Use indexes and keys to extract only the data related to the person.

:bulb: The following is an excerpt of what a typical SWAPI JSON response looks like when searching for people. You have to access the value of the key `"results"` which is a list. You then only need to extract the first element of the list. You can store this data into a list with a name of your choice.
```
{
	"count": 1,
	"next": null,
	"previous": null,
	"results": [
		{
			"name": "Luke Skywalker",
			"height": "172",
			"mass": "77",
			"hair_color": "blond",
			"skin_color": "fair",
			.........,
			"films": [
				"https://swapi.py4e.com/api/films/1/",
				"https://swapi.py4e.com/api/films/2/",
				"https://swapi.py4e.com/api/films/3/",
				"https://swapi.py4e.com/api/films/6/",
				"https://swapi.py4e.com/api/films/7/"
			],
            ....,
			"url": "https://swapi.py4e.com/api/people/1/"
		}
	]
}
```
### Problem 7.3 (20 points)
:bulb: You can use the same `for` loop for all of problem 7.2 and problem 7.3
1. For each person on `people_info`, create an object of `People` class and initialize the instance variable using the data you received from problem 7.2.
2. The `films` property for the person is still a list of urls. To replace the list with `Film` objects, call the instance method `update_films()`.
3. Store the `People` instance to the `people_objects` dictionary with the `name` as the `key` and the `Person` object as the value.
4. Use the correct key to get the string representation of the `Person` instance for `'Rey'` from the `people_objects` dictionary and assign it to a variable named `rey_instance`. 

:bulb: If you print `rey_instance`, you will get the following string:
```
Rey has brown hair and hazel eyes.
```

### Problem 7.4 (15 points)
1. Create an empty dictionary named `write_dict`.
2. For each item in the `people_objects` dictionary, call the `jsonable()` method. Store the return value in the `write_dict` dictionary with the returned value as the value and the person's `name` as the key.
3. Call the `write_json()` function to write the `write_dict` to a file named `updated_people.json`.

:bulb: This is an excerpt of what the `updated_people.json` file should look like:
```
{
  "Rey": {
    "name": "Rey",
    "hair_color": "brown",
    "skin_color": "light",
    "eye_color": "hazel",
    "gender": "female",
    "films": [
      {
        "title": "The Force Awakens",
        "episode_id": 7,
        "url": "https://swapi.py4e.com/api/films/7/"
      }
    ],
    "url": "https://swapi.py4e.com/api/people/85/"
  },
  "Finn": {
      .......
  },
  .......
}