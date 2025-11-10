"""
Practice Python Exercise 33: Birthday Dictionaries

For this exercise, we will keep track of when our friend’s birthdays are, 
and be able to find that information based on their name. Create a dictionary 
(in your file) of names and birthdays. When you run your program it should 
ask the user to enter a name, and return the birthday of that person back to them.

Semester: Fall 2025
Name: Michalia Lewis

Link to practice problem: https://www.practicepython.org/exercise/2017/01/24/33-birthday-dictionaries.html

Notes: To help me with the edge cases I noticed I did look up solutions on how to 
address those edge cases. As I was looking at solutions I remembered our clean_word function 
from HW 8 and decided to use it as a base and adjusted to fit my my anime birthday dictionary program.
I did still need some assistance when it came to how to call my clean_name function on the user's input
and on the birthday_directory dictionary as well as how to format my print statements.
"""

birthday_directory = {'Monkey D. Luffy' : 'May 5th',
                        'Naruto Uzumaki' : 'October 10th',
                        'Tanjiro Kamado' : 'July 14th',
                        'Ichigo Kurosaki' : 'July 15th',
                        'Ken Ryuguji' : 'May 10th',
                        'Gojo Satoru' : 'December 7th',
                        'Izuku Midoriya' : 'July 15th',
                        'Eren Yeager' : 'March 30th',
                        'Anya Forger' : 'March 3rd',
                        'Goku Son' : 'April 16th'
                        }


def clean_name(name: str) -> str:
    """
    Function: Recursively removes punctuation but keeps spaces and capitalization.

    Arguments:
        name (str): the name to remove punctuation from and keep spaces between first and last name
    Returns:
        str: the name without punctuation and a space between first and last name
    """
    if not name:  # base case: empty string
        return name
    if name[0].isalnum() or name[0].isspace():   # If the first char is a letter/number/space, keep it
        return name[0] + clean_name(name[1:])  # recurses through the rest of the string
    else:
        return clean_name(name[1:])  # skips anything that is not a letter/number/space
    

def birthday_lookup(name):
    """
    Provides birthdays for specific anime characters based on the user's input.

    Examples:
        >>> birthday_lookup('Naruto Uzumaki')
        Naruto Uzumaki's birthday is October 10th.
        Thanks for using the anime birthday dictionary!
        >>> birthday_lookup('Ada Lovelace')
        Sadly we don't have Ada Lovelace's birthday yet.
        >>> birthday_lookup('Johnny Dep')
        Sadly we don't have Ada Lovelace's birthday yet.
        >>> birthday_lookup('1')
        ValueError: Your entry can only contain letters (Note:spaces between first & last names are okay!)
        >>> birthday_lookup('GojoSatoru')
        Gojo Satoru's birthday is December 7th.
        >>> birthday_lookup('ErEnYeAgEr')
        Eren Yeager's birthday is March 30th.

    Arguments: name -- name of the person the user enters in to look up
    Returns: None
    """
    # Clean up all dictionary keys and create a “normalized” version that ignores spacing & case.
    normalized_dict = {clean_name(k).replace(" ", "").lower(): k for k in birthday_directory}
    # cleans user's input
    normalized_name = clean_name(name).replace(" ", "").lower()

    if normalized_name in normalized_dict:
        original_name = normalized_dict[normalized_name]  # if user's input matches a name in birthday_directory store it in original_name
        formatted_name = original_name.title() # returns the name to proper title case
        print(f"{formatted_name}'s birthday is {birthday_directory[original_name]}.")
        print("Thanks for using the anime birthday dictionary!")
    elif name.isalpha() or " " in name:
        print(f"Sadly, we don't have {name}'s birthday yet.")
    else:
        raise ValueError('Your entry can only contain letters (Note:spaces between first & last names are okay!)')
    

def main():
    print('Welcome to the anime birthday dictionary. We know the birthdays of:')
    for name in birthday_directory:
        print(name)
    
    print('Who\'s birthday do you want to look up?')
    name = input()
    name.replace(" ", "")

    birthday_lookup(name)

main()
