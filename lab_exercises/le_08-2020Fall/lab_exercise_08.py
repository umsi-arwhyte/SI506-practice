import csv

# START LAB EXERCISE 08
print('Lab Exercise 08 \n')

# PROBLEM 1 (5 Points)
def read_csv_file(input_filepath):
    """
    This function reads a .csv file and parses it into a list of dictionaries,
    where each dictionary is formed from the data on one line of the .csv file.

    Parameters:
        filepath (str): The location of the file to read and parse.

    Returns:
        list: A list of dictionaries, where each dictionary is one row from the
            input file.
    """

    pass

# PROBLEM 2 (5 Points)
def hci_database_urls(library_list):
    """
    This function takes a list of library data and returns a new dictionary of databases in the HCI category.
    only the name of the database and the link to the database will be included.

    Parameters:
        library_list (list): A list of dictionaries, where each dictionary contains the
            information on a specific databas.

    Returns:
        dict: A dictionary where the keys are the name of the HCI database and its permalink
    """
    pass


# PROBLEM 3 (5 Points)
def write_csv_file(output_filepath, dict_to_write, header):
    """
    Writes a .csv file using the < csv > module.

    Parameters:
        output_filepath (str): The file path to the new file being created.
        dict_to_write (dict): The information to include in the file being created.
        header (list): The header row in the table.

    Returns:
        None
    """

    pass

# PROBLEM 4 (5 Points)
def main():
    """
    Entry point for the program. This function will process the library data.

    Parameters:
        None

    Returns:
        None
    """
    pass

if __name__ == '__main__':
    main()
