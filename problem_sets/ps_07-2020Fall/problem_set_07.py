#Problem 02
def recieve_treats(trick_or_treaters, candy):
    '''
    Adds the given candy to the treats list of each trick_or_treater

    Parameters:
        trick_or_treaters(dict): a dictionary of trick-or-treaters, candy(str): a string representing a candy

    Returns:
        None
    '''
    pass #TODO: Implement function

#Problem 03
def sort_candy(candy_list):
    '''
    Uses the types dict to sort the candies in the candy_list by type

    Parameters:
        candy_list(list): a list of strings, each respresenting a different candy

    Returns:
        dict: types
    '''
    #Setup
    types = {
        'chocolate' : [],
        'fruit' : [],
        'other' : []
    }
    #End Setup
    pass #TODO: Implement function

def main():
    """
    Program entry point.  Handles program workflow (or words to that effect).

    Parameters:
        None

    Returns:
        None
    """
    #Problem 01
    brian = None #TODO: Create dictionary
    patrick = None #TODO: Create dictionary
    simone = None #TODO: Create dictionary

    friends_dict = None #TODO: Create dictionary

    friends_dict_items = None #TODO: Use items() method to create dict_items object

    #Problem 02
    #TODO: Use recieve_treats() to add candies to the treats lists of friends_dict

    #TODO: Add candies to patrick's treats list

    #Problem 03
    patricks_candies_sorted = None #TODO: Create use sort_candy() to create dictionary
    chocolate_candies = None #TODO: Use patricks_candies_sorted to create list
    fruit_candies = None #TODO: Use patricks_candies_sorted to create list
    other_candies = None #TODO: Use patricks_candies_sorted to create list
    return brian, patrick, simone, friends_dict, friends_dict_items, patricks_candies_sorted, chocolate_candies, fruit_candies, other_candies

#Do not modify or delete this line
brian, patrick, simone, friends_dict, friends_dict_items, patricks_candies_sorted, chocolate_candies, fruit_candies, other_candies = main()

#The code below is how main is traditionally called
# if __name__ == '__main__':
#     main()
