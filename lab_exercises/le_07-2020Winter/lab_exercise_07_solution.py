import csv
import operator

# START LAB EXERCISE 07
print('Lab Exercise 07 \n')

# THIS WEEK'S LAB:
# This lab exercise introduces you to working with files.

# SETUP Do Not Modify

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


# END SETUP

# BEGIN CODING HERE

# PROBLEM 1 (5 POINTS)

def read_csv_file(input_filepath):
    """
    This function reads a .csv file and parses it into a list of dictionaries,
    where each dictionary is formed from the data on one line of the .csv file.

    Parameters:
        input_filepath (str): The location of the file to read and parse.
    Returns:
        list: A list of dictionaries, where each dictionary is one row from the
            input file.
    """

    output_list = []

    with open(input_filepath, 'r') as f:
        reader = csv.reader(f)
        for i,row in enumerate(reader):
            if i == 0:
                labels = row
            else:
                airports_dict = {}
                for j,value in enumerate(row):
                    airports_dict[labels[j]] = value
                output_list.append(airports_dict)

    return output_list


# PROBLEM 2 (5 POINTS)

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


# PROBLEM 3 (5 POINTS)

def passengers_per_city(list_of_airport_dicts):
    """
    This function takes a list of airport data (e.g. the return from
    < read_csv_file >), and returns a new dictionary of airports in each state. The output
    dictionary should have the format:
    {< airport city >: < total number of passengers passing through the airport in that city >}

    Parameters:
        list_of_airports (list): A list of dictionaries, where each dictionary contains the
            information on a specific airport.

    Returns:
        dict: A dictionary where the keys are the city and the values
            are the total number of passengers (integer) passing through the airport in that city.
    """

    passengers_per_city = {}

    for airport in list_of_airport_dicts:
       city = airport["City"]
       passengers = int(airport['Passengers'])
       passengers_per_city[city] = passengers

    return passengers_per_city


# PROBLEM 4 (5 POINTS)

def main():
    """
    Parameters:
        None

    Returns:
        None
    """

    data = read_csv_file('airports.csv')
    city_passenger = passengers_per_city(data)
    city_passenger = sort_dictionary_by_value(city_passenger)
    write_csv_file("airports_ranked.csv", city_passenger, ('City','Passengers'))


# END CODING HERE

if __name__ == '__main__':
    main()
