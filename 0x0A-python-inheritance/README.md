Technical Write-up for Project 0x0A: Python - Inheritance
Project Overview
The project "0x0A: Python - Inheritance" is part of the curriculum for learning Python programming with a focus on Object-Oriented Programming (OOP) and Inheritance. The project aims to enhance the understanding of inheritance, classes, objects, and various aspects of OOP in Python. It consists of several tasks that require the creation of Python classes and functions.

The project's tasks can be summarized as follows:

Lookup (File: 0-lookup.py)

Write a function that returns the list of available attributes and methods of an object.
Demonstrate how to access the attributes and methods of various classes and objects.
My List (File: 1-my_list.py)

Create a class MyList that inherits from the built-in list class.
Add a method print_sorted that prints the list sorted in ascending order.
Same Class or Inherit From (File: 2-is_same_class.py)

Write a function that determines if an object is an instance of a specified class.
Demonstrate how to check the class of various objects and print appropriate messages.
Kind of Class (File: 3-is_kind_of_class.py)

Write a function that checks if an object is an instance of, or inherited from, a specified class.
Illustrate how to determine if objects are instances of different classes.
Only Subclass of (File: 4-inherits_from.py)

Develop a function that checks if an object is an instance of a class that directly or indirectly inherited from a specified class.
Demonstrate how to check object inheritance.
Geometry Module (File: 5-base_geometry.py)

Create an empty class BaseGeometry to serve as the base class for future classes.
Show how to create an instance of the class and list its attributes and methods.
Improve Geometry (File: 6-base_geometry.py)

Enhance the BaseGeometry class by adding an abstract method area that raises an exception.
Demonstrate how to raise and handle exceptions in Python.
Integer Validator (File: 7-base_geometry.py)

Extend the BaseGeometry class to include a method integer_validator that validates integer values.
Validate and raise exceptions for various input scenarios.
Rectangle (File: 8-rectangle.py)

Create a class Rectangle that inherits from BaseGeometry.
Implement instantiation with width and height attributes and validation.
Override the area method to calculate the area of a rectangle.
Square #1 (File: 10-square.py)

Develop a class Square that inherits from the Rectangle class.
Initialize the class with a single size attribute.
Implement the area method for calculating the area of a square.
Square #2 (File: 11-square.py)

Enhance the Square class by providing a custom string representation for squares.
Show how to customize the str() output.
My Integer (File: 100-my_int.py)

Create a class MyInt that inherits from int with inverted == and != operators.
Demonstrate custom operator overloading.
Can I? (File: 101-add_attribute.py)

Implement a function add_attribute that adds a new attribute to an object if possible.
Demonstrate dynamic attribute assignment and raise exceptions when necessary.
Learning Objectives
The project aims to achieve the following learning objectives:

General
Understanding the awesomeness of Python programming.
Differentiating between superclass, base class, parent class, and subclass.
Listing attributes and methods of a class or instance.
Identifying when an instance can have new attributes.
Inheriting a class from another and using multiple base classes.
Exploring the default class every class inherits from.
Overriding a method or attribute inherited from the base class.
Understanding which attributes or methods are available to subclasses through inheritance.
Realizing the purpose of inheritance in Python.
Utilizing isinstance, issubclass, type, and super built-in functions
