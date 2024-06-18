# Setting Up a Django Project

## Steps

- [ ] **Install Python and pip**

  To start, you need to have Python and pip installed on your system. You can download the latest version of Python from the official [Python website](https://www.python.org/downloads/). Pip is usually included with Python, but you can verify its installation by running:

  ```bash
  python -m ensurepip --upgrade
  ```

- [ ] **Set up a virtual environment**

  Creating a virtual environment helps manage dependencies for your project. You can create a virtual environment using the following command:

  ```bash
  python -m venv myenv
  ```

  Replace `myenv` with the name of your virtual environment. To activate it, use:

  ```bash
  # On Windows
  myenv\Scripts\activate

  # On macOS/Linux
  source myenv/bin/activate
  ```

- [ ] **Install Django using pip**

  With the virtual environment activated, you can install Django by running:

  ```bash
  pip install django
  ```

- [ ] **Create a new Django project**

  Once Django is installed, you can create a new project by using the `django-admin` command:

  ```bash
  django-admin startproject myproject
  ```

  Replace `myproject` with the name of your project.

- [ ] **Understand the structure of a Django project**

  After creating a new Django project, it's important to understand its structure. Here is a brief overview:

  - `manage.py`: A command-line utility that lets you interact with your project.
  - The project directory (same name as your project) contains:
    - `__init__.py`: An empty file that tells Python this directory should be considered a Python package.
    - `settings.py`: Settings/configuration for your Django project.
    - `urls.py`: URL declarations for this Django project; a “table of contents” of your Django-powered site.
    - `wsgi.py`: An entry-point for WSGI-compatible web servers to serve your project.
    - `asgi.py`: An entry-point for ASGI-compatible web servers to serve your project (if you're using Django with ASGI).

  This basic setup provides a solid foundation for starting a Django project. You can now begin developing your application.

  For more information visit [Django documentation](https://www.djangoproject.com/).
