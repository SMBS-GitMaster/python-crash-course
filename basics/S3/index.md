# Session 3: Exception handling

In this session, we'll learn about exception handling in Python. That is, how to handle errors and exceptions that occur during the execution of a program. We'll cover the following topics:

- **Exception handling**
  - Customized exceptions
  - Exception management blocks (try-catch-finally)

## Exception handling

Here's an example of exception handling in Python:

```python
try:
    # This code will raise a ZeroDivisionError
    result = 1 / 0
except ZeroDivisionError as e:
    print(f"An error occurred: {e}")
finally:
    print("This block will always be executed, regardless of whether an exception occurred or not.")
```

Exception handling is a mechanism in Python that allows us to handle errors and exceptions that occur during the execution of a program. When an error occurs, Python raises an exception, which can be caught and handled by the programmer. This prevents the program from crashing and allows us to gracefully recover from errors.

It is imperative that you handle exceptions in your code, as unhandled exceptions can lead to unexpected behavior and security vulnerabilities. Python provides several built-in exception classes that you can use to handle different types of errors, sometimes we can also create our own exception classes if the built-in ones are not enough.

When you use `except <exception>`, you're catching all exceptions that are either the one provided, or inherit from it (as subclasses).

It's important to note that only the explicit exception and exceptions that derive from it will be caught by `except`. This means that, if an exception inherits from `BaseException`, it won't be caught by `except Exception`, according to the exception hierarchy. You can check the full exception hierarchy in [the documentation](https://docs.python.org/3/library/exceptions.html#exception-hierarchy).

There's patterns for exception handling, which are paradigms that determine when we should throw and when we should catch exceptions. 

The most common pattern is the EAFP (Easier to Ask for Forgiveness than Permission) pattern, which is based on the idea that it's easier to ask for forgiveness (handle exceptions) than to ask for permission (check for conditions). This pattern is widely used in Python and is considered more Pythonic than the LBYL (Look Before You Leap) pattern.

Usually, with the EAFP pattern, we assume that the code will run without errors and handle exceptions when they occur. This makes the code more concise and readable, as we don't have to check for conditions at every step. Additionally, we handle the exceptions in a more centralized way, which makes the code easier to maintain.

With the LBYL pattern, however, we check for conditions before executing the code, which can lead to more verbose and less readable code. This pattern is more common in other programming languages like Java and C++, where exceptions are considered expensive and should be avoided if possible.

```python
import os, errno, stat

def read_file_eafp(fn):
    """
    Read a file and return its contents.  If the file doesn't exist or
    can't be read, return "".
    """
    try:
        return open(fn).read()
    except IOError, e:
        return ""

def read_file_lbyl(fn):
    """
    Read a file and return its contents.  If the file doesn't exist or
    can't be read, return "".
    """
    if not os.access(fn, os.R_OK):
        return ""
    st = os.stat(fn)
    if stat.S_ISDIR(st.st_mode):
        return ""
    return open(fn).read()

print read_file("x")
```

In the above example, we use the EAFP and LBYL patterns to read a file and return its contents. 

In the first function we use EAFP, We assume that the file will exist and can be read, and handle the exception if it doesn't. This makes the code more concise and readable, as we don't have to check for conditions at every step.

In the second one, we use LBYL. We check if the file exists and can be read before trying to open it, but by doing this, we're doing a lot more IO work, which overomplicate the code and may even lead to bad performance (even worse than if we just caught the exception!).

In Python, exceptions are considered a normal part of the program flow and are used to handle errors and edge cases, and sometimes to control the program flow (such as the "StopIteration" exception in iterators). They are not as expensive as in other languages (such as C++, where an exception causes stack unwinding) and are used more frequently in Python codebases.

In general, you should throw when you know that continuing the execution of the program is not possible, or if it would lead to unexpected behavior. You should catch when you can recover from the error and continue the execution of the program.

In this example, we use a `try` block to wrap the code that might raise an exception. If an exception occurs, the code inside the `except` block will be executed, and the program will continue to run. The `finally` block will always be executed, regardless of whether an exception occurred or not.

### Caveats

There are some caveats to exception handling that you should be aware of, such as:
- Exceptions are not free: even though they're much more efficient than in other languages, they take time to be raised and caught, so you should avoid using them for trivial things such as control flow. 
- When within a `context manager` (like a `with` block), the manager decides whether to handle the exception or propagate it. The `open` function is a context manager, so it will handle the exception and close the file if an error occurs. There's also some context managers that will propagate the exception, like the `unittest` module. We'll delve into context managers in a future session.

## Customized exceptions

Sometimes the built-in exception classes are not enough to handle all the errors in your program. In these cases, you can create your own exception classes by subclassing the `Exception` class. This allows you to define custom error messages and behaviors for your exceptions. Custom exceptions are useful when you want to provide more context about the error or when you want to handle specific errors in a special way.

Here's an example of a custom exception class in Python:

```python
class MyCustomError(Exception):
    def __init__(self, message):
        super().__init__(message)

try:
    raise MyCustomError("This is a custom error message.")
except MyCustomError as e:
    print(f"An error occurred: {e}")
```

This example defines a custom exception class `MyCustomError` that inherits from the `Exception` class. We then raise an instance of this exception class with a custom error message, and catch it with an `except` block. The error message is printed to the console, along with the custom error message we provided.

We're using the `super()` function to call the constructor of the parent class `Exception` and pass the custom error message to it. This ensures that the exception is properly initialized and can be caught and handled by the `except` block, as expected.

