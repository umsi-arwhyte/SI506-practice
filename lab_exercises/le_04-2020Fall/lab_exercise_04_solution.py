# START LAB EXERCISE 04
print('Lab Exercise 04 \n')


# SETUP

city_state =  ["Detroit|MI", "Philadelphia|PA", "Hollywood|CA",
            "Oakland|CA", "Boston|MA", "Atlanta|GA",
            "Phoenix|AZ", "Birmingham|AL", "Houston|TX", "Tampa|FL"]

# PROBLEM 1

cali = city_state[2:4]

# PROBLEM 2

us_cities = []

for city in city_state:
    city_names = city.split('|')[0]
    us_cities.append(city_names)

# PROBLEM 3

southern_cities = []

for city in us_cities:
    index = us_cities.index(city)
    if index > 4:
        southern_cities.append(city)
