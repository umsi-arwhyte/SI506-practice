# START PROBLEM SET 05
print('PROBLEM SET 05 \n')

# The following 5 problems constitute a pre-midterm exam review. If a problem
# includes a setup section do not modify, delete or otherwise ignore the setup
# code.

# PROBLEM 1 (20 Points):

# SETUP - DO NOT MODIFY

# We provide you with a tuple to start the problem

language1 = ("English",)

# END SETUP

# BEGIN CODING

# Refer to Problem Set 05 README.md for instructions and tips.

language2 = ("Spanish","German",)

languages = language1 + language2

languages_list = list(languages)

languages_dict = {languages : languages_list}

# END CODING

# When you have finished Problem 1, uncomment the lines below to test your result:
p1_test_ans = {('English', 'Spanish', 'German'): ['English', 'Spanish', 'German']}
print(f"\nProblem 1:\nThe following two lines should be the same:\nlanguages_dict = {languages_dict}")
print(f"languages_dict = {p1_test_ans}")

# END PROBLEM 1


# SETUP - DO NOT MODIFY

# < recipe > is a list of strings. Each element of < recipe > will be called a step.
# You'll use this data for Problems 2,3,4,5

recipe = [
    'Preheat oven to 350 degrees F (175 degree C).\n',
    'Place the sliced apples in a 9x13 inch pan.\n',
    'Mix the white sugar, 1 tablespoon flour and ground cinnamon together, and sprinkle over the apples.\n',
    'Pour water evenly over all.\n',
    'Combine the oats, 1 cup of flour, brown sugar, baking powder, baking soda and melted butter together.\n',
    'Crumble evenly over the apple mixture.\n',
    'Bake at 350 degrees F (175 degrees C) for about 45 minutes.'
    ]

# END SETUP

# PROBLEM 2 (20 Points):

def format_step(step, order):
    """
    This function accepts a step from the recipe and the order of the step.
    If < step > contains "\n", the function should remove "\n".
    Then the function should return a formatted string.

    Parameters:
        - step (str): A string that represents a step in the recipe (i.e. an element from < recipe >).
        - order (int): An integer that represents the order of the step in the recipe.

    Returns:
        - (str): A string that combines < step > and < order > in the following format:
            "Step< order >: < step >"
    """

    if "\n" in step:
        step = step[:-1]

    string = f"Step{order}: {step}"

    return string


# When you have finished < format_string >, uncomment the lines below to test your function:
print(f"\nProblem 2:\nThe following two lines should be the same:")
p2_res = format_step(recipe[0], 1)
print("Step1: Preheat oven to 350 degrees F (175 degree C).")
print(f"{p2_res}")

# END PROBLEM 2


# PROBLEM 3 (20 Points):

def create_step_length(step_list):
    """
    This function accepts a list of strings.
    Each element in < step_list > has the format "Step< order >: < step >".
    This function would return a dictionary called < step_length >.
    This function should iterate over the < step_list > list.
    For each step, the function should add a new key-value pair to the returned dictionary:
    "step< order >" : the number of characters in the < step >

    e.g. for "Step1: Preheat oven", key-value pair should be "step1": 12

    When calculating the number of characters, you should NOT include the space after ":"

    Parameters:
        - step_list (list): A list contains steps of a recipe.

    Returns:
        - step_length (dict): A dictionary that has key-value pair in the following format:
            "step< order >": length of the < step >
    """

    step_length = {}

    for step in step_list:
        step_order, step_content = step.split(": ")
        step_length[step_order.lower()] = len(step_content)

    return step_length


# When you are finished with your < create_step_length > function, uncomment the lines below.
p3_test = ['Step1: Preheat oven','Step2: Place the sliced apples','Step3: Mix the white sugar']
p3_test_ans = {'step1': 12, 'step2': 23, 'step3': 19}
p3_res = create_step_length(p3_test)
print(f"\nProblem 3:\nThe following two lines should be the same: \n{p3_test_ans}")
print(f"{p3_res}")

# END PROBLEM 3


# PROBLEM 4 (20 Points):

def filter_step_length(step_length):
    """
    This function accepts a dictionary with the key-value pair in the format
    "step< order >" : length of the < step >.
    This function returns a new dictionary of "core steps" called < filtered_dict >.
    This function would iterate each key-value pair in < step_length >,
    then adds the corresponding key-value pairs of "core steps" to the returned dictionary.

    Refer to Problem Set 05 README.md for the definition of "core steps".

    Parameters:
        - step_length (dict): A dictionary contains key-value pair in the format:
            "step< order >" : length of the < step >

    Returns:
        - filtered_dict (dict): A dictionary that only contains "core steps" key-value pairs
    """

    max_length = max(step_length.values())
    filtered_dict = {}

    for step_order, step_length in step_length.items():
        if step_length > 0.5*max_length:
            filtered_dict[step_order] = step_length

    return filtered_dict


# When you are finished with your < filter_step_length > function, uncomment the lines below.
p4_test = {"step1":4, "step2":5, "step3":7}
p4_res = filter_step_length(p4_test)
print(f"\nProblem 4:\nThe following two lines should be the same: \n{p4_test}")
print(f"{p4_res}")

# END PROBLEM 4


# PROBLEM 5 (20 Points):

def main(step_list):
    """
    This function takes a list of steps of a recipe.
    This function returns either a tuple of ints containing the the order of "core steps" in a recipe
    or a tuple of strings containing the formatted "core steps" in a recipe.

    Refer to Problem Set 05 README.md for instructions and tips.

    Parameters:
        - step_list (list): A list of strings containing steps of a recipe
            (i.e. < recipe >)

    Returns:
        - (tuple): either a tuple of ints containing the the order of "core steps" in a recipe
                or a tuple of strings containing the formatted "core steps" in a recipe.
    """

    step_list_formatted = []

    for i, step in enumerate(step_list):
        step_list_formatted.append(format_step(step, i+1))

    step_length = create_step_length(step_list_formatted)

    res_dict = filter_step_length(step_length)

    order_tuple = ()
    step_tuple = ()

    for step_order in res_dict.keys():
        order_tuple += (int(step_order[4:]),)
        step_tuple += (step_list_formatted[int(step_order[4:])-1],)

    # return order_tuple
    # if you want to return a tuple of strings containing the formatted "core steps" in a
    # recipe, comment the line above and uncomment the line below
    return step_tuple


# When you are finished with your < main > function, uncomment the lines below.
print(f"\nProblem 5:\nThe following two lines should be the same: if your function return a tuple of ints")
p5_res = main(recipe)
print(f"(3, 5, 7)\n{p5_res}\n")
print(f"The following two lines should be the same: if your function return a tuple of strings: \n('Step3: Mix the white sugar, 1 tablespoon flour and ground cinnamon together, and sprinkle over the apples.', 'Step5: Combine the oats, 1 cup of flour, brown sugar, baking powder, baking soda and melted butter together.', 'Step7: Bake at 350 degrees F (175 degrees C) for about 45 minutes.')\n{p5_res}")

# END PROBLEM 5

# END PROBLEM SET