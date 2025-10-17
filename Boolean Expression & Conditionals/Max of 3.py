"""
Practice Python Exercise 28: Max of 3

Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!
The goal of this exercise is to think about some internals that Python normally takes care of for us. All you need is some variables and if statements!

Link to practice problem:
https://www.practicepython.org/exercise/2016/03/27/28-max-of-three.html

Semster: Fall 2025
Name: Michalia Lewis
"""

def main ():

    first = int(input('Enter first number: '))
    second = int(input('Enter second number: '))
    third = int(input('Enter third number: '))

    if first >= second and first >= third:
        max = first
    elif second >= first and second >= third:
        max = second
    else:
        max = third

    print('Max number is', max,'.')

main ()
