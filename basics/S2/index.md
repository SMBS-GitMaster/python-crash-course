# Session 2: Object Oriented Programming (in Python!)

In this session, we'll learn about Object Oriented Programming (OOP) in Python. We'll cover the following topics:

- Basic concepts
- Class, object and methods
- Inheritance and polymorphism

## Basic concepts

Object Oriented Programming (OOP) is a programming paradigm that uses objects to represent data and methods to manipulate that data. It is based on the concept of "objects" which can contain data in the form of fields (attributes) and code in the form of procedures (methods).

In Python, everything (including integers, strings, functions, and modules) is an object, and can be manipulated using OOP principles. There is no such thing as primitives. Variables are also references to objects, not the objects themselves.

## Class, object and methods

A class is a blueprint for creating objects. It defines the attributes and methods that an object will have. An object is an instance of a class. It is a concrete entity that exists in memory. A method is a function that is associated with a class.

Additionally, classes can have what's called "magic methods" or "dunder methods" (short for "double underscore"). These methods are special methods that have double underscores at the beginning and end of their names. They are used to perform special operations on objects and are treated as built-in methods by the Python interpreter.

Here's an example of a simple class in Python:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
```

In this example, we define a class `Person` with two attributes `name` and `age`, and a method `greet` that prints a greeting message. We can create an instance of this class and call the `greet` method like this:

```python
person = Person("Alice", 30)
person.greet()
```

## Inheritance and polymorphism

Inheritance is a mechanism in which a new class inherits attributes and methods from an existing class. The existing class is called the base class or superclass, and the new class is called the derived class or subclass. Inheritance allows us to reuse code and create a hierarchy of classes.

Polymorphism is the ability of an object to take on many forms. In Python, polymorphism is achieved through method overriding. Method overriding is a feature that allows a subclass to provide a specific implementation of a method that is already provided by its superclass.

An interesting example of polymorphism is the factory pattern. In this pattern, a factory class is used to create objects of different subclasses, depending on the input parameters. Think of it like having a "vehicle" factory that can create cars, bikes, and trucks, depending on the input.

```python
class VehicleFactory:
    # Factory method
    @staticmethod
    def create_vehicle(vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "bike":
            return Bike()
        elif vehicle_type == "truck":
            return Truck()

    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        print("Driving a car")

class Bike(Vehicle):
    def drive(self):
        print("Riding a bike")

class Truck(Vehicle):
    def drive(self):
        print("Driving a truck")
```

In this example, we have a `VehicleFactory` class with a factory method `create_vehicle` that creates objects of different subclasses based on the input parameter `vehicle_type`. Each subclass (`Car`, `Bike`, `Truck`) has a `drive` method that prints a message specific to that type of vehicle. We can use the factory method to create different types of vehicles and call the `drive` method on them.

That's it for this session! We've covered the basics of Object Oriented Programming in Python. If you have any questions or suggestions for improvements, please open an issue on GitHub. You can also contribute to this course by submitting a pull request.


## Assignments

Note: all assignments must be done in idiomatic Python. Doing it in too many lines or using too many variables is not idiomatic.

1. Write classes for the following shapes: `Circle`, `Rectangle`, and `Triangle`.
- Each class should have a method `area` that calculates the area of the shape.
- The `Circle` class should have a method `circumference` that calculates the circumference of the circle.
- The `Rectangle` class should have a method `perimeter` that calculates the perimeter of the rectangle.
- The `Triangle` class should have a method `is_right` that returns `True` if the triangle is a right triangle, and `False` otherwise.
- You can assume that the shapes are 2D and are defined by their dimensions (e.g., radius for a circle, base and height for a triangle, etc.).

