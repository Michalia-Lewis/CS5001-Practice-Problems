"""
HackerRank If Else Practice:

Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird

Link to practice problem:
https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true

Semester: Fall 2025
Name: Michalia Lewis
"""


def main ():

    n = int(input('Choose a number between 1 and 100. '))

    if n % 2 != 0:
        print('Weird')
    if n % 2 == 0 and (n >= 2 <= 5):
        print('Not Weird')
    if n % 2 == 0 and (n >= 6 <= 20):
        print('Weird')
    if n % 2 == 0 and n > 20:
        print('not weird')

main ()
