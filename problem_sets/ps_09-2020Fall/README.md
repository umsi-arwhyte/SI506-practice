# SI 506: Problem Set 09

## This week's problem set

This week's problem set includes 7 problems. We will continue working with dictionaries, reading/writing files, and working with class instances, constructors, and methods.

## Background

This week, we will be working with the coolest part of Python: Classes! We will use meat consumption per capita of different countries, CO2 equivalent emission per kg consumption of different meat and other data to calculate the CO2 emission per capita and in total for a selective countries.

**country_population.csv** contains country code, name and population which is derived from [https://tradingeconomics.com/country-list/population?continent=g20]

**country_meat_consumption.csv** contains country code, meat type and meat consumption which is derived from [https://data.oecd.org/agroutput/meat-consumption.htm]

`meat_emission` in `main()` contains meat type and CO2 equivalent emission per kg meat consumption which is derived from [https://www.greeneatz.com/foods-carbon-footprint.html]

## 1.0 Problem 01 (20 Points)

Implement the constructor, `__init__()`, of the `Country` class.

The constructor will take the following parameters:

- self
- code
- name
- population

and assign each to an instance variable of the same name. In addition, the constructor should create three instance variables `self.meat_consumption_per_capita` which should be initialized as an empty dictionary, `self.meat_co2_emission_per_capita` and `self.meat_co2_emission_total` which both should be initialized as a float zero. We'll update them later in other class methods.

:bulb: Read the attributes section in Docstring to help you better understand the meaning of each parameter.

## 2.0 Problem 02 (20 Points)

Implement the method, `__str__()`, of the `Country` class.

The return value must adhere to the following format:
```
<name> (<code>) emitted <meat_co2_emission_per_capita> kg CO2 caused by meat consumption per capita and <meat_co2_emission_total> kg in total
```

## 3.0 Problem 03 (20 Points)

Implement the method, `add_meat_consumption()`, of the `Country` class.

Read the function Docstring for additional implementation details.


## 4.0 Problem 04 (20 Points)

Implement the method, `calculate_emission_per_capita()`, of the `Country` class.

Read the function Docstring for additional implementation details.

:bulb: Loop over items of <meat_consumption_per_capita>, calculate CO2 emission of each meat by meat consumption (kg) * CO2 emission equivalent per kg consumption and sum it together.

:bulb: Sample input & output

```python
# country is a Country instance
country.meat_consumption_per_capita = {"BEEF": 12, "PIG": 4}
meat_emission = {
        'BEEF': 27.0,
        'PIG': 12.1,
        'SHEEP': 39.2,
        'POULTRY': 6.9,}
country.calculate_emission_per_capita(meat_emission)
# The expacted value of country.meat_co2_emission_per_capita should be 
# 12*27.0 + 4*12.1
```

## 5.0 Problem 05 (20 Points)

Implement the method, `calculate_total_emission()`, of the `Country` class.

Read the function Docstring for additional implementation details.

## 6.0 Problem 06 (10 Points)

Implement the function `write_to_file()`.

Read the function Docstring for additional implementation details.

## 7.0 Problem 07 (90 Points)

Complete Problem 07 in `main()` function

### 7.1 (10 Points)

1. Call `read_csv` to read **country_population.csv** into a list of dictionary and assign it to a variable `country_population`.
2. Call `read_csv` to read **country_meat_consumption.csv** into a list of dictionary and assign it to a variable `country_meat_consumption`.

### 7.2 (20 Points)

1. Create an empty dictionary `countries`.
2. Loop over `country_population`, create instance of the `Country` class using data from each dictionary in the list, and add a key:value pair where key is the **code** of the country and value is the **country instance** to `countries`.
3. Convert the country instance for USA to `str` and assign the string value to the variable `usa`.

:bulb: You need to convert population from `str` to `float`. 

:bulb: In the **country_population.csv** file the population is expressed in terms of millions, but you want to add the population expressed in terms of ones. So if the csv file says the population is 1.1, then the population you want to pass into the class constructor should be 1100000

:bulb: The expected value of `usa` should be
```
United States (USA) emitted 0.0 kg CO2 caused by meat consumption per capita and 0.0 kg in total
```

### 7.3 (20 Points)

1. Loop over `country_meat_consumption` and add meat consumption to the country instances stored in the dictionary `countries`.
2. Assign the value of the attribute `meat_consumption_per_capita` of the country instance for USA to the variable `usa_meat_consumption_per_capita`.

:bulb: You need to convert consumption from `str` to `float` before creating the instance

### 7.4 (20 Points)

1. Loop over `countries`, calculate the emission per capita of each country instance using **the correct class method**. We provide the dictionary `meat_emission` which contains CO2 emission equivalent per kg of different meat.
2. Similar to **7.4.1**, calculate the total emission of each country instance using **the correct class method**.
3. Convert the country instance for USA to `str` and assign the string value to the variable `usa2`.

:bulb: The expected value of `usa2` should be
```
United States (USA) emitted 1364.214 kg CO2 caused by meat consumption per capita and 448826406000.0 kg in total
```

### 7.5 (20 Points)

1. Loop over `countries` and find out what are the country instances having the **most** and **least** CO2 emission caused by meat consumption **per capita** and assign the country instances to variables `max_country` and `min_country`. There are no ties for max or min values.
2. Write `max_country` and `min_country` to files **max_country.txt** and **min_country.txt** by calling the function `write_to_file()`.

### Return

To test class methods, functions, and generated files, you don't need to complete `main()` function.

To test `main()` function and intermediate variables, you need to return requested variables in order