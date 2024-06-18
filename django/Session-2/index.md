# Session 2: Getting Started with Django

**Create an application within the project:**

- In Django, an application is a self-contained module that performs a specific function within your project. To create an app, run the following command in your project directory:
  ```
  python manage.py startapp myapp
  ```
- Replace `myapp` with your desired app name. This will generate the necessary files and directories for your app.

**Add the App to Installed Apps:**

Open the settings.py file in your Django project and add the name of your new app to the INSTALLED_APPS list. This tells Django to include your app in the project.

```python
# settings.py

INSTALLED_APPS = [
    ...
    'myapp',
]

```

**Configure the database (default is SQLite):**

- By default, Django uses SQLite as its database backend. You can configure other databases (such as PostgreSQL or MySQL) in your project's `settings.py` file.
- Locate the `DATABASES` section in `settings.py` and modify the `ENGINE`, `NAME`, `USER`, and `PASSWORD` settings according to your chosen database.

**Run the development server:**

- To start the development server, run:
  ```
  python manage.py runserver
  ```
- This will launch the server at `http://127.0.0.1:8000/`. You can access your Django project there.

**Run the development server:**

Within your Django project's root directory, you'll find individual Django application folders. Each file and folder represents a specific functionality of a Django web app. This modular approach keeps your code organized and allows for independent development and testing of each application.

Here's a brief overview of the key components within an app folder:

- `models.py`: Defines the data models (database tables) for your app.
- `views.py`: Contains the view functions that handle HTTP requests and render templates.
- `urls.py`: Maps URLs to view functions.
- `admin.py`: Registers app-specific models with the Django admin interface.
- `apps.py`: Configuration for the app (e.g., app name, verbose name).
- `migrations/`: Stores database migration files.
- `static/`: Holds static files (CSS, JavaScript, images).
- `templates/`: Contains HTML templates for rendering views.

Remember that this structure promotes modularity, making it easier to maintain and extend your Django project. Feel free to explore and customize each app according to your project's needs! 😊
