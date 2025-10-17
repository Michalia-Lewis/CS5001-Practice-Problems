"""
Practice Python Exercise 2: Odd Or Even

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

Challenge:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

Link to practice problem:
https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

Semester: Fall 2025
Name: Michalia Lewis
"""


def main ():

    num = int(input('Pick a number. Any number.'))
    check = int(input('Give me a number to divide by.'))

    if num % 4 == 0:
        print(num, 'is a multiple of 4.')
    elif num % 2 == 0:
        print(num, 'is an even number.')
    else:
        print(num, 'is an odd number.')

    if num % check == 0:
        print(num, 'divides evenly by', check,'.')
    else:
        print(num, 'does not divide evenly by', check,'.')


main ()
