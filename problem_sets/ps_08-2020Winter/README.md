# SI 506: Problem Set 08

## This Week's Lab

This week, we will be working with the *advanced* part of Classes: Inheritance! You'll work and code
as a Software Engineer of a game company. You are asked to construct objects for those heroes in the
game and also simulate the game. Each task that you must complete in the skeleton code file is,
problem_set_08.py delineated by a `pass`.

## 1.0 Problem 01 (12.5 Points)

Implement the `Hero` parent class.

Instance Variables:

* `name` (str): The name of the hero.
* `hp` (float): The health points of the hero.
* `mp` (float): The magic points of the hero.
* `damage` (float): The damage of the hero.
* `strength_growth` (float): The strength gain per level of the hero.
* `agility_growth` (float): The agility gain per level of the hero.
* `intelligence_growth` (float): The intelligence gain per level of the hero.

### 1.1 Implement the `__init__()` method

The constructor will take the following arguments:

* `self`
* `name`
* `hp`
* `mp`
* `damage`
* `strength_growth`
* `agility_growth`
* `intelligence_growth`

and assign each to an instance variable of the same name. In addition, the constructor should create
an instance variable called `level` and assign its value as 0 (zero). We'll change that later when
calling the `level_up()` method in the child classes.

Replace the `pass` statements with the appropriate code blocks. Read the class and method Docstrings
for additional implementation details.

### 1.2 Implement the `__str__()` method

Implement the `__str__()` method of the `Hero` class by replacing the `pass` statement with the
appropriate code block. Read the function Docstring for additional implementation details.

### 1.3 Implement the `attack()` method

Implement the `attack()` method of the `Hero` class by replacing the `pass` statement with the
appropriate code block. Read the function Docstring for additional implementation details.

### 1.4 Implement the `is_dead()` method

Implement the `is_dead()` method of the `Hero` class by replacing the `pass` statement with the
appropriate code block. Read the function Docstring for additional implementation details.

## 2.0 Problem 02 (12.5 Points)

Implement the `StrengthHero` child class.

Instance Variables:

* `name` (str): The name of the hero.
* `hp` (float): The health points of the hero.
* `mp` (float): The magic points of the hero.
* `damage` (float): The damage of the hero.
* `strength_growth` (float): The strength gain per level of the hero.
* `agility_growth` (float): The agility gain per level of the hero.
* `intelligence_growth` (float): The intelligence gain per level of the hero.

### 2.1 Implement the `__init__()` method

The constructor will take the following arguments:

* `self`
* `name`
* `hp`
* `mp`
* `damage`
* `strength_growth`
* `agility_growth`
* `intelligence_growth`

and assign each to an instance variable of the same name. In addition, the constructor should create
an instance variable called `main_attribute` and assign the string "strength" as it's value.

:exclamation: Use the `super()` function to inherit the attributes from the `Hero` parent class.

Replace the `pass` statements with the appropriate code blocks. Read the class and method Docstrings
for additional implementation details.

### 2.2 Implement the `level_up()` method

Implement the `level_up()` method of the `StrengthHero` class by replacing the `pass` statement with
the appropriate code block. Read the function Docstring for additional implementation details.

### 2.3 Implement the `ability()` method

Implement the `ability()` method of the `StrengthHero` class by replacing the `pass` statement with
the appropriate code block. Read the function Docstring for additional implementation details.

## 3.0 Problem 03 (12.5 Points)

Implement the `AgilityHero` child class.

Instance Variables:

* `name` (str): The name of the hero.
* `hp` (float): The health points of the hero.
* `mp` (float): The magic points of the hero.
* `damage` (float): The damage of the hero.
* `strength_growth` (float): The strength gain per level of the hero.
* `agility_growth` (float): The agility gain per level of the hero.
* `intelligence_growth` (float): The intelligence gain per level of the hero.

### 3.1 Implement the `__init__()` method

The constructor will take the following arguments:

* `self`
* `name`
* `hp`
* `mp`
* `damage`
* `strength_growth`
* `agility_growth`
* `intelligence_growth`

and assign each to an instance variable of the same name. In addition, the constructor should create
an instance variable called `main_attribute` and assign the string "agility" as it's value.

:exclamation: Use the `super()` function to inherit the attributes from the `Hero` parent class.

Replace the `pass` statements with the appropriate code blocks. Read the class and method Docstrings
for additional implementation details.

### 3.2 Implement the `level_up()` method

Implement the `level_up()` method of the `AgilityHero` class by replacing the `pass` statement with
the appropriate code block. Read the function Docstring for additional implementation details.

### 3.3 Implement the `ability()` method

Implement the `ability()` method of the `AgilityHero` class by replacing the `pass` statement with
the appropriate code block. Read the function Docstring for additional implementation details.

## 4.0 Problem 04 (12.5 Points)

Implement the `IntelligenceHero` child class.

Instance Variables:

* `name` (str): The name of the hero.
* `hp` (float): The health points of the hero.
* `mp` (float): The magic points of the hero.
* `damage` (float): The damage of the hero.
* `strength_growth` (float): The strength gain per level of the hero.
* `agility_growth` (float): The agility gain per level of the hero.
* `intelligence_growth` (float): The intelligence gain per level of the hero.

### 4.1 Implement the `__init__()` method

The constructor will take the following arguments:

* `self`
* `name`
* `hp`
* `mp`
* `damage`
* `strength_growth`
* `agility_growth`
* `intelligence_growth`

and assign each to an instance variable of the same name. In addition, the constructor should create
an instance variable called `main_attribute` and assign the string "intelligence" as it's value.

:exclamation: Use the `super()` function to inherit the attributes from the `Hero` parent class.

Replace the `pass` statements with the appropriate code blocks. Read the class and method Docstrings
for additional implementation details.

### 4.2 Implement the `level_up()` method

Implement the `level_up()` method of the `IntelligenceHero` class by replacing the `pass` statement
with the appropriate code block. Read the function Docstring for additional implementation details.

### 4.3 Implement the `ability()` method

Implement the `ability()` method of the `IntelligenceHero` class by replacing the `pass` statement
with the appropriate code block. Read the function Docstring for additional implementation details.

## 5.0 Problem 05 (50 Points)

Implement `main()` following the hints provided below.

### 5.1 SETUP

```python
heroes = [
    {
        "name": "Axe",
        "main_attribute": "strength",
        "base_hp": 625,
        "base_mp": 234,
        "base_damage": 52,
        "strength_growth_per_level": 3.6,
        "agility_growth_per_level": 2.2,
        "intelligence_growth_per_level": 1.6
    },
    {
        "name": "Monkey King",
        "main_attribute": "agility",
        "base_hp": 511,
        "base_mp": 260,
        "base_damage": 51,
        "strength_growth_per_level": 2.8,
        "agility_growth_per_level": 3.7,
        "intelligence_growth_per_level": 1.8
    },
    {
        "name": "Invoker",
        "main_attribute": "intelligence",
        "base_hp": 492,
        "base_mp": 195,
        "base_damage": 42,
        "strength_growth_per_level": 2.4,
        "agility_growth_per_level": 1.9,
        "intelligence_growth_per_level": 4.6
    }
]
```

### 5.2 Create instances of `Hero`

1. Loop over the `heroes` list and create a correspoding `Hero` instance for each dictionary encountered.
    - If a hero's main attribute is "strength", it should be an instance of `StrengthHero`
    - If a hero's main attribute is "agility", it should be an instance of `AgilityHero`
    - If a hero's main attribute is "intelligence", it should be an instance of `IntelligenceHero`

    :bulb: Use conditional statements to check the hero's main attribute.

2. Add key-value pairs of the heros into a new dictionary named `all_heroes`. It should look like this: {`name` : hero instance}

### 5.3 Level up your heroes

1. Iterate over `all_heroes`, for each key-value pair, level up the value of `level` (which is an attribute of `Hero`) to 25. This means you need to call the `level_up()` method 25 times for each hero.\
:bulb: You can use `range()` to help repeat functions/methods several times.
2. Print the information of your heroes by uncomment the for loop below when you finish the above steps to see how your heros have leveled up!
```python
for v in all_heroes.values():
    print(v)
```

Your print output should be the same as below:
```python
Axe, level 25, hp 2425.0, mp 434.0, damage 141.9999999999999
Monkey King, level 25, hp 1211.0, mp 710.0, damage 143.5
Invoker, level 25, hp 792.0, mp 2495.0, damage 156.9999999999999
```

### 5.4 Simulate a fight!

Let your heroes fight with each other with following rules:

If there are 4 heroes, `A`, `B`, `C` and `D`,
- `A` would use their ability and then attack `B`, `C`, `D`
- Then `B` would use their ability and then attack `A`, `C`, `D`
- Then `C`, then `D`...

1. Iterate over the `all_heroes` dictionary's key/value pairs. Recall that the key is the hero name and the value is the class instance representing that hero. This loop will determine whose turn it is to act in the fight!
2. Have the hero use their ability. Remember that the ability is a method of the class instance.
3. Inside the for loop from step 1, iterate through the key/value pairs in `all_heroes` again, but this time use different variables to capture the individual keys and values than the outer loop. This loop will let the hero, who has activated their ability, attack the other heroes.
4. Have the hero, whose ability is activated, attack each of the other heroes. Make sure the hero doesn't attack themself!\
:bulb: Use a conditional statement to ensure that the hero from the inner loop is different from the hero in the outer loop.\
:bulb: You will want to use the `attack()` method here!

### 5.5 Find the winners!

1. Iterate over the `all_heroes` dictionary's key/value pairs and use the method `is_dead()` to check whether the hero is dead or not. If the hero is not dead, add it into the list named `winners`.
2. Return `winners`.

## RECAP

Now let's do a recap of this Problem Set:
Why do we need the `Hero` class? These heroes have attributes and methods that do not change between the different types of heros, like the `attack()` method. We need the child classes `StrengthHero`, `AgilityHero`, and `IntelligenceHero` because the different types of heroes have different ways of leveling up and abilities seen in the `level_up()` and `ability()` methods.

That's the power of inheritance and overriding. We use a parent class to manage the common attributes and methods, and then use the child class' attributes and methods to specify things that only apply to itself and also to modify parent class methods that should act in different ways.

The simulation has been simplified for you. In a real world game there would be a lot more attributes and methods to manage, that's why we need Object Oriented Programming, OOP, to better organize our code.
