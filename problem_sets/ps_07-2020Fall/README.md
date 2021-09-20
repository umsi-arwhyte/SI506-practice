# SI 506: Problem Set 7

## This week's Problem Set
This week's problem set will focus on dictionaries, which are a data structure that involves using `keys` to look up `values` that they are mapped with. You can think of a python dictionary in a similar way that you would think of a traditional dictionary. In a traditional dictionary, the `key` would be the word you are looking up and the `value` would be the definition of the word. The general structure of a dictionary would be
```python
<dict_name> = {
    <key>: <value>,
    <key>: <value>,
    <key>: <value>
}
```

## Background
This lab centers around the halloween tradition of trick-or-treating, which consists of groups of people (usually children, but we here at SI 506 don't judge) traveling from door to door asking for treats (usually candy) by saying "trick-or-treat". Upon making this request, the trick-or-treaters are usually presented with treats that they store in a bucket or a bag. In this problem set, you are about to go trick-or-treating with your friends Brian, Patrick, and Simone.

## Problem 01 (20 points)
1. Before you can head out for your fun night of trick-or-treating, you need to make sure that each of your friends have all their supplies ready. They each need to have a `costume` as well as a bag to hold their `treats`. In the `main()` function, create three dictionaries, each representing your friends, and assign them with the following key-value pairs:
    * Brian's `"costume"` needs to be a `"wizard"` and his `"treats"` should be an empty list, representing a (currently) empty candy bag
    * Patrick's `"costume"` needs to be a `"vampire"` and his `"treats"` should be an empty list.
    * Simone's `"costume"` should be a `"mummy"` and her `"treats"` should be an empty list

    :bulb: If you were to print out the `brian` dictionary for instance, the output would look like this:
    ```
    {'costume': 'wizard', 'treats': []}
    ```

2. You can have many different types of key, value pairs in python. The key can be any immutable object (integer, string, etc.) and the value can be almost anything, it can even be another dictionary! (You can probably see where this is going). Inside of the `main()` function, create a dictionary called `friends_dict` that maps your friends names (as strings) to their respective dictionaries.

    :bulb: If you were to print out `friends_dict`, it would look like this:
    ```
    {'brian': {'costume': 'wizard', 'treats': []}, 'patrick': {'costume': 'vampire', 'treats': []}, 'simone': {'costume': 'mummy', 'treats': []}}]
    ```

3. One way you can view the contents of a given dictionary is through the use of the `items()` method. This method returns a `dict_items` object which displays all of the key, value pairs stored within the dictionary. Call the `items()` method on the `friends_dict` dictionary and store the resulting value in a variable called `friends_dict_items`
    
    :bulb: If you were to print out `friends_dict_items`, it would look like this:
    ```
    dict_items([('brian', {'costume': 'wizard', 'treats': []}), ('patrick', {'costume': 'vampire', 'treats': []}), ('simone', {'costume': 'mummy', 'treats': []})])
    ```

## Problem 02 (25 points)
Now that you're all ready to go trick-or-treating, we just need a way for you to recieve the treats. 
1. Create a function called `recieve_treats()` that takes in a dictionary of `trick-or-treaters` and a string representing a `candy` that is going to be handed out as required parameters.

    :bulb: This function should loop through each of the `trick-or-treaters` and add the `candy` to each of their `treats` lists

    :bulb: There are several ways to loop through a `dict`, including looping over the keys using the `keys()` method, the values using the `values()` method, and the items using the `items()` method. Determine which approach would be best for this particular implementation. 

    :bulb: If you were to call this function with the parameters of `friends_dict` and `"snickers"` for instance, and then printed the `brian` dictionary, it would look like this:
    ```
    {'costume': 'wizard', 'treats': ['snickers']}
    ```

    
2. In the `main()` function, call the `recieve_treats()` function to add each of the following candies to your friends' `treats` lists
    * `"skittles"`
    * `"snickers"`
    * `"candy corn"`

    :bulb: After completing this step, using the `items()` method on the `friends_dict` would look like this:
    ```
    dict_items([('brian', {'costume': 'wizard', 'treats': ['skittles', 'snickers', 'candy corn']}), ('patrick', {'costume': 'vampire', 'treats': ['skittles', 'snickers', 'candy corn']}), ('simone', {'costume': 'mummy', 'treats': ['skittles', 'snickers', 'candy corn']})])
    ```
3. Patrick somehow managed to get more candy than the rest of you, add the following candies (as strings) to just `patrick`'s `treats` list
    * `"hershey bar"`
    * `"starburst"`
    * `"tootsie roll"`

    :bulb: After adding these candies to patrick's `treats` list, printing out the `patrick` dictionary would look like this:
    ```
    {'costume': 'vampire', 'treats': ['skittles', 'snickers', 'candy corn', 'hershey bar', 'starburst', 'tootsie roll']}
    ```

## Problem 03 (55 Points)
After a successful night of trick-or-treating, you and your friends all go home. 
1. Patrick likes to sort his candy by type, `chocolate`, `fruit`, and `other`. In order to help him do this, we need to create a function, called `sort_candy()` which takes in a list of candies and returns a dictionary which contains three different lists, one representing chocolate candies, one representing fruit candies and one representing other candies.

    :bulb: This function comes with a dictionary called `types`, which has three keys: `chocolate`, `fruit`, and `other`. Each key maps to an (initially) empty list.

    :bulb: `sort_candy()` should `loop` through a list of candies, and then add each candy to the appropriate list within the `types` dictionary

    :bulb: While there are many different candies that can fall into each of these categories, for the purpose of this exercise, the different types of candy (chocolate, fruit, and other) are defined below:
    
    * Chocolate: "hershey bar" and "snickers"
    * Fruit: "skittles" and "starburst"
    * Other: "tootsie roll" and "candy corn"
    
    :bulb: Each candy should be sorted into the appropriate list based on its type

2. After you've implemented `sort_candy()`, call this function on  `patrick`'s `treats` list and store the resulting dictionary in a variable called `patricks_candies_sorted`

    :bulb: After using `sort_candy()` to create the `patricks_candies_sorted` dictionary, it should look like this:
    ```
    dict_items([('chocolate', ['snickers', 'hershey bar']), ('fruit', ['skittles', 'starburst']), ('other', ['candy corn', 'tootsie roll'])])
    ```

3. Using the `patricks_candies_sorted` dictionary, create three lists called `chocolate_candies`, `fruit_candies`, and `other_candies`.
    * `chocolate_candies` should have the `"chocolate"` list from the `patricks_candies_sorted` dictionary
    * `fruit_candies` should have the `"fruit"` list from the `patricks_candies_sorted` dictionary
    * `other_candies` should have the `"other"` list from the `patricks_candies_sorted` dictionary


:bulb: Note: The way the `main()` function is called in this problem set is a bit unusual. This was done in order to make grading the assignment easier. In a more traditional context, the `main()` function would be called like this:
```python
if __name__ == '__main__':
    main()
```