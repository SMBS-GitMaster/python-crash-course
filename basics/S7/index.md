# Asyncio

## What is asyncio?

Asyncio is a library to write concurrent code using the async/await syntax. It is a library that allows you to write asynchronous code in Python, using the async/await syntax. It defines a set of high-level interfaces that allow you to create tasks and coroutines, and manage their execution.

## Why use asyncio?

Asyncio is useful when you need to write code that performs I/O-bound operations, such as reading from a file, making network requests, or querying a database. By using asyncio, you can write code that performs these operations concurrently, without blocking the main thread of execution.

Asynchronous implementations are imperative in high-performance applications, where you need to perform as many tasks as possible, and leverage the usage of your CPU cores.

## How does asyncio work?

Asyncio works by defining coroutines, which are functions that can be paused and resumed at specific points. Coroutines are defined using the `async def` syntax, and can be paused using the `await` keyword.

When you call an asynchronous function, it returns a coroutine object, which you can then schedule to run using the `asyncio` event loop. The event loop is responsible for running the coroutines concurrently, and managing their execution.

## Example

```python
import asyncio

async def foo():
    await asyncio.sleep(2)
    print("Hello from foo!")

async def bar():
    await asyncio.sleep(1)
    print("Hello from bar!")

async def main():
    task1 = asyncio.create_task(foo())
    await task1
    task2 = asyncio.create_task(bar())
    await task2
```

Take a look at the example above. We define two asynchronous functions, `foo` and `bar`, that sleep for 2 and 1 second respectively, and then print a message. We then define a `main` function that creates tasks for `foo` and `bar`, and awaits for them to complete.

Thanks to `await`, this will print "Hello from foo!" after 2 seconds, and "Hello from bar!" after 3 seconds.

- "3 seconds? why?"

Well, because we're awaiting for `task1` to complete before starting `task2`. If we wanted to run them concurrently, we could have awaited for both tasks at the same time:

```python
async def main():
    task1 = asyncio.create_task(foo())
    task2 = asyncio.create_task(bar())

    # await doeesn't pause currently running tasks, it just pauses the current task (or thread)
    await task1
    await task2

    # or, alternatively:
    # await asyncio.gather(task1, task2)
```

This way, both tasks will run concurrently, and the program will print "Hello from bar!" after 1 second, and "Hello from foo!" after 2 seconds, without leaving the `main()` function until both tasks are done.

## Callbacks

Callbacks are a common pattern in asynchronous programming, where you pass a function as an argument to another function, and that function calls the callback function when it's done.

```python
def callback(result):
    print(f"Result: {result}")

async def async_function(callback):
    result = 42
    await syncio.sleep(1)
    callback(result)

task = asyncio.create_task(async_function(callback))
# Let's continue doing stuff
print("hell yeah we're doing stuff")

# Ok enough, let's wait for the task to finish so it doesn't get cancelled
await task
```

## Conclusion

Asyncio is a powerful library that allows you to write asynchronous code in Python, using the async/await syntax. By defining coroutines and using the asyncio event loop, you can write code that performs I/O-bound operations concurrently, without blocking the main thread of execution. Asyncio is a great tool for writing high-performance applications that need to perform many tasks concurrently, and can help you write more efficient and scalable code.

## Assignments

Since this is the last session, the assignment is in the Assignment folder.
