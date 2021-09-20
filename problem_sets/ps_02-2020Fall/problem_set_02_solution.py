# START PROBLEM SET 02
print('Problem Set 02')

# PROBLEM 1 (20 points)
print('\nProblem 1')

cases = [11, 10, 38, 19, 27]

cases_latest = cases[-1]

cases[0] = 9

print(cases)

# PROBLEM 2 (20 points)
print('\nProblem 2')

tests = [867, 854, 1494, 1712, 1667]

tests_max = max(tests)

tests_max_index = tests.index(tests_max)

print(tests_max,  tests_max_index)

# PROBLEM 3 (20 points)
print('\nProblem 3')

weeks = ' Aug.09,Aug.16,Aug.23,Aug.30,Sep.06 '

weeks_list = weeks.strip().replace('.', '').split(',')
print(weeks_list)

# PROBLEM 4 (20 points)
print('\nProblem 4')

weeks_new = '|'.join(weeks_list)

aug_count = weeks_new.count('Aug')

print(weeks_new)
print(aug_count)

# PROBLEM 5 (20 points)
print('\nProblem 5')

cases_max_index = cases.index(max(cases))

most_tests = f"In the week starting on {weeks_list[tests_max_index]}, UM has conducted {tests[tests_max_index]} tests and reported {cases[tests_max_index]} cases."

most_cases = f"In the week starting on {weeks_list[cases_max_index]}, UM has conducted {tests[cases_max_index]} tests and reported {cases[cases_max_index]} cases."

print(most_tests)
print(most_cases)