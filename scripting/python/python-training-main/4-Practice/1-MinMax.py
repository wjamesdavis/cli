"""
Task - Implement the functions Below.
        You do not need to (and should not) edit main in order to accomplish this
"""


def findLowest(numbers):
    """
    Param: numbers - A list containing only numbers
    Returns: int - the lowest integer in the list
    """
    # Write code here
    # You are not allowed to use the 'min' keyword...
    # use the "return" keyword to return the lowest number


def findHighest(numbers):
    """
    Param: numbers - A list containing only numbers
    Returns: int - the highest integer in the list
    """
    # Write code here
    # You are not allowed to use the 'max' keyword...
    # use the "return" keyword to return the lowest number


def main():
    numbers = [15, 23, 91, 7, 28, 513, 12]

    lowest = findLowest(numbers)
    highest = findHighest(numbers)

    print(f"The lowest number in {numbers} is {lowest}")
    print(f"The highest number in {numbers} is {highest}")

    print(f"The true result is {min(numbers)} and {max(numbers)}")
