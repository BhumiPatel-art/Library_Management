from collections import defaultdict

from books import Book, fetch_book_details

MAX_BORROWED_BOOKS = 3
BOOKS_CSV_FILE = "books.csv"

class Library:
    def _init_(self):
        self.books = {}
        self.borrowed_books = {}
        self.borrow_count = defaultdict(int)
        self.load_books_from_csv()

    def load_books_from_csv(self):
        try:
            with open(BOOKS_CSV_FILE, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    book = Book(row['title'], row['author'], row['summary'])
                    self.books[book.title] = book
        except FileNotFoundError:
            print(f"No CSV file found. Starting with an empty library.")

    def save_books_to_csv(self):

    def add_book(self, title):

    def remove_book(self, title):


    def view_available_books(self):


    def borrow_book(self, member, title):


    def return_book(self, member, title):


    def view_borrowed_books(self):


    def view_most_popular_books(self):
