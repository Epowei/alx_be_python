# book_class.py

class Book:
    def __init__(self, title, author, year):
        """
        Initialize a Book instance.

        :param title: str, the title of the book
        :param author: str, the author of the book
        :param year: int, the year the book was published
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor method to print a message when the object is deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        Returns a string representation of the book.

        :return: str formatted as "title by author, published in year"
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns a string that represents how to recreate the Book instance.

        :return: str that can be used to recreate this instance
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
