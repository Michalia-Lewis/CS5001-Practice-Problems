"""
Hacker Rank's String Validator Practice Problem:

You are given a string .
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Semester: Fall 2025
Name: Michalia

Link to practice problem: 
https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true
"""

def string_validator(str):
    """
    This function checks to see if a string contains any digits, alphanumeriec or alphabetical characters, and uppercase or lowercase characters.

    Examples:
    >>> string_validator(qA2)
    True, True, True, True, True
    >>> string_validator(4/11/25)
    True, False, True, True, False, True, True
    >>> string_validator($$$$$)
    False, False, False, False, False
    >>> string_validator(-1234)
    False, True, True, True, True

    Arguments:
        str: The string to be analyzed.
    Returns:
        none

    In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
    In the second line, print True if  has any alphabetical characters. Otherwise, print False.
    In the third line, print True if  has any digits. Otherwise, print False.
    In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
    In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
    """
    for char in str:
        if char.isalnum():
            print(True)
            if char.isalpha():
                print(True)
                if char.isdigit():
                    print(True)
                    if char.islower():
                        print(True)
                        if char.isupper():
                            print(True)
        else:
            print(False)

string_validator("qA2")
print("\n")

string_validator("4/11/25")
print("\n")

string_validator("$$$$")
print("\n")

string_validator("-1234")