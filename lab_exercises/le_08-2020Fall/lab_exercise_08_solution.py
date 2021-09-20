import csv

# START LAB EXERCISE 08
print('Lab Exercise 08 \n')

# PROBLEM 1 (5 Points)
def read_csv_file(path, delimiter=','):
    """
    Accepts a path, creates a file object, and returns a list of dictionaries
    that represent the row values.

    Parameters:
        filepath (str): path to file
        delimiter (str): delimiter that overrides the default

    Returns:
        list: nested dictionaries representing the file contents
    """

    with open(path, 'r', newline='', encoding='utf-8') as csv_file:
        data = []
        reader = csv.DictReader(csv_file, delimiter=delimiter)
        for line in reader:
            data.append(line) # OrderedDict()
            # data.append(dict(line)) # convert OrderedDict() to dict

        return data

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
    database_links = {}
    for item in library_list:
        if item['Category'] == 'Human Computer Interaction':
            database = item['Name']
            link = item['Permalink']
            database_links[database] = link

    return database_links


# PROBLEM 3 (5 Points)
def write_csv_file(output_filepath, dict_to_write, header):
    """
    Writes a .csv file using the < csv > module. The file will contain the information
    from < dict_to_write >, where each row of the new .csv file is one of the key/value
    pairs.

    Parameters:
        output_filepath (str): The file path to the new file being created.
        dict_to_write (dict): The information to include in the file being created.
        header (list): The header row in the table.

    Returns:
        None
    """

    with open(output_filepath,'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for key,val in dict_to_write.items():
            writer.writerow((key,val))

# PROBLEM 4 (5 Points)
def main():
    """
    Entry point for the program. This function will process the library data.

    Parameters:
        None

    Returns:
        None
    """

    data = read_csv_file('library_databases.csv')
    hci_data = hci_database_urls(data)
    write_csv_file("library_hci_databases.csv", hci_data, ('database','url'))

if __name__ == '__main__':
    main()
