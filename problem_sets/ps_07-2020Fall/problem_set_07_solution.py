#Problem 02
def recieve_treats(trick_or_treaters, candy):
    '''
    Add the given candy to the treats list of each trick_or_treater

    Parameters:
        trick_or_treaters(dict): a dictionary of trick-or-treaters, candy(str): a string representing a candy

    Returns:
        None
    '''
    for value in trick_or_treaters.values():
        value['treats'].append(candy)

#Problem 03
def sort_candy(candy_list):
    '''
    Uses the types dict to sort the candies in the candy_list by type

    Parameters:
        candy_list(list): a list of strings, each respresenting a different candy

    Returns:
        dict_types
    '''
    types = {
        "chocolate" : [],
        "fruit" : [],
        "other" : []
    }
    for candy in candy_list:
        if candy == "hershey bar" or candy == "snickers":
            types["chocolate"].append(candy)
        elif candy == "skittles" or candy == "starburst":
            types["fruit"].append(candy)
        else:
            types["other"].append(candy)
    return types

def main():
    #Problem 01
    brian = {
    "costume": "wizard",
    "treats": []
    }

    patrick = {
        "costume": "vampire",
        "treats": []
    }

    simone = {
        "costume": "mummy",
        "treats": []
    }

    friends_dict = {
        "brian": brian,
        "patrick": patrick,
        "simone": simone
    }

    friends_dict_items = friends_dict.items()

    #Problem 02
    recieve_treats(friends_dict, "skittles")
    recieve_treats(friends_dict, "snickers")
    recieve_treats(friends_dict, "candy corn")

    friends_dict["patrick"]["treats"].extend(["hershey bar", "starburst", "tootsie roll"])
    # print(friends_dict["patrick"])

    #Problem 03
    patricks_candies = patrick.get('treats')
    patricks_candies_sorted = sort_candy(patricks_candies)
    chocolate_candies = patricks_candies_sorted.get('chocolate')
    fruit_candies = patricks_candies_sorted.get('fruit')
    other_candies = patricks_candies_sorted.get('other')

    return brian, patrick, simone, friends_dict, friends_dict_items, patricks_candies, patricks_candies_sorted, chocolate_candies, fruit_candies, other_candies

#The code below is how main is traditionally called
# if __name__ == '__main__':
#     main()

#Do not modify or delete this line
brian, patrick, simone, friends_dict, friends_dict_items, patricks_candies, patricks_candies_sorted, chocolate_candies, fruit_candies, other_candies = main()
