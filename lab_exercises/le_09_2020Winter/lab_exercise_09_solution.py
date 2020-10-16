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

        self.title = title
        self.author = author


    def __str__(self):
        """
        String method for the <Book> class. Whenever an instance of <Book> is passed to the 
        str() or print() functions, the string from this method will be returned.

        Parameters:
            None

        Returns:
            str: A string representation of <Book> instance in the format "<title> by <author>"
        """
        return f"{self.title} by {self.author}"
        
# PROBLEM 2 (4 Points)

class Library():
    """
    This is a class that contains information on a Library.

    Attributes:
        books (list): List of book instances in the library.
        torn_pages_tolerance (int): Number of torn pages a book can have and the library will still accept

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

        self.books = []
        self.torn_pages_tolerance = 3


    def __str__(self):
        """
        String method for the <Library> class.

        Parameters:
            None

        Returns:
            str: A string representation of <Book> instance in the format:
                "This library contains <number of books> books"
                    
        """

        return f"This library contains {len(self.books)} books"

# PROBLEM 3 (2 Points)

    def will_accept(self, book):
        """
        Determines if the library will add a book instance to its collection
        depending on its conditions.

        If book instance is of Book class, return True.
        If book instance is of PaperbackBook class and the number of torn pages 
          is less than or equal to the library's torn page tolerance, return True.
        Else return False.
            HINT: there is a built-in isinstance() function to check what class an isntance
            came from

        Parameters:
            book: instance of any book class

        Returns:
            Boolean (True or False)
        """

        if isinstance(book, PaperbackBook):
            if book.num_torn_pages <= self.torn_pages_tolerance:
                return True
            else:
                return False
        else:
            return True

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

        if self.will_accept(book) == True:
            self.books.append(book)

# PROBLEM 5 (2 Points)

class PaperbackBook(Book): # <- remember to fill in () for class inheritence!
    """
    This is a PaperbackBook class that inherits from the Book class. It will inherit
    all attributes and methods from Book. You will overwrite the parent constructor 
    to add an additional property but inherit the string method as is.

     Attributes:
        title (str): The title of the book.
        author (str): The name of the author.
        num_torn_pages (int): The number of torn pages in the PaperbackBook.
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
        super().__init__(title, author)
        # or Book.__init__(self, title, author)
        self.num_torn_pages = 0
 
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
        self.num_torn_pages += 1
    
# PROBLEM 7 (4 Points)

def main():
    
    # 7.1 Create an instance of <Book>

    homer_odyssey = Book("The Odyssey", "Homer")

    # print instance of book
    print(homer_odyssey)

    # 7.2 Create an instance of <PaperbackBook>

    angelou_rise = PaperbackBook("And Still I Rise", "Maya Angelou")

    # print instance of PaperbackBook
    print(angelou_rise)

    # 7.3 Create an instance of <Library>

    lib = Library()

    # 7.4 Add book to the library

    lib.add_book(homer_odyssey)

    # 7.5 Increase number of torn pages
    
    for i in range(4):
        angelou_rise.rip_page()
    
    # 7.6 Set number of torn pages

    torn_pages = angelou_rise.num_torn_pages

    # 7.7 Try to add Paperbook to the library

    lib.add_book(angelou_rise)

    # 7.8 Print out the library's books
    
    print(lib.books)

# END CODING HERE - - - - - - - - - - - - - - - - - - - - - - - - - - - -

if __name__ == '__main__':
    main()
