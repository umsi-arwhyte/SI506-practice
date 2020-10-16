# START LAB EXERCISE 9
print('LAB EXERCISE 09 \n')

# PROBLEM 1 (4 Points)

class Book(): 
    """
    This is a class that contains information on Books.

    Attributes:
        title (str): The title of the book.
        author (str): The name of the author.

    """
    def __init__(self, title, author): 
        """
        The constructor of the <Book> class. Here you will need to create
        the instance variables that were described in the docstring above. 
        Note that the attributes are defined by parameters passed to this constructor method.
        
        Parameters:
            title (str): The title of the book.
            author (str): The name of the author.

        Returns:
            None
        """

        pass # Implement


    def __str__(self):
        """
        String method for the <Book> class. Whenever an instance of <Book> is passed to the 
        str() or print() functions, the string from this method will be returned.

        Parameters:
            None

        Returns:
            str: A string representation of <Book> instance in the format "<title> by <author>"
        """
        pass # Implement

# PROBLEM 2 (4 Points)

class Library():
    """
    This is a class that contains information on a Library.

    Attributes:
        books (list): List of book instances in the library.
        torn_pages_tolerance (int): Number of torn pages a book can have and the library will still accept.

    """
    def __init__(self):
        """
        The constructor of the <Library> class. Here you will need to create instance variables
        described in the docstring above. The Library constructor should take NO positional arguments, but
        set instance variables <books> to an empty list and <torn_pages_tolerance> to 3.
        
        Parameters:
            None

        Returns:
            None
        """

        pass # Implement


    def __str__(self):
        """
        String method for the <Library> class.

        Parameters:
            None

        Returns:
            str: A string representation of <Book> instance in the format:
                "This library contains <number of books> books"
                    
        """

        pass # Implement

# PROBLEM 3 (2 Points)

    def will_accept(self, book):
        """
        Determines if the library will add a book instance to its collection
        depending on its conditions.

        if book instance is of Book class, return True.
        if book instance is of PaperbackBook class and the number of torn pages 
          is less than or equal to the library's torn page tolerance, return True.
        else return False.
            HINT: there is a built-in isinstance() function to check what class an isntance
            came from

        Parameters:
            book: instance of any book class

        Returns:
            Boolean (True or False)
        """

        pass # Implement

# PROBLEM 4 (2 Points)

    def add_book(self, book):
        """
        This method will modify the <books> attribute by appending the parameter <book>
        to it if the library will accept the book.
            HINT: call will_accept within this method to determine if book can be added

        Parameters:
            book: instance of any book class

        Returns:
            None
        """

        pass # Implement

# PROBLEM 5 (2 Points)

class PaperbackBook(Book): # <- remember to fill in () for class inheritence!
    """
    This is a PaperbackBook class that inherits from the Book class. It will inherit
    all attributes and methods from Book. You will overwrite the parent constructor 
    to add an additional property but inherit the string method as is.

     Attributes:
        title (str): The title of the book.
        author (str): The name of the author.
        num_torn_pages (int): The number of torn pages in the PaperBook.
        
    """

    def __init__(self, title, author):
        """
        The constructor of the <PaperbackBook> class. Here you will need to inherit the attributes 
        from the parent class, but add an additional instance variable <num_torn_pages> 
        and initialize it to 0. Note that the constructor takes two positional arguments, but will
        set three instance variables.
        
        Parameters:
            title (str): The title of the book.
            author (str): The name of the author.

        Returns:
            None
        """

        pass # Implement

# PROBLEM 6 (2 Points)

    def rip_page(self):
        """
        This method will modify the <num_torn_pages> and increase it by one every time the
        method is called.

        Parameters:
            None

        Returns:
            None
        """
        pass # Implement

# PROBLEM 7 (4 Points)
    
def main():

    # 7.1 Create an instance of <Book>

    homer_odyssey = None

    # print instance of book
    print(homer_odyssey)

    # 7.2 Create an instance of <PaperbackBook>

    angelou_rise = None

    # print instance of PaperbackBook
    print(angelou_rise)

    # 7.3 Create an instance of <Library>

    lib = None

    # 7.4 Add book to the library

    pass # Implement

    # 7.5 Increase number of torn pages

    pass # Implement

    # 7.6 Set number of torn pages

    torn_pages = None

    # 7.7 Try to add Paperbook to the library

    pass # Implement

    # 7.8 Print out the library's books

    pass # Implement

# END CODING HERE - - - - - - - - - - - - - - - - - - - - - - - - - - - -

if __name__ == '__main__':
    main()
