# python-crash-course

Hello!

During the first three weeks of the course, you'll be implementing a Flask application that will allow users to create, read, update, and delete (CRUD) todos. The application will also have user authentication and authorization.

This repository contains the source files for the final result that I'm expecting to see from all of you. Obviously, you use this repository as a reference, but I encourage you to try to implement the application on your own first.

Good luck!

## Getting started

1. Clone this repository
2. Create a virtual environment
3. Install the dependencies
4. Run the application

### Clone this repository

```bash
git clone https://github.com/coalio/python-crash-course.git
```

### Create a virtual environment

```bash
cd python-crash-course
python3 -m venv venv
```

### Install the dependencies

```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Run the application

```bash
python base.py
```

Or, if you're feeling fancy:

```bash
FLASK_APP=base.py FLASK_ENV=development flask run
```

## Questions? Improvements?

You can add an issue to this repository and I'll get back to you as soon as possible.
