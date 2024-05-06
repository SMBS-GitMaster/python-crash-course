# Working with files

- **Working with files**
  - Reading and writing text files.
  - Read/write operations with binary files.
  - Handling file and directory paths.

## Reading and writing text files.

In Python, we can read and write text files using the built-in `open` function. The `open` function takes two arguments: the name of the file to open and the mode in which to open the file. The mode can be `'r'` for reading, `'w'` for writing, `'a'` for appending, `'r+'` for reading and writing, and `'b'` for binary mode.

Here's an example of reading a text file in Python:

```python
with open('example.txt', 'r') as file:
    data = file.read()
    print(data)
```

In this example, we open the file `example.txt` in read mode (`'r'`) and read its contents using the `read` method. The `with` statement is used to ensure that the file is properly closed after reading. If an exception occurs while reading the file, the file will still be closed.

To write to a text file, you can use the `'w'` mode. Here's an example of writing to a text file:

```python
with open('example.txt', 'w') as file:
    file.write('Hello, world!')
```

In this example, we open the file `example.txt` in write mode (`'w'`) and write the string `'Hello, world!'` to the file using the `write` method. If the file already exists, its contents will be overwritten. If you want to append to the file instead, you can use the `'a'` mode.

## Read/write operations with binary files.

In addition to text files, Python can also read and write binary files. Binary files are files that contain non-textual data, such as images, audio, or video files. To read and write binary files, you can use the `'b'` mode in the `open` function.

Here's an example of reading a binary file in Python:

```python
with open('example.jpg', 'rb') as file:
    data = file.read()
    print(data)
```

In this example, we open the file `example.jpg` in binary read mode (`'rb'`) and read its contents using the `read` method. The contents of the file are stored as a bytes object, which can be used to manipulate the binary data.

To write to a binary file, you can use the `'wb'` mode. Here's an example of writing to a binary file:

```python
with open('example.jpg', 'wb') as file:
    file.write(b'\x00\x01\x02\x03\x04\x05')
```

In this example, we open the file `example.jpg` in binary write mode (`'wb'`) and write the bytes object `b'\x00\x01\x02\x03\x04\x05'` to the file using the `write` method. If the file already exists, its contents will be overwritten.

## Handling file and directory paths.

When working with files and directories in Python, it's important to handle file paths correctly. Python provides the `os.path` module for working with file paths. The `os.path` module contains functions for manipulating file paths, such as joining paths, splitting paths, and checking if a path exists.

Here's an example of joining two paths (base path and relative path) to find a file from the current directory:

```python
import os

# Get the current working directory. The working directory refers to the place where the script is being executed
base_path = os.getcwd()

relative_path = 'example.txt'

file_path = os.path.join(base_path, relative_path)

with open(file_path, 'r') as file:
    data = file.read()
    print(data)
```

In this example, we use the `os.getcwd` function to get the current working directory and then join it with the relative path `'example.txt'` to get the full file path. We then open the file using the full file path and read its contents.

The `os.path` module also provides functions for checking if a path exists, splitting a path into its components, and getting the absolute path of a file or directory. These functions can be useful when working with file paths in Python.

```python
# Check if a path exists
os.path.exists(file_path)

# Split a path into its components
os.path.split(file_path)

# Get the absolute path of a file or directory
os.path.abspath(file_path)
```

# Conclusion

In this guide, we learned how to read and write text files in Python, how to read and write binary files, and how to handle file and directory paths. Working with files is an essential part of programming, and Python provides powerful tools for working with files and directories. By understanding how to work with files in Python, you can build applications that read and write data to files, process binary data, and manipulate file paths with ease.
