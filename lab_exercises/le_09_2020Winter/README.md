# SI 506: Lab Exercise 09

## This Week's Lab
This week's lab focuses on working with classes, but more particularly on class inheritance. You will define three classes (`Book`, `Library`, `PaperbackBook`). `PaperbackBook` will inherit from the parent `Book` class. You will then create instances of the different kinds of books and add them to your "library".

## 1.0 Problem 01 (4 Points)

Implement the `Book` parent class.

Instance Variables:

* `title` (str): The title of the book.
* `author` (str): The name of the author.

### 1.1 Implement the `__init__()` method

The constructor will take the following arguments:

* `self`
* `title`
* `author`

and assign each to an instance variable of the same name.

Replace the `pass` statements with the appropriate code blocks. Read the class and method Docstrings for additional implementation details.

### 1.2 Implement the `__str__()` method

Implement the `__str__()` method of the `Book` class by replacing the `pass` statement with the appropriate code block. Read the function Docstring for additional implementation details.

## 2.0 Problem 02 (4 Points)

Implement the `Library` class.

Instance Variables:

* `books` (list): List of book instances in the library.
* `torn_pages_tolerance` (int): Number of torn pages a book can have and the library will still accept.

### 2.1 Implement the `__init__()` method

The constructor will take the following arguments:

* `self`
* `books`
* `torn_pages_tolerance`

and assign each to an instance variable of the same name.

Replace the `pass` statements with the appropriate code blocks. Read the class and method Docstrings for additional implementation details.

### 2.2 Implement the `__str__()` method

Implement the `__str__()` method of the `Library` class by replacing the `pass` statement with the appropriate code block. Read the function Docstring for additional implementation details.

## 3.0 Problem 03 (2 Points)

Implement the `Library` class `will_accept()` method of the `Library` class by replacing the `pass` statement with the appropriate code block. Read the function Docstring for additional implementation details.

## 4.0 Problem 04 (2 Points)

Implement the `Library` class `add_book()` method of the `Library` class by replacing the `pass` statement with the appropriate code block. Read the function Docstring for additional implementation details.

## 5.0 Problem 05 (2 Points)

Implement the `__init__()` method of `PaperbackBook` child class.

Instance Variables:

* `title` (str): The title of the book.
* `author` (str): The name of the author.
* `num_torn_pages` (int): The number of torn pages in the PaperBook.

The constructor will take the following arguments:

* `self`
* `title`
* `author`
* `num_torn_pages`

and assign each to an instance variable of the same name.

:exclamation: Use the `super()` function to inherit the attributes from the `Book` parent class.

Replace the `pass` statements with the appropriate code blocks. Read the class and method Docstrings for additional implementation details.

## 6.0 Problem 06 (2 Points)

Implement the `rip_page()` method of the `PaperbackBook` class by replacing the `pass` statement with the appropriate code block. Read the function Docstring for additional implementation details.

## 7.0 Problem 07 (4 Points)

Implement `main()` following the hints provided below.

### 7.1 Create an instance of `Book`

1. Create an instance of Book class with title = "The Odyssey" and author = "Homer".
2. Assign the instance to variable `homer_odyssey`.

### 7.2 Create an instance of `PaperbackBook`

1. Create an instance of PaperbackBook class with title = "And Still I Rise" and author = "Maya Angelou".
2. Assign the instance to variable `angelou_rise`.

### 7.3 Create an instance of `Library`

1. Create an instance of Library class.
2. Assign it to the variable `lib`.

### 7.4 Add book to the library

Add book `homer_odyssey` to the library `lib`.

### 7.5 Increase number of torn pages

Increase `num_torn_pages` of book `angelou_rise` to 4 by calling `rip_page` method 4 times in a row.

:bulb: you can do this using a for loop and the range() function.

Note: each call increases `num_torn_pages` by 1.

### 7.6 Set number of torn pages

Set `torn_pages` equal to the number of torn pages of `angelou_rise`. 

:warning: Use the instance variable, do not hard code a number.

### 7.7 Try to add Paperbook to the library

Try to add `angelou_rise` to the library -- it shouldn't be added because the num_torn_pages is too high.

### 7.8 Print out the library's books

There should be only one book in the library.