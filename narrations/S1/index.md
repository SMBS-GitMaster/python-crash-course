# Introduction

The first version of Python was released 30 years ago in 1990. Since then, the language has undergone a huge amount of change, and has grown into one of the most popular programming languages in the world.

One of the main strengths of Python is the readability of its code, which makes it extremely accessible. Often Python code reads just like English. Python is also extremely flexible, and can be found in a wide range of industries, from machine learning to web development.

At the time of writing there are two major Python standards in active use.

First we have Python 2.7 which is the most current version of Python 2. Python 2 has technically reached its end of life, and will no longer get any additional updates, but there’s still a huge amount of Python 2 code out there!

The second branch of Python is Python 3, with the most current version being Python 3.12. Python 3 was intended to be a replacement for Python 2, and boasts a number of improvements along with some significant syntax changes. Code written in Python 2 may not be compatible with Python 3, and even if the code runs we may end up with unexpected behaviour.

## Numbers

In Python, we have several different ways of representing numbers, the most common of which are integers and floating point numbers—also known as floats.

Integers and floats are basic numerical types in Python. Integers are used to represent whole numbers, and floats are used for real numbers with some decimal component. For example, we'd use an integer for the number 3, but a float for 3.141.

- @improvise example Here

Python also has a complex number type, which is used to represent complex numbers. Complex numbers have a real part and an imaginary part, and are written in the form `a + bj`, where `a` is the real part, `b` is the imaginary part, and `j` is the square root of -1. These are useful for certain mathematical calculations, such as signal processing and electrical engineering. We'll not dive into complex numbers in this course, but if you ever need them, call god.

## Variables

Variables are used to store data in a program. In Python, variables are created when they are assigned a value. The type of the variable is determined by the value assigned to it. For example, if we assign the value `42` to a variable, Python will create an integer variable. If we assign the value `3.14`, Python will create a float variable. Variables can also be assigned strings, booleans, lists, dictionaries, and other data types.

Something important to keep in mind is that variabls are references to objects, not the objects themselves. This means that when we assign a variable to an object, we're actually assigning a reference to the object, not the object itself. This can lead to some unexpected behavior if you're not careful!

- @improvise example here, we can use dicts or lists

## Operators

Operators are used to perform operations on variables and values. Python has several types of operators, including arithmetic operators, comparison operators, logical operators, assignment operators, identity operators, membership operators, and bitwise operators. These operators allow us to perform mathematical operations, compare values, and control the flow of our programs.

- @improvise example here, we can use arithmetic operators

## Strings

Strings are used to represent text in Python. They are created by enclosing text in single or double quotes. Strings are immutable, which means that once they are created, they cannot be changed. However, we can create new strings by combining or manipulating existing strings.

Strings can be concatenated using the `+` operator, which joins two strings together. We can also use string formatting to insert variables or expressions into a string. There are several ways to format strings in Python, including the `format()` method and f-strings. f-strings are a newer feature in Python 3.6 that allow us to embed expressions inside strings by prefixing the string with an `f`, similar to what we'd do in languages such as JavaScript with template strings, or in C# with interpolated strings.

- @improvise example here, we can use f-strings and format

## Booleans

I think this is pretty obvious

## Lists

Lists are used to store multiple items in a single variable. They are created by placing items inside square brackets, separated by commas. Lists can contain items of different data types, including integers, floats, strings, booleans, and even other lists. Lists are mutable, which means that we can change, add, or remove items from a list after it has been created.

Something really important to keep in mind is that the objects within a list are referenced whenever we iterate on top of them. This means that if we change the object, the list will also change, as I showed in the example earlier.

## Tuples

Tuples are similar to lists, but they are immutable, which means that once they are created, they cannot be changed. Tuples are created by placing items inside parentheses, separated by commas. Tuples are often used to store related pieces of information together, such as the coordinates of a point or the RGB values of a color.

## Dictionaries

Dictionaries are used to store key-value pairs in Python. They are created by placing items inside curly braces, separated by commas, with a colon between the key and the value. Dictionaries are mutable, which means that we can change, add, or remove items from a dictionary after it has been created. Similar to lists, dictionaries are also referenced when we iterate over their values.

## Sets

These are similar to lists, but they are unordered and contain unique items. Sets are created by placing items inside curly braces, separated by commas. Sets can contain items of different data types, including integers, floats, strings, and booleans. Sets are mutable, which means that we can change, add, or remove items from a set after it has been created. Sets are often used to perform mathematical operations such as union, intersection, difference, and symmetric difference.

## Control Flow

Control flow is used to determine the order in which statements are executed in a program. The basic control flow statements in Python are:
