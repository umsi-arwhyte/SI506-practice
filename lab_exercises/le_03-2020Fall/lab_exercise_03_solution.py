# START LAB EXERCISE 03
print('Lab Exercise 03 \n')

# SETUP
quote_str = """The greatest glory in living lies not in never falling, but in rising every time we fall.
You will face many defeats in life, but never let yourself be defeated
He who is not courageous enough to take risks will accomplish nothing in life.
It isn't where you came from it's where you're going that counts.
Real change, enduring change, happens one step at a time.
The journey of a thousand miles begins with one step."""

authors = "nelson mandela | muhammad ali | ella fitzgerald | ruth bader ginsburg | lao tzu"

# END SETUP

# PROBLEM 1.0 (5 Points)
# Convert quotes to list

quotes = quote_str.splitlines()

print(f"\nProblem 1.0 quotes = {quotes}")

restyled_authors = authors.title().split(' | ')

print(f"\nProblem 1.0 restyled authors = {restyled_authors}")

# PROBLEM 2.0 (5 Points)
restyled_authors.insert(1, "Maya Angelou")

print(f"\nProblem 2.0 = {restyled_authors}")

# PROBLEM 3.0 (5 Points)
american_authors = restyled_authors[1:5]
# american_authors = restyled_authors[-5:-1] # negative slicing

print(f"\nProblem 3.0 = {american_authors}")

# PROBLEM 4.0 (5 Points)
american_author_quotes = []
american_author_quotes.append(f"{american_authors[0]} - {quotes[1]}")
american_author_quotes.append(f"{american_authors[1]} - {quotes[2]}")
american_author_quotes.append(f"{american_authors[2]} - {quotes[3]}")
american_author_quotes.append(f"{american_authors[3]} - {quotes[4]}")

print(f"\nProblem 4.0 = {american_author_quotes}")

# END LAB EXERCISE

