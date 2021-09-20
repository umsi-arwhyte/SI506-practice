# SI 506: Lab Exercise 03

## This week's Lab Exercise

This week's lab exercise includes four (4) problems that focus on string
and list operations, including slicing.

## 1.0 Problem 01 (5 Points)

The variable `quote_str` is a multiline string of inspirational quotes. Split the multiline string
`quote_str` into a list of individual quotes and assign the new list to `quotes`.

```python
quote_str = """The greatest glory in living lies not in never falling, but in rising every time we fall.
You will face many defeats in life, but never let yourself be defeated
He who is not courageous enough to take risks will accomplish nothing in life.
It isn't where you came from it's where you're going that counts.
Real change, enduring change, happens one step at a time.
The journey of a thousand miles begins with one step."""
```

The variable `authors` is a string containing authors for the quotes in `quotes`. First, restyle the
authors within the string `authors` by capitalizing all of the author's names. For example,
'nelson mandela' must be restyled to 'Nelson Mandela'.

:bulb: there is a `str` method that you can use to capitalize both the first and last name of each
author.

Next, split the restyled `authors` string into a list method and assign the list to
`restyled_authors`. The resulting list must match the following list:

```python
['Nelson Mandela', 'Muhammad Ali', 'Ella Fitzgerald', 'Ruth Bader Ginsburg', 'Lao Tzu']
```

## 2.0 Problem 02 (5 Points)

There is an author missing from the list. The second quote in `quotes` belongs
Maya Angelou. Insert 'Maya Angelou' into the second position in `restyled_authors`.
The resulting list must match:

```python
['Nelson Mandela', 'Maya Angelou', 'Muhammad Ali', 'Ella Fitzgerald', 'Ruth Bader Ginsburg', 'Lao Tzu']
```

## 3.0 Problem 03 (5 Points)

Use slicing to return a list containing the following authors in the following order from the
`restyled_authors` list:

1. Maya Angelou
2. Muhammad Ali
3. Ella Fitzgerald
4. Ruth Bader Ginsburg

Assign the new list to a variable named `american_authors`.

```python
['Maya Angelou', 'Muhammad Ali', 'Ella Fitzgerald', 'Ruth Bader Ginsburg']
```

## 4.0 Problem 04 (5 Points)

Create an empty list named `american_author_quotes`. Append to the list each American author along
with their inspirational quote, using an f-string to format the string to be added to the new list
as follows:

`<author> - <quote>`

:exclamation: You can match each American author to their respective quote by relying on the
ordering of elements in both `restyled_authors` and `quotes`. For example, restyled_authors[0]
is the author of quote[0], and so on.
