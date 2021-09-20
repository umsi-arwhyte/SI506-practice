# LAB EXERCISE 08
print('Lab Exercise 08')

# This Week's Lab
# This lab exercise introduces you to classes, creating instances and updating variables.

# A class named Dog has been created using the keyword class for you.
# You will be implementing the < __init__() >, < increment_age >,
# < update_tricks > and < __str__() > methods

class Dog:
    """
    This Dog class helps instantiate the Dog objects later in the lab exercise.
    This is your first exposure to Object Oriented Programming (OOP). This contains
    the init function and helper models.
    """

    # PROBLEM 1 (5 Points)

    def __init__(self): # Missing parameters
        """
        This function initialises the class with three variables: < name >, < age > and < tricks >.
        < name > is updated using the passed positional argument < name > and < age > is updated with
        < age >. < tricks > is initilized as an empty list.

        Parameters:
            name (string): Name of the Dog for the instance.
            age (float): Age of the Dog for the instance.

        Returns:
            none
        """

        pass # Implement


    # PROBLEM 2 (2.5 Points)

    def increment_age(self):
        """
        This function updates the < age > class variable's value by 1.

        Paraments:
            none

        Returns:
            none
        """

        pass # Implement


    # PROBLEM 3 (5 Points)

    def update_tricks(self): # Missing parameters
        """
        This function updates the < tricks > list with the value provided from the
        < trick > argument. Append < trick > to < tricks >.

        Parameters:
            trick (string): New trick to add to the instace.

        Returns:
            none
        """

        pass # Implement


    # PROBLEM 4 (2.5 Points)

    def __str__(self):
        """
        This function returns the string representation of the object.

        Parameters:
            none

        Returns:
            string: the string representation of the object. This should
            return the following string "Dog(name = < name >, age = < age >, tricks = < tricks >)"
        """

        pass # Implement


# PROBLEM 5 (5 Points)

# BEGIN PROBLEM 5 SOLUTION

# Refer to Lab Exercise 08 README.md for instructions and tips.

# 5.1: Create Fido

pass # Implement


# 5.2: Create Spot

pass # Implement

# END PROBLEM 5 SOLUTION

# END LAB EXERCISE
