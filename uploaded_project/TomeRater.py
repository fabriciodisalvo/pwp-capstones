# Codecademy Intensive
# Programming with Python
# TomeRater Capstone Project


"""
NOTES TO REVIEWER:
-----------------

a. I have no idea how to write documentation. I am not sure if I should write it to another programmer ("Input user name as string")or to a user of the program that doesnt know anything about python ("Please enter a user name").

b. I can't seem to underderstand how to keep my lines under 79 characters. Any input on that? :) 

c. For the price related to books, I took the following approach: books have different prices in different places, people pay different amounts for the same thing. So instead of assigning a price to each book, I consider prices to work as ratings: each user has one per book. So, to calculate the most expensive books, i need to use the average of what people has paid for it. To calculate a user's collection value, I average those purchase prices as well, so it is considered how much her/his books costs in average, not how much she/he paid for them...

d. Would you guys publish one recommended solution to the project? 

e. This project was really fun.
"""

class User(object):
    """A User class to create users associated with their emails.
    Arguments:
    name -- User name as a string.
    email -- The user's email as a string.
    """

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        """Returns the email address of the user."""
        return self.email

    def change_email(self, address):
        """Updates the email address of the user."""
        self.email = address
        print('The user email address has been updated.')

    def read_book(self, book, rating=None):
        """Adds a Book to the user's read-list.
        Arguments:
        book -- A book object to be added.
        rating -- The user's rating, as an integer, from 0 to 4. (default = None).
        """
        if rating in range(5):
            self.books[book] = rating
        elif rating is None:
            self.books[book] = None
        else:
            print('Invalid Rating. Rating must be between 0 and 4.')

    def get_average_rating(self):
        """Returns an average of all given ratings by the user."""
        try:
            rolling_sum = 0
            rolling_count = 0
            for i in self.books.values():
                if i is not None:
                    rolling_sum += i
                    rolling_count += 1
            return rolling_sum / rolling_count
        except ZeroDivisionError:
            return 0

    def __repr__(self):
        return ('user: {}, \nemail: {}, \nbooks read : {}'.format(self.name, self.email, self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            print('Both objects are equal')
            return True
        else:
            return False


class Book(object):
    """A Book class to create books associated with their ISBNs.
    Arguments:
    title -- Book's title, without author.
    isbn -- The book-s ISBN as integer (no dashes).
    """

    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []
        self.prices = []

    def get_title(self):
        """Returns the title of the book."""
        return self.title

    def get_isbn(self):
        """Returns the isbn of the book."""
        return self.isbn

    def set_isbn(self, isbn):
        """Updates the isbn of the book."""
        if type(isbn) is int:
            self.isbn = isbn
            print('ISBN has been updated.')
        else:
            print('ISBN should be an integer. Please try again.')

    def add_rating(self, rating):
        """Adds a user rating to the book, as an integer from 0 to 4."""
        if rating in range(5):
            self.ratings.append(rating)
        elif rating is None:
            pass
        else:
            print('Invalid Rating')

    def add_purchase_price(self, price):
        """Adds a user purchase price to the book, as an float
         with no limits (some people spend a lot of money on books).
        """
        if price is None:
            pass
        elif price < 0:
            print('Invalid Price')
        else:
            self.prices.append(price)

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            print('They are equal')
            return True

    def get_average_rating(self):
        """Returns an average of all given ratings to this title."""
        try:
            rolling_sum = 0
            rolling_count = 0
            for i in self.ratings:
                if i is not None:
                    rolling_sum += i
                    rolling_count += 1
            return rolling_sum / rolling_count
        except ZeroDivisionError:
            return 0

    def get_average_price(self):
        """Returns an average of all purchasing prices to this title."""
        try:
            rolling_sum = 0.00
            rolling_count = 0.00
            for i in self.prices:
                if i is not None:
                    rolling_sum += i
                    rolling_count += 1
            return rolling_sum / rolling_count
        except ZeroDivisionError:
            return 0.00

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return str('{}'.format(self.title))


class Fiction(Book):
    """A subclass of Book.
    Arguments:
    title -- Book's title as a string.
    author -- Book's author or authors, as a string.
    isbn -- The book-s ISBN as integer (no dashes).
    """

    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        """Returns the author or authors of this title."""
        return self.author

    def __repr__(self):
        return '{} by {}'.format(self.title, self.author)


class Non_Fiction(Book):
    """A subclass of Book.
    Arguments:
    title -- Book's title as a string.
    subject -- Book's subject or general theme, as a string.
    level -- Level of difficulty of this volume.
    isbn -- The book-s ISBN as integer (no dashes).
    """

    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        """Returns the subject of this title."""
        return self.subject

    def get_level(self):
        """Returns the Level of difficulty of this title."""
        return self.level

    def __repr__(self):
        return '{}, a {} manual on {}'.format(self.title, self.level, self.subject)


class TomeRater():
    """A class object to handle a group of users, the books that they have read, and the rating the have assigned to those volumes.
    """

    def __init__(self):
        self.users = {}
        """ Dictionary with emails as keys, user objects as values."""
        self.books = {}
        """ Dictionary with books objects as keys, times read as values."""
        self.isbn_list = []

    def create_book(self, title, isbn):
        """Creates a book object.
        Arguments:
        title -- Book's title, without author.
        isbn -- The book-s ISBN as integer (no dashes)
        """
        if isbn in self.isbn_list:
            print('This book has already been created!')
        else:
            self.isbn_list.append(isbn)
            return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        """Creates a novel, a book-type object.
        Arguments:
        title -- Book's title as a string.
        author -- Book's author or authors, as a string.
        isbn -- The book-s ISBN as integer (no dashes).
        """
        if isbn in self.isbn_list:
            print('This book has already been created!')
        else:
            self.isbn_list.append(isbn)
            return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        """Creates a non-fiction book, a book-type object.
        Arguments:
        title -- Book's title as a string.
        subject -- Book's subject or general theme, as a string.
        level -- Level of difficulty of this volume.
        isbn -- The book-s ISBN as integer (no dashes).
        """
        if isbn in self.isbn_list:
            print('This book has already been created!')
        else:
            self.isbn_list.append(isbn)
            return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None, price=None):
        """Adds a Book to the user's read-list.
        Arguments:
        book -- A book object to be added.
        email - An email address, as a string. Note: The user must already be created using this email as unique identifier.
        rating -- The user's rating, as an integer, from 0 to 4. (default = None).
        """
        if email in self.users.keys():
            self.users[email].read_book(book.title, rating)
            book.add_rating(rating)
            book.add_purchase_price(price)
            if book in self.books.keys():
                self.books[book] = self.books[book] + 1
            else:
                self.books[book] = 1
        else:
            print('No user with email {}'.format(email))

    def add_user(self, name, email, user_books=None):
        """Adds a User to the user's list.
        Arguments:
        name -- User name as a string.
        email -- The user's email as a string.
        user_books -- A list of book objects read by the user. (default = None).
        """
        if email in self.users.keys():
            print('User already in database.')
        if '@' in email and ('.com' in email or '.edu' in email or '.org' in email):
            self.users[email] = User(name, email)
            if user_books is not None:
                for i in user_books:
                    self.add_book_to_user(i, email)
        else:
            print('Check email address format and retry')

    def print_catalog(self):
        """Prints the full book catalogue (only titles)."""
        for i in self.books.keys():
            print(i.title)

    def print_users(self):
        """Prints the full user list (only names)."""
        for i in self.users.values():
            print(i.name)

    def get_most_read_book(self):
        """Returns the most read book of the catalogue."""
        the_most_read_book = 'No book is more popular than the rest'
        reading_rolling_sum = 0
        for i in self.books.keys():
            if self.books[i] > reading_rolling_sum:
                reading_rolling_sum = self.books[i]
                the_most_read_book = i
        return the_most_read_book

    def highest_rated_book(self):
        """Returns the highest rated read book of the catalogue."""
        the_highest_rating = 0
        for i in self.books.keys():
            if i.get_average_rating() > the_highest_rating:
                the_highest_rating = i.get_average_rating()
                the_highest_rated_book = i
        return the_highest_rated_book.title

    def most_positive_user(self):
        """Returns the most positive user, based on available ratings."""
        the_most_positive_user = 'All users are quite positive'
        the_highest_rating = 0
        for i in self.users.values():
            if i.get_average_rating() > the_highest_rating:
                the_most_positive_user = i
        return the_most_positive_user.name

    def get_n_most_read_books(self, n):
        """Returns the most read books.
        Arguments:
        n -- number of books that we want returned.
        """
        the_most_read_book_dict = {}
        n = min(len(self.books), n)
        for j in range(n):
            reading_rolling_sum = 0
            for i in self.books.keys():
                if i.title not in the_most_read_book_dict.keys():
                    if self.books[i] > reading_rolling_sum:
                        reading_rolling_sum = self.books[i]
                        the_most_read_book = i.title
            the_most_read_book_dict[the_most_read_book] = reading_rolling_sum
        return the_most_read_book_dict

    def get_n_most_prolific_readers(self, n):
        """Returns the users with the most read books.
        Arguments:
        n -- number of users that we want returned.
        """
        the_most_prolific_dict = {}
        n = min(len(self.users), n)
        for j in range(n):
            reading_rolling_sum = 0
            for i in self.users.values():
                if i.name not in the_most_prolific_dict.keys():
                    if len(i.books) > reading_rolling_sum:
                        reading_rolling_sum = len(i.books)
                        prolific_user = i.name
            the_most_prolific_dict[prolific_user] = reading_rolling_sum
        return the_most_prolific_dict

    def get_n_most_expensive_books(self, n):
        """Returns the books with the higher price tags.
        Arguments:
        n -- number of books that we want returned.
        """
        n = min(len(self.books), n)
        the_most_expensive_books = {}
        for j in range(n):
            pricing_sum = 0.00
            for i in self.books:
                if i.title not in the_most_expensive_books.keys():
                    if i.get_average_price() > pricing_sum:
                        pricing_sum = i.get_average_price()
                        expensive_book = i.title
            the_most_expensive_books[expensive_book] = pricing_sum
        return the_most_expensive_books

    def get_worth_of_user(self, user_email):
        rolling_sum = 0
        for i in self.books.keys():
            if i.title in self.users[user_email].books.keys():
                # print(i.title, i.get_average_price())
                rolling_sum += i.get_average_price()
        return rolling_sum

    def __repr__(self):
        return("Tome_Rater is a TomeRater type object, that contains lists of users and books read by those users.")

    def __eq__(self, other_TR):
        if self.users == other_TR.users and self.books == other_TR.books:
            print('They are equal')
            return True
        else:
            return False
