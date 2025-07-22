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
