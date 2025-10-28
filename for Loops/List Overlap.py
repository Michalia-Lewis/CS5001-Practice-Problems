"""
Practice Python Exercise 5: List Overlap

Take two lists and write a program that returns a list that contains only 
the elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.

Challenges:
Randomly generate two lists to test this
Write this in one line of Python

Note: I wasn't able to figure out how to write this in one line of Python with my current knowledge.
As I learn, I will return to this practice problem to see if I am able to complete this challenge. 

Semester: FAll 2025
Name: Michalia Lewis

Link to practice problem: 
https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
"""

import random

def list_overlap(a = [], b = []) -> list:
    """
    Takes two lists and returns a single list with the common elements between each list
    without duplicates.


    Examples:
        >>> list_overlap(a = [pizza, sushi, cheeseburgers], b = [pizza, ramen, udon, sushi, sashimi])
        [pizza, sushi]
        >>> list_overlap(a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
        [1, 2, 3, 5, 8, 13]
        >>> list_overlap(a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29 ], b = ['get', 'pranked'])
        []

    Arguments:
        list: first list to be analyzed
        list: second list to be analyzed

    Returns:
        list: common elements from each list 
    """

    list_final = []

    for n in a:
        if n in b and n not in list_final:
            list_final.append(n)  
    return list_final

def list_overlap_random(a = [], b = []) -> None:
    """
    Takes two randomly generated lists of ints and returns a single list with the common ints between each list
    without duplicates.

    Arguments:
        list: first list to be analyzed
        list: second list to be analyzed

    Returns:
        none
    """
    a = [random.randint(0, 100) for _ in range(20)]
    print(a)
    b = [random.randint(0, 100) for _ in range(20)]
    print(b)

    list_final = []

    for n in a:
        if n in b:
            list_final.append(n)
    if len(list_final) != 0:
        print('Random list:', list_final, '\n')
    else:
        print('No common numbers found.')

def main():

    list_result_one = list_overlap(a = ['pizza', 'sushi', 'cheeseburgers'], b = ['pizza', 'ramen', 'udon', 'sushi', 'sashimi'])
    print('List 1: ', list_result_one, '\n')

    list_result_two = list_overlap(a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
    print('List 2: ', list_result_two, '\n')

    list_result_three = list_overlap(a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29 ], b = ['get', 'pranked'])
    print('List 3: ', list_result_three, '\n')

    list_overlap_random(a = [], b = [])

main()
