"""
PYnative Practice Problem: Exercise 4 Create a function with a default argument

Write a program to create a function show_employee() with the following specifications:

It should accept the employee’s name and salary.
It should display both the name and salary.
If the salary is not provided in the function call, it should default to 9000.

Semester: Fall 2025
Name: Michalia Lewis

Link to practice problem: 
https://pynative.com/python-functions-exercise-with-solutions/#h-exercise-4-create-a-function-with-a-default-argument
"""
def show_employee(name, salary):
    """
    Displays an employee's name and current salary if provided. If the employee only provides their name
    then it will display a default salary of 9000.


    Examples:
        >>> show_employee("Ben", 12000)
        Name: Ben salary: 12000
        >>> show_employee("Jessa")
        Name: Jessa salary: 9000
        >>> show_employee("Eren")
        Name: Eren salary: 9000
        >>> show_employee("Armin", 150000)
        Name: Armin salary: 150000
        >>> show_employee("Nagato", 80000000000)
        Name: Nagato salary: 80000000000
        >>> show_employee("Luffy")
        Name: Luffy salary: 9000
        
    Arguments:
        name: employee's name provided by the employee
        salary: employee's salary provided by the employee. If not provided salary defaults to 9000.

    Returns:
        none
    """
    print("Name:", name, "salary:", salary)

def main():

    user_input = input("Please enter your name and salary: ")
    name_and_salary = user_input.split()
    name = name_and_salary[0]

    if len(name_and_salary) > 1:
        salary = name_and_salary[1]
    elif len(name_and_salary) == 1:
        salary = 9000

    show_employee(name, salary)

main()