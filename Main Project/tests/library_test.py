import pytest
from books import Book
from library import Library
from io import StringIO
import sys

def test_remove_book():
    # Setup
    library = Library()
    library.books = {
        "Book A": Book("Book A", "Author A", "Summary A"),
        "Book B": Book("Book B", "Author B", "Summary B"),
    }

    # Capture output for removing an existing book
    captured_output = StringIO()
    sys.stdout = captured_output
    try:
        library.remove_book("Book A")
    finally:
        sys.stdout = sys.__stdout__

    assert "removed 'book a'" in captured_output.getvalue().lower()
    assert "Book A" not in library.books

    # Capture output for removing a non-existent book
    captured_output = StringIO()
    sys.stdout = captured_output
    try:
        library.remove_book("Book X")
    finally:
        sys.stdout = sys.__stdout__

    assert "'book x' not found" in captured_output.getvalue().lower()
