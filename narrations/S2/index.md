# Session 2: Object Oriented Programming (in Python!)

Object Oriented Programming (OOP) is a programming paradigm that uses objects to represent data and methods to manipulate that data. It is based on the concept of "objects" which can contain data in the form of fields (attributes) and code in the form of procedures (methods).

In Python, everything (including integers, strings, functions, and modules) is an object, and can be manipulated using OOP principles. There is no such thing as primitives. Variables are also references to objects, not the objects themselves.

## Class, object and methods

A class is a blueprint for creating objects. It defines the attributes and methods that an object will have. An object is an instance of a class. It is a concrete entity that exists in memory. A method is a function that is associated with a class.

Additionally, classes can have what's called "magic methods" or "dunder methods" (short for "double underscore"). These methods are special methods that have double underscores at the beginning and end of their names. They are used to perform special operations on objects and are treated as built-in methods by the Python interpreter.

- @improvise an example here, or use the same as in the doc

There's a lot of magic methods in Python, and they are used to perform special operations on objects. For example, the `__init__` method is used to initialize an object, the `__str__` method is used to return a string representation of an object, and the `__add__` method is used to define the behavior of the `+` operator for objects.

There's also `__repr__`, which behaves similar to `__str__`, but is used for debugging and logging, and `__eq__`, which is used to define the behavior of the `==` operator for objects.

You can find a list of magic methods [in the docs](https://docs.python.org/3/reference/datamodel.html#special-method-names)

## Inheritance and polymorphism

Inheritance is a mechanism in which a new class inherits attributes and methods from an existing class. The existing class is called the base class or superclass, and the new class is called the derived class or subclass. Inheritance allows us to reuse code and create a hierarchy of classes.

Polymorphism is the ability of an object to take on many forms. In Python, polymorphism is achieved through method overriding. Method overriding is a feature that allows a subclass to provide a specific implementation of a method that is already provided by its superclass.

An interesting example of polymorphism is the factory pattern. In this pattern, a factory class is used to create objects of different subclasses, depending on the input parameters. Think of it like having a "vehicle" factory that can create cars, bikes, and trucks, depending on the input.
