## START LAB EXERCISE 4
print('Lab Exercise 04 \n')

# BACKGROUND
# The mission of CAPS to foster the psychological development and
# emotional well-being of students. If you or someone you know is feeling
# overwhelmed, depressed, and/or in need of support, services are available.
# For help, contact Counseling and Psychological Services (CAPS) at
# (734) 764-8312 and https://caps.umich.edu/ during and after hours,
# on weekends and holidays.

# We provide you with a select list of
# Counseling And Psychological Services (CAPS) embedded staff members at
# different schools across the University of Michigan. In the future,
# the teaching team will provided you such data in a file
# which you will read into Python with some useful functions.
# However, for today, the teaching team has provided this list for you.

# Data Description:

# Each item in the caps_staff list is a string containing the name,
# the degree, the school, and email address of each CAPS staff member.
# Each data point relating to the staff member is separated by a
# pipe ('|') delimiter.

caps_staff = [
    "Nidaa Shaikh|Psychologist|College of Engineering|nfkazi@umich.edu",
    "Laura Monschau|Psychologist|Rackham Gradate School|lauralm@umich.edu",
    "Meaghan Narula|Social Worker|School of Public Health|mbnarula@umich.edu",
    "Julie Kaplan|Social Worker|Ross School of Business|jrkaplan@umich.edu",
    "Alejandro Rojas|Social Worker|School of Social Work|aroja@umich.edu"
    ]

# END SETUP


# PROBLEM 1 (2.5 Points)
# Replace 'None' with the first staff member in < caps_staff >.
# Use their index value.

# BEGIN PROBLEM 1 SOLUTION

nfkazi = caps_staff[0]
print(nfkazi)

# END PROBLEM 1 SOLUTION


# PROBLEM 2 (2.5 Points)
# Replace 'None' with the first staff member in < caps_staff >.
# Use their index value.

# BEGIN PROBLEM 2 SOLUTION

aroja = caps_staff[-1]
print(aroja)
#You can also use forward indexing with 4#

# END PROBLEM 2 SOLUTION


# PROBLEM 3 (5 Points)
# Use list slicing to replace 'None' with the social workers from < caps_staff >.

# BEGIN PROBLEM 3 SOLUTION

social_workers = caps_staff[2:5]
print(social_workers)

# END PROBLEM 3 SOLUTION


# PROBLEM 4 (5 Points)
# Create a list of CAPS staff member names called < names_of_staff >.

# BEGIN PROBLEM 4 SOLUTION

names_of_staff = []
for i in caps_staff:
    name = i.split('|')[0]
    names_of_staff.append(name)

print(names_of_staff)

# END PROBLEM 4 SOLUTION


# PROBLEM 5 (5 Points)
# Implement < thank_you_caps_staff() > function

# BEGIN PROBLEM 5 SOLUTION

def thank_you_caps_staff(names_of_staff):
    """This function will loop through a list (ie. < names_of_staff >)
    and returns an appreciative statement for each item in the list
    (ie. thank you, < name_of_staff_member >).

    Parameters:
        names_of_staff (list): staff member names

    Returns:
        None (but prints out 'Thank you, < name_of_staff_member >'.)
    """

    for name in names_of_staff:
        print(f"Thank you, {name}.")


thank_you_caps_staff(names_of_staff)

# END PROBLEM 5 SOLUTION

## END LAB EXERCISE 04