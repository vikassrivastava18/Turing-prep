# Problem: "Validate" the inputs to be numbers, also check denominator is not zero
def calc(a: int, b: int) -> None:
    assert isinstance(a, int) and isinstance(b, int), "Only integers allowed"
    try:
        print("a+b = ", a+b)
        print("a/b = ", a/b)
    except ZeroDivisionError:
        print("Can't divide by zero")
        print("a/b = infinity")
    finally:
        print("Program execution complete.")


# Problem: Return the remainder for two given numbers
def remainder(a: int, b: int) -> (int | AssertionError):
    """
    Parameters: two integers (a, b)
    Returns: Returns integer remainder for correct input, Assertion Error
    Plan: Use assertion concept for input validation
    """
    assert  b!=0, 'Denominator should not be 0'
    assert type(a) == int and type(b) == int, "Invalid inputs"

    r = a % b
    return r
