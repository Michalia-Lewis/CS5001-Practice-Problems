"""
w3resource: Python: Recursion - Exercises, Practice, Solution

Write a Python program to calculate the sum of a list of numbers using recursion.

Semester: Fall 2025
Name: Michalia Lewis

Link to practice problem: 
https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php
"""

def sum_of_list(list):
    """
    Takes a list of numbers and adds them together.

    Examples:
        >>> sum_of_list([4, 11, 2025])
        2040
        >>> sum_of_list([3, 6, 9])
        18
        >>> sum_of_list([-1, 0.5, 28])
        27.5

    Arguments:
        list: list of numbers

    Returns:
        int: sum of the numbers in the list
    """

    if len(list) == 1:
        return list[0]
    else:
        return list[0] + sum_of_list(list[1:])


def main():

    user_input = input("Enter numbers separated by spaces (e.g. 1 2 3 4): ")
    user_numbers = [int(num) for num in user_input.split()]
    result = sum_of_list(user_numbers)

    print("The sum is:", result)

main()
