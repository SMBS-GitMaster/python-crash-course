# Functional programming with Python

Functional programming is a programming paradigm that treats computation as the evaluation of mathematical functions and avoids changing-state and mutable data. It is a declarative type of programming style, where we define what we want to do, rather than how we want to do it.

It's based on the concept that functions are first-class citizens, which means that functions can be passed as arguments to other functions, returned from other functions, and assigned to variables. This makes functions very flexible and powerful. In Python, functions are first-class objects, which means they can be treated like any other object.

Functional programming is based on a few core concepts:

- Pure functions
- Immutability
- Higher-order functions
- Recursion
- Lazy evaluation
- Referential transparency
- Monads

In this course, we'll cover some of these concepts and how they can be applied in Python.

## Pure functions

A pure function is a function that has the following properties:

- Its return value is the same for the same arguments (deterministic)
- Its evaluation has no side effects
- Its evaluation does not depend on the state of the program

In all programming languages, pure functions are the building blocks of functional programming. They are easy to reason about, test, and debug. They also make it easier to understand and maintain code. Whenever you create a util (or helper) function, you should strive to make it a pure function, as it will make your code more predictable and easier to work with.

I won't provide an example because we've already seen a lot of functions in the previous sections, if you have any doubts just ask me :)

## Immutability

Immutability is a property of data that means it cannot be changed after it has been created, assigned or captured within a context. In Python, some data types are immutable, such as integers, strings, and tuples. This means that once you create an integer, string, or tuple, you cannot change its value, only create a new one.

Objects can be passed to another context in two ways:

1. By value: the object is copied and passed to the new context. This is the case for immutable objects, and even the original variable is not changed, the new one is.
2. By reference: the object is not copied, only a reference to it is passed to the new context. This is the case for mutable objects, and if you change the object in the new context, the original object will also change.

```python
def change_list(lst):
    """
    This function changes the list passed as an argument, as it is mutable (passed by reference)
    """
    lst.append(4)

my_list = [1, 2, 3]
change_list(my_list)

print(my_list)  # Output: [1, 2, 3, 4]
```

It is imperative that you KEEP TRACK OF MODIFICATIONS TO MUTABLE OBJECTS, as these are usually the main source of bugs in Python programs (that and the infamous `None`).

And, here's an example of immutability:

```python
def change_string(s):
    """
    This function changes the string passed as an argument, but as strings are immutable, it creates a new one
    """
    s += " World!"

my_string = "Hello"
change_string(my_string)

print(my_string)  # Output: Hello
```

## Higher-order functions

Higher-order functions are functions that take other functions as arguments or return functions as results. They are a powerful concept in functional programming, as they allow us to abstract over actions, not just data. In Python, functions are first-class objects, which means they can be passed as arguments to other functions, returned from other functions, and assigned to variables.

There's built-in functions in Python that are higher-order functions, such as `map`, `filter`, and `reduce`. These functions take a function and an iterable as arguments and apply the function to each element of the iterable. We'll see some examples of these functions later, just wait.

## Recursion

Recursion is a technique in which a function calls itself in order to solve a problem. It is a powerful concept in functional programming, as it allows us to solve complex problems by breaking them down into smaller, more manageable subproblems. Recursion is often used to solve problems that can be broken down into smaller, similar subproblems, such as tree traversal, sorting, and searching.

Here's an example of a recursive function that calculates the factorial of a number:

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)

print(result)  # Output: 120
```

## Lazy evaluation

Lazy evaluation is an evaluation strategy that delays the evaluation of an expression until its value is actually needed. This can help improve performance by avoiding unnecessary computations. In Python, lazy evaluation is often used with generators and iterators, which generate values on the fly, rather than all at once.

We saw generators in S1, and they are a great example of lazy evaluation. They allow us to generate values on the fly, rather than all at once. This can be useful when working with large datasets, as it allows us to process data one element at a time, rather than loading the entire dataset into memory.

## Referential transparency

Referential transparency is a property of functions that means they can be replaced with their return values without changing the program's behavior. This property makes it easier to reason about and optimize code, as you can substitute function calls with their return values without changing the program's behavior.

Not all functions are referentially transparent, as some functions may have side effects or depend on the state of the program. However, pure functions are always referentially transparent, as they have no side effects and their return values are determined solely by their input arguments.

The reason for which pure functions are referentially transparent, is that their return value is the only effect they have on the program. This means that if you call a pure function with the same arguments, you'll always get the same result, and you can replace the function call with its return value without changing the program's behavior. They can also be easily cached thanks to this property.

## Monads

Monads are a design pattern in functional programming that allows us to chain operations together in a sequence. They are a way to encapsulate computations and control the flow of a program. Monads are often used to handle side effects, such as I/O operations, in a pure functional way.

```python
# Alchemy example of the monad design pattern:
db.session.query(User).filter(User.name == 'Alice').all()
```

SQLAlchemy ORM is a great example of the monad design pattern. In this example, we're using the `query` method to create a query object, the `filter` method to filter the results, and the `all` method to retrieve all the results. Each method returns a new object that encapsulates the computation, and we can chain these operations together to create complex queries.

Here's an implementation of a monad. You'll need this for the assignment later on:
```python
class Maybe:
    def __init__(self, value):
        self._value = value

    def bind(self, func):
        if self._value is None:
            return Maybe(None)
        else:
            return Maybe(func(self._value))

    def orElse(self, default):
        if self._value is None:
            return Maybe(default)
        else:
            return self

    def unwrap(self):
        return self._value

    def __or__(self, other):
        return Maybe(self._value or other._value)

    def __str__(self):
        if self._value is None:
            return 'Nothing'
        else:
            return 'Just {}'.format(self._value)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if isinstance(other, Maybe):
            return self._value == other._value
        else:
            return False

    def __ne__(self, other):
        return not (self == other)

    def __bool__(self):
        return self._value is not None

        def add_one(x):
        return x + 1

def double(x):
    return x * 2

result = Maybe(3).bind(add_one).bind(double)
print(result)  # Just 8

result = Maybe(None).bind(add_one).bind(double)
print(result)  # Nothing

result = Maybe(None).bind(add_one).bind(double).orElse(10)
print(result)  # Just 10

result = Maybe(None) | Maybe(1)
print(result) # Just 1
```

In this example, we define a `Maybe` monad that represents a value that may or may not be present. The `Maybe` monad has a `bind` method that applies a function to the value if it is present, and returns a new `Maybe` monad with the result. The `orElse` method returns a default value if the value is not present. The `__or__` method allows us to combine two `Maybe` monads using the `or` operator.

We're also adding dunder methods for handling of the monad, such as `__str__`, `__repr__`, `__eq__`, `__ne__`, and `__bool__`. These methods allow us to print the monad, compare it with other monads, and check if it has a value.


## Functools

Python has a module called `functools` that provides higher-order functions and operations on callable objects. This module is very useful for functional programming in Python, as it provides tools for working with functions as first-class objects.

Here's an example of using the `reduce` function from the `functools` module to calculate the sum of a list of numbers:

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(
    # This lambda is our function that will be applied to the list
    lambda current_value, next_value:
        current_value + next_value,

    # The list we're gonna iterate over
    numbers
)
```

We're using `reduce` with a lambda that sums pairs of numbers in the list, and the result is the sum of all numbers in the list.

`reduce`, if we implemented it, would look like:

```python
def reduce(func, iterable, initializer=None):
    # Get an iterator from the list (or any iterable object really)
    it = iter(iterable)

    # If an initializer is provided, use it as the initial value
    # This is optional, we're not using it in the example above
    if initializer is None:
        # "next" calls the iterator only once,
        # so we can get the first value if no initializer is provided
        value = next(it)
    else:
        # Otherwise, let the initializer be the initial value
        value = initializer

    # Here, we're gonna use the iterator and accumulate the values provided by the function, passing the value and the next element
    for element in it:
        value = func(value, element)

    return value
```

And that's it! We've implemented a simple version of `reduce` using a for loop and an iterator. This is a very simple implementation, and the real `reduce` function in Python is more complex and optimized.

There's also the `map` and `filter` functions, which are also available in the `functools` module. These functions are used to apply a function to each element of an iterable and filter elements from an iterable, respectively. They work just as their names suggest (mapping and filtering). Here's an example of using `map` and `filter`:

```python
from functools import map, filter

numbers = [1, 2, 3, 4, 5]

# Map
squared_numbers = map(
    lambda x: x ** 2,
    numbers
)

# Filter
even_numbers = filter(
    lambda x: x % 2 == 0,
    numbers
)
```

Just like their JavaScript counterparts, we can use `map` to apply a function to each element of a list into a new one, and `filter` to filter elements from a list based on a condition.

By the way, [here's a full list of the functions provided by functools](https://docs.python.org/3/library/functools.html).

## Conclusion

Thanks for staying! We've covered a lot of ground in this course, and I hope you've learned a lot about Python and programming in general. Functional programming is a powerful paradigm that can help you write more concise, readable, and maintainable code. By understanding the core concepts of functional programming, you can become a more effective programmer and build better software.

## Assignment

1. Write a program that implements a monad that reads a comma-separated string of numbers and returns a "Series" monad. Then implement the following functions:

- `get`: Gets an index of the series
- `then`: Applies a lambda in the previous result, if it's not None
- `else`: Applies a lambda in the previous result, if it's None

Usage example:

```python
series = Series("1,2,3,4,5")
series.get(2).then(lambda x: x * 2).else(lambda: 0)  # Output: 6, because 3 * 2 is 6
series.get(10).then(lambda x: x * 2).else(lambda: 0)  # Output: 0, because 10 is out of bounds
```

