# robust_division_calculator.py

def safe_divide(a, b):
    """
    Performs a safe division of two numbers.

    Parameters:
        a (float): The numerator.
        b (float): The denominator.

    Returns:
        float: The result of the division.

    Raises:
        ZeroDivisionError: If b is zero.
        ValueError: If inputs are not convertible to float.
    """
    try:
        a = float(a)
        b = float(b)
        result = a / b
        return result
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide by zero.")
    except ValueError:
        raise ValueError("Both inputs must be numbers.")
