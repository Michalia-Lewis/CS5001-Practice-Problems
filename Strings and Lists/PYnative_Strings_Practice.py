"""
PYnative Exercise 5 Count all letters, digits, 
and special symbols from a given string.

Semester: Fall 2025
Name: Michalia
"""
import doctest
doctest.testmod()

def find_digits_chars_symbols(user_string):
    """
    Finds the total number of letters, numbers, and symbols in a given string.

    Examples:
        >>> find_digits_chars_symbols("H3!!0 W0R1D")
        Letters: 4
        Digits: 4
        Symbols: 2
        >>> find_digits_chars_symbols("y0u l0st th3 g4m3")
        Letters: 9
        Digits: 5
        Symbols: 0
        >>> find_digits_chars_symbols("Wh@tTh3$hu")
        Letters: 7
        Digits: 1
        Symbols: 2

    Arguments:
        user_string (str): The string that will be analyzed.

    Returns: None
    """
    characters = 0
    digits = 0
    symbols = 0

    for char in user_string:
        if char == " ":
            continue
        elif char.isalpha():
            characters += 1
        elif char.isdigit():
            digits += 1
        else:
            symbols +=1

    print("Letters:", + characters)
    print("Digits:", + digits)
    print("Symbols:", + symbols)

def main():

    user_string = input("Please enter a series of numbers and letters: ")

    find_digits_chars_symbols(user_string)

main()
