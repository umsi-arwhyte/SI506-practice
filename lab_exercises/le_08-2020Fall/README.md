# SI 506: Lab Exercise 08

## This week's Lab Exercise

This week's lab exercise focuses on working with files using information on databases provided by the University of Michigan Library.

## Data description

The data contains information on databases the University of Michigan Library provides access to for students, faculty, and staff. Databases are a library search engine focused on a specific subject or a series of subjects. For this lab exercise, in `library_databses.csv` there are a few databases in African Studies, Art & Design, Health Management & Policy, Human Computer Interaction, and Population & Demography.

`library_databases.csv` includes information on the category, name, type, format, description, and a link for each database. Source: https://search.lib.umich.edu/databases

## 1.0 Problem 01 (5 Points)

Implement the `read_csv_file()` function.

The `read_csv_file()` function will take a filepath, such as `library_databases.csv`, and a delimiter as its parameters. Use the `csv.DictReader()` method to read the file. The return value of this function will comprise a list of dictionaries.

For example if the input file is structured like this:

```python
country,state,county
United States,California,Orange
United States,Michigan,Washtenaw

```

The `read_csv_file` function will alter that file to be structured like this:

```python
[
    {
    "country": "United States",
    "state": "California",
    "county": "Orange"
    },
    {
    "country": "United States",
    "state": "Michigan",
    "county": "Washtenaw"
    }
]
```

## 2.0 Problem 02 (5 Points)

Implement the `hci_database_links()` function.

This function takes a list of library data (e.g. the return from `read_csv_file()`),
and returns a new dictionary of databases only in the `Human Computer Interaction` (HCI) category.
The output dictionary should have the format:

```python
{
    "Database": Name of HCI Database
    "Link": https://app.lib.umich.edu.hcinumber
}
```

## 3.0 Problem 03 (5 Points)

Implement the `write_csv_file()` function.

Writes a .csv file using the `csv` module. The file will contain the information from `hci_database_urls()`, where each row of the new .csv file is one of the key/value pairs. In other words, the output file should have two columns. Don't forget to include the header to each column, which is given to this function in the parameter < header >. The names of the header names are "database" and "url". The resultant file should be structured in the following way:

```python
    < header[0] >, < header[1] >
    key1, value1
    key2, value2
    key3, value3
    ...etc
```

## 4.0 Problem 04 (5 Points)

Implement the `main()` function.

There are three steps to this section.
1. Read in the data from `library_databses.csv`.
2. Parse that data and create a new dictionary with only the HCI databases information using `hci_database_urls()`.
3. Write the sorted dictionary to a new file `library_hci_databases.csv`.

:hint: Don't forget to include headers that are tuples into the `library_hci_databases.csv` file!

:exclamation: You will need to call each of the functions in this script to complete this task.
