# PROBLEM SET 6

# Importing some required libraries:
import csv # You'll use this one!
import operator # Don't worry about this one.


def sort_dictionary_by_value(dictionary):
    """
    DON'T CHANGE THIS FUNCTION. This function sorts a dictionary by its values in a
    descending fashion.

    Parameters:
        dictionary (dict): A dictionary to be sorted.

    Returns:
        dict: The sorted dictionary.
    """

    desc_dictionary = dict(sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True))

    return desc_dictionary

# BEGIN CODING HERE - - - - - - - - - - - - - - - - - - - - - - -

def read_csv_file(input_filepath):
    """
    This function reads a .csv file and parses it into a list of dictionaries,
    where each dictionary is formed from the data on one line of the .csv file.
    This function takes one argument < input_filepath >, which is the path of the file
    to be read. You will need to use the "csv" module in this function.

    Parameters:
        input_filepath (str): The location of the file to read and parse.

    Returns:
        list: A list of dictionaries, where each dictionary is one row from the
            input file.
    """

    pass


def write_csv_file(output_filepath, dict_to_write, header):
    """
    Writes a .csv file using the "csv" module. The file will contain the information
    from <dict_to_write>, where each row of the new .csv file is one of the key/value
    pairs. In other words, the output file should have two columns.

    Parameters:
        output_filepath (str): The file path to the new file being created.
        dict_to_write (dict): The information to include in the file being created.
        header (list): A list of two elements that correspond to the headers of the
            two columns in the new file.

    Returns:
        None, but writes a file.
    """

    pass


def acres_to_km2(acres):
    """
    Converts a value in acres to a value in kilometers squared. The conversion
    is as follows:

        1 acre is approximately 0.004 km^2

    Parameters:
        acres (float): A number in acres

    Returns:
        float: A number in km^2
    """

    pass


def km2_by_state(list_of_park_dicts):
    """
    This function takes a list of national park data (e.g. the returned value from
    <read_csv_file>), and returns a new dictionary that contains the summed
    area (in kilometers squared) of national parks in each state. The output
    dictionary should have the format:

    {<state two-letter identifier>: <float of total area of parks in that state in km^2>}

    Parameters:
        list_of_park_dicts (list): A list of dictionaries, where each dictionary contains the
            information on a specific park.

    Returns:
        dict: A dictionary where the keys are the two-letter state identifiers and the values
            are the sum total area of national parks in that state (in km^2).
    """

    pass


def main():
    """
    Read in the data from "parks.csv". Then, parse that data and determine
    how much national park area is in each state using your < km2_by_state > function.
    Then, sort the resultant dictionary. Finally, write the sorted dictionary to a
    new file "parkarea.csv". Don't forget to include headers into the "parkarea.csv"
    file!

    Parameters:
        None

    Returns:
        None
    """

    pass


# END CODING HERE - - - - - - - - - - - - - - - - - - - - - - - - - - - -

if __name__ == '__main__':
    main()
