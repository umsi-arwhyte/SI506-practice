# SI 506: Problem Set 10

## Background

This week, you will be using list comprehension and dictionary comprehension together with json, APIs, classes(inheritance), methods, and functions in order to construct a main() function that will convert url representations to object representations and then to meaningful JSON representations. You will need to make use of an additional file, <Luke.json>, to complete this assignment. The skeleton code file, problem_set_10.py, contains areas that need your work, which are demarcated by the use of pass statements.

## General Outline

- Read this document.
- Review template files
  - `problem_set_10.py`
  - `sw_entities.py`
  - `sw_utilities.py`

- Review data files
  - `Luke.json`

## 1.0 Classes

These classes will be imported from the sw_entities module.

### 1.1 Entity()

Implement the `Entity` class `__init__()` method.

| method | implement | add Docstring | notes |
| :----- | :-------- | :------------ | :---- |
| `__init__()` | Yes | No | |

### 1.2 Film(Entity)

The `Film` class extends `Entity`. Implement the `Film` class `__init__()`, and `jsonable()` methods.

| method | implement | add Docstring | notes |
| :----- | :-------- | :------------ | :---- |
| `__init__()` | Yes | No | Here we use a `property_dict` to wrap all `properties` of the object. Use property in `properties` as key to access the value in `property_dict` and assign it to the instance attribute. For example, "url" is in `properties` and you should use `super().__init__` in this way: < super().__init__(property_dict["url"] >. For example, since "title" is in `properties`, you should assign the instance variable in this way: < self.title = property_dict["title"] >|
| `jsonable()` | Yes | No | |

### 1.3 Planet(Entity)

The `Planet` class extends `Entity`. Implement the `Planet` class `__init__()`, and `jsonable()` methods.

| method | implement | add Docstring | notes |
| :----- | :-------- | :------------ | :---- |
| `__init__()` | Yes | No | Similar to `Film.__init__()`|
| `jsonable()` | Yes | No | |

### 1.4 Person(Entity)

Person is the child class of Entity.

| method | implement | add Docstring | notes |
| :----- | :-------- | :------------ | :---- |
| `__init__()` | Yes | No | Similar to `Film.__init__()`|
| `update_homeworld()` | Yes | No | |
| `update_films()` | Yes | No |
| `jsonable()` | Yes | No | |

:exclamation: Please review `convert_resource_to_obj()` first. You need to utilize it in `update_homeworld()`, `update_films()`, `jsonable()` methods.

## 2.0 Functions

These functions will be imported from the `sw_utilities` module.

| function | implement | add Docstring | notes|
| :------- | :-------- | :------------ | :--- |
| `get_swapi_resource()` | Yes | No | This is the updated function you have implemented in PS9|
| `convert_resource_to_obj()` | Yes | No | You may notice that in the JSON returned by SWAPI, some information are represented by other urls. For example, in `Luke.json`, the value of "films" is a list of urls, where each url represents a film that Luke Skywalker was in. `convert_resource_to_obj()` would convert JSONs represented by those urls to meaningful objects. |
| `write_json()` | No | No | We have provided `write_json()` for you. |
| `read_json()` | No | No | We have provided `read_json()` for you. |

## 3.0 main()

### 3.1 Test get_swapi_resource(), Entity, and Film

Pass the three tests provided for you before you start working on `main()`.

1. Test for `get_swapi_resource()`. Uncomment when you're ready! This test print statement should return '404 something wrong happend.'
2. Test for `Entity`. Uncomment when you're ready! This test print statement should return True.
3. Test for `Film`. Uncomment when you're ready! This test print statement should return True.

### 3.2 Begin main()

Call the function `read_json()` to read `Luke.json` to retrieve the resource dict.

Call the function `convert_resource_to_obj()` to create a `Person` instance `luke`.

### 3.3 Test convert_resource_to_obj()

Uncomment when you're ready! All test print statements should return True.

### 3.4 Test update_homeworld()

So far `luke.homeworld` is still a url. Let's replace it with a Planet object. Uncomment when you're ready! This test print statement should return True.

### 3.5 Test update_films()

So far `luke.films` is still a list of urls. Let's replace it with a list of `Film` objects. Uncomment when you're ready! The test print statement should return True.

### 3.6 Test jsonable()

Uncomment when you're ready! All test print statements should return True.

### 3.7 Write luke.jsonable()

Write `luke.jsonable()` into the file `luke_updated.json`.