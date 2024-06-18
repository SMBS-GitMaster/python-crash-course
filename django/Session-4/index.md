# Session 4: Working with Django Models

A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.

**The basics**:

1. Each model is a Python class that subclasses django.db.models.Model.
2. Each attribute of the model represents a database field.
3. With all of this, Django gives you an automatically-generated database-access

**Create Data Models:**

- In Django, models define the structure of your database tables. Create a model for your `TODO` items.
- Example model (`myapp/models.py`):

  ````python
  from django.db import models

  class Todo(models.Model):
      title = models.CharField(max_length=255)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      deleted_at = models.DateTimeField(null=True, blank=True)
      updated_at = models.DateTimeField(auto_now=True)

      def __str__(self):
      return self.title
       ```

  ````

**_Using models_**

Once you have defined your models, you need to tell Django you’re going to use those models. Do this by editing your settings file and changing the INSTALLED_APPS setting to add the name of the module that contains your models.py.

For example, if the models for your application live in the module myapp.models (the package structure that is created for an application by the manage.py startapp script), INSTALLED_APPS should read, in part:

- Run `python manage.py makemigrations` to create migration files.

**Migrations and How to Apply Them:**

- Migrations are scripts that apply changes to your database schema. Run:
  ```
  python manage.py migrate
  ```
- This will create the necessary database tables based on your models.

**Basic CRUD Operations with Models (Create, Read, Update, Delete):**

- Create a new `TODO` item:
  ```python
  todo = Todo.objects.create(title='Buy groceries', content='Milk, eggs, bread')
  ```
- Retrieve all `TODO` items:
  ```python
  todos = Todo.objects.all()
  ```
- Update a `TODO` item:
  ```python
  todo.title = 'Buy fruits'
  todo.save()
  ```
- Delete a `TODO` item:
  ```python
  todo.delete()
  ```

For more information visit [Django Models](https://docs.djangoproject.com/en/5.0/topics/db/models/)
