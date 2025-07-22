# main.py

from robust_division_calculator import safe_divide

def main():
    print("Welcome to the Robust Division Calculator!")
    numerator = input("Enter the numerator: ")
    denominator = input("Enter the denominator: ")

    try:
        result = safe_divide(numerator, denominator)
        print(f"The result of dividing {numerator} by {denominator} is {result}")
    except ZeroDivisionError as zde:
        print(f"Error: {zde}")
    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
from library_management import Book, Library

def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()

if __name__ == "__main__":
    main()
