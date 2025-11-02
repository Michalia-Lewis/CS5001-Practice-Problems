"""
w3resource Write a Python program that prompts the user to 
input an integer and raises a ValueError exception 
if the input is not a valid integer.

Semester: Fall 2025
Name: Michalia

Link to practice problem: 
https://www.w3resource.com/python-exercises/python-exception-handling-exercises.php
"""

def valid_num(num):
    """
    checks to see if a number is positive and if not raises a value error

    Examples:
        >>> valid_num(-1)
        Invalid value:  <class 'ValueError'> Your number cannot be negative.
        >>> valid_num(12345678)
        Your number is 12345678
        >>> valid_num(0)
        Your number is 0

    Arguments:
        num: an int
    Returns:
        num: an int
    """

    if num < 0:
        raise ValueError('Your number cannot be negative.')
    return num


def main():

    try:
        number = int(input('Enter a positive number: '))
        check_valid = valid_num(number)
        print('Your number is', check_valid)
    except ValueError as ex:
        print('Invalid value: ', type(ex), ex) 

main()
