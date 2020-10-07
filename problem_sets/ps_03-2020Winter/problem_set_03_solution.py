# START PROBLEM SET 03
print('PROBLEM SET 03 \n')

# SETUP - DO NOT MODIFY

# Use the < nintendo_consoles > list for problems 1 and 2

nintendo_consoles = [
    "Famicom/Nintendo Entertainment System (NES), released: 1983",
    "Super Famicom/Super Nintendo Entertainment System (SNES), released: 1990",
    "Nintendo 64 (N64), released: 1996",
    "GameCube, released: 2001",
    "Wii, released: 2006",
    "Wii U, released: 2012",
    "Nintendo Switch, released: 2017"
    ]

# END SETUP

# PROBLEM 1 (20 points)

# BEGIN CODING

# Using the < nintendo_consoles > list and your knowledge of list slicing and indexing,
# create new list variables as directed. Replace `pass` with your code.

# Index all the Nintendo consoles that were released from 1980 - 1989
eighties_consoles = nintendo_consoles[0]

# Index all the Nintendo consoles that were released from 1990 - 1999
nineties_consoles = nintendo_consoles[-6:-4]

# Index all the Nintendo consoles that were released from 2000 - 2009
aughts_consoles = nintendo_consoles[3:5]

# Index all the Nintendo consoles that were released from 2010 - 2019
teens_consoles = nintendo_consoles[5:]

# END CODING

print(f"""\nProblem 1:\neighties_consoles = {eighties_consoles}
nineties_consoles = {nineties_consoles}
aughts_consoles = {aughts_consoles}
teens_consoles = {teens_consoles}""")

# END PROBLEM 1


# PROBLEM 2 (20 points)

# Create a new list called < release_years > that contains all of the years
# in which Nintendo released a television-based video game console.

# Example of what your < release_years > list should look like:
# [ "1983", "1990", ... etc. ]

# BEGIN CODING

release_years = []

for console in nintendo_consoles:
    year = console.split(": ")[1]
    release_years.append(year)

# END CODING

print(f"\nProblem 2:\nrelease_years = {release_years}")

# END PROBLEM 2


# SETUP - DO NOT MODIFY

# Use the < vg_consoles > list for problems 3 - 5

vg_consoles = [
    "Odyssey,Magnavox,1st Generation,1972,100000",
    "Atari 2600,Atari,2nd Generation,1977,30000000",
    "ColecoVision,Coleco Industries,2nd Generation,1980,2000000",
    "Intellivision,Mattel Electronics,2nd Generation,1982,3000000",
    "Famicom/Nintendo Entertainment System (NES),Nintendo,3rd Generation,1983,61910000",
    "Master System,Sega,3rd Generation,1985,13000000",
    "Atari 7800,Atari,3rd Generation,1986,3770000",
    "Super Famicom/Super Nintendo Entertainment System (SNES),Nintendo,4th Generation,1990,49100000",
    "Mega Drive/Genesis,Sega,4th Generation,1988,30750000",
    "Saturn,Sega,5th Generation,1994,9260000",
    "PlayStation,Sony,5th Generation,1994,102490000",
    "Nintendo 64 (N64),Nintendo,5th Generation,1996,32930000",
    "Dreamcast,Sega,6th Generation,1998,9130000",
    "PlayStation 2,Sony,6th Generation,2000,155000000",
    "GameCube,Nintendo,6th Generation,2001,21740000",
    "Xbox,Microsoft,6th Generation,2001,24000000",
    "Xbox 360,Microsoft,7th Generation,2005,84700000",
    "PlayStation 3,Sony,7th Generation,2006,87400000",
    "Wii,Nintendo,7th Generation,2006,101630000",
    "Wii U,Nintendo,8th Generation,2012,13560000",
    "PlayStation 4,Sony,8th Generation,2013,102800000",
    "Xbox One,Microsoft,8th Generation,2013,46900000",
    "Nintendo Switch,Nintendo,9th Generation,2017,47300000"
    ]

# END SETUP

# PROBLEM 3 (20 points)

def filter_by_units_sold(console,minimum_units_sold):
    """
    This function will parse a string (i.e. one of the elements of < vg_consoles >),
    and return True if the number of units sold was higher than < minimum_units_sold >,
    or False if the number of units sold was lower than < minimum_units_sold >.

    Parameters:
        - console (str): A string containing all of the information on the console (i.e.
            an element from < vg_consoles >).
        - minimum_units_sold (int): An integer to compare the number of units sold against.

    Returns:
        - (bool): True or False, depending on if the number of units sold in < console > are
            greater than < minimum_units_sold > or not.
    """

    data = console.split(',')
    num_units = int(data[-1])

    if num_units > minimum_units_sold:
        return True
    else:
        return False


# When you have finished < filter_by_units_sold >, uncomment the below lines to test your
# function:
print(f"\nProblem 3:\nThis should print False: {filter_by_units_sold(vg_consoles[0],100000)}")
print(f"This should print True: {filter_by_units_sold(vg_consoles[0],1000)}")

# END PROBLEM 3


# PROBLEM 4 (20 Points)

def format_string(console):
    """
    This function accepts a string of video game console data, delmited by commas (e.g. an
    element from < vg_consoles >), and returns a formatted string.

    Parameters:
        - console (str): A string containing all of the information on the console (i.e.
            an element from < vg_consoles >).

    Returns:
        - (str): A string that has formatted the information from < console > in the following
            format:

            "< Console name > was produced in < Release year > by < Production company >"
    """

    data = console.split(',')
    name = data[0]
    year = data[3]
    company = data[1]

    return f"{name} was produced in {year} by {company}"


# When you have finished < format_string >, uncomment the below lines to test your
# function:
print(f"\nProblem 4:\nThe following two lines should be the same:")
print("Odyssey was produced in 1972 by Magnavox")
print(f"{format_string(vg_consoles[0])}")

# END PROBLEM 4


# PROBLEM 5 (20 Points)

def main(console_list):
    """
    This function takes a list of video game console data (i.e. < vg_consoles >) as an
    argument, and returns a list showing formatted information on the consoles that
    were extremely commercially succesful (sold more than 100,000,000 units). In order
    to do so, this function will loop over < console_list >, determine which elements have
    sold more than 100,000,000 units, and then format them and add them to the returned
    list.

    Parameters:
        - console_list (list of str): A list of strings containing comma-delimited information
            on video game consoles (i.e. < vg_consoles >)

    Returns:
        - (list of str): A list of strings, where each string is an instance of a video game
            console that has sold more than 100,000,000 units, formatted by < format_string >
    """

    succesful = []

    for console in console_list:
        if filter_by_units_sold(console,100000000):
            succesful.append(format_string(console))

    return succesful


# When you are finished with your < main > function, uncomment the below lines.
print(f"\nProblem 5:\nThe following line should include: PlayStation, PlayStation 2, PlayStation 4, and Wii")
print(f"{main(vg_consoles)}")

# END PROBLEM 5

# END PROBLEM SET
