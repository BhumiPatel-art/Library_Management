import pytest
from books import Book
from library import Library
from io import StringIO
import sys

def test_borrow_limit():
    library = Library()
    library.books = {
        "Book A": Book("Book A", "Author A", "Summary A"),
        "Book B": Book("Book B", "Author B", "Summary B"),
        "Book C": Book("Book C", "Author C", "Summary C"),
        "Book D": Book("Book D", "Author D", "Summary D")
    }

    member = "test_user"
    library.borrow_book(member, "Book A")
    library.borrow_book(member, "Book B")
    library.borrow_book(member, "Book C")

    captured_output = StringIO()
    sys.stdout = captured_output
    try:
        library.borrow_book(member, "Book D")
    finally:
        sys.stdout = sys.__stdout__
    assert "cannot borrow more than" in captured_output.getvalue().lower()
