"""
w3resource: Modify the attribute values of a given class

Create a Class Named Student with Attributes; Modify and Print Original and Modified Values

Write a Python class named Student with two attributes student_name, marks. 
Modify the attribute values of the said class and print the original and modified values of the said attributes.

Semester: Fall 2025
Name: Michalia Lewis

Link to practice problem:
https://www.w3resource.com/python-exercises/class-exercises/python-class-basic-1-exercise-9.php
"""

class Student:
    student_name = 'Naruto Uzumaki'
    math = 52

print(f"Student Name: {getattr(Student, 'student_name')}")
print(f"Math Grade: {getattr(Student, 'math')}")
setattr(Student, 'student_name', 'Gojo Satoru')
setattr(Student, 'math', 0)
print(f"Student Name: {getattr(Student, 'student_name')}")
print(f"Math Grade: {getattr(Student, 'math')}")
