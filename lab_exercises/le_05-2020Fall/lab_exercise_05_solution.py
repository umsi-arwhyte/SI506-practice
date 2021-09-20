# START LAB EXERCISE 05
print('Lab Exercise 05 \n')

# SETUP

record = [
    ['school', 'year', 'won', 'lost', 'win_percent', 'bowl_appear', 'bowl_win'],
    ['Michigan', 2019, 9, 4, None, True, False],
    ['Michigan', 2018, 10, 3, None, True, False],
    ['Michigan', 2017, 8, 5, None, True, False],
    ['Michigan', 2016, 10, 3, None, True, False],
    ['Michigan', 2015, 10, 3, None, True, True],
    ['Michigan', 2014, 5, 7, None, False, False],
    ['Michigan', 2013, 7, 6, None, True, False],
    ['Michigan', 2012, 8, 5, None, True, False],
    ['Michigan', 2011, 11, 2, None, True, True],
    ['Michigan', 2010, 7, 6, None, True, False],
    ['Michigan', 2009, 5, 7, None, False, False],
    ['Michigan', 2008, 3, 9, None, False, False],
    ['Michigan', 2007, 9, 4, None, True, True],
    ['Michigan', 2006, 11, 2, None, True, False],
    ['Michigan', 2005, 7, 5, None, True, False],
    ['Michigan', 2004, 9, 3, None, True, False],
    ['Michigan', 2003, 10, 3, None, True, False],
    ['Michigan', 2002, 10, 3, None, True, True],
    ['Michigan', 2001, 8, 4, None, True, False],
    ['Michigan', 2000, 9, 3, None, True, True]
]

print(f"\nRecord = {record}")

# END SETUP

# PROBLEM 1
def calculate_win_percentage(wins, losses):
    return round(wins / (wins + losses), 3)

# PROBLEM 2
for year in record[1:]:
    year_win_percent = calculate_win_percentage(year[2], year[3])
    year[-3] = year_win_percent

print(f"\nRecord updated = {record}")

# PROBLEM 3
record_wins = 0
record_losses = 0

for year in record[1:]:
    record_wins += year[2]
    record_losses += year[3]

record_win_percent = calculate_win_percentage(record_wins, record_losses)

print(f"\n2000-2019: wins = {record_wins}; losses = {record_losses}; win percentage = {record_win_percent}")

# PROBLEM 4

def calculate_best_year(record):
    best_year = None
    high_score = 0.0

    for year in record[1:]:
        if year[4] > high_score:
            high_score = year[4]
            best_year = year[1]
        elif year[4] == high_score and year[5] == True and year[6] == True:
            best_year = year[1]
    return best_year

def calculate_worst_year(record):
    worst_year = None
    low_score = 1.0

    for year in record[1:]:
        if year[4] <  low_score:
                low_score = year[4]
                worst_year = year[1]
    return worst_year

best_year = calculate_best_year(record)
worst_year = calculate_worst_year(record)

print(f"\nBest year: {best_year}; worst year: {worst_year}")

