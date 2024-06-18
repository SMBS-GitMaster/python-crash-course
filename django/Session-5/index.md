# Django Administration

The Django admin application can use your models to automatically build a site area that you can use to create, view, update, and delete records. This can save you a lot of time during development, making it very easy to test your models and get a feel for whether you have the right data. The admin application can also be useful for managing data in production, depending on the type of website. The Django project recommends it only for internal data management (i.e. just for use by admins, or people internal to your organization), as the model-centric approach is not necessarily the best possible interface for all users, and exposes a lot of unnecessary detail about the models.

You must do to add your models to the admin application is to register them. At the end of this article we'll provide a brief demonstration of how you might further configure the admin area to better display our model data.

After registering the models we'll show how to create a new "superuser", login to the site and create some `TODOS`. These will be useful for testing the views and templates we'll start creating in the next tutorial.

## Registering models

First, open admin.py in the catalog application (/django-locallibrary-tutorial/catalog/admin.py). It currently looks like this — note that it already imports django.contrib.admin:

```python
from django.contrib import admin

# Register your models here.

```

Register the models by copying the following text into the bottom of the file. This code imports the models and then calls admin.site.register to register each of them.

```python
from .models import Todos

admin.site.register(Todos)
```

This is the simplest way of registering a model, or models, with the site. The admin site is highly customizable, and we'll talk more about the other ways of registering your models further down.

## Creating a superuser

In order to log into the admin site, we need a user account with Staff status enabled. In order to view and create records we also need this user to have permissions to manage all our objects. You can create a "superuser" account that has full access to the site and all needed permissions using manage.py.

Call the following command, in the same directory as manage.py, to create the superuser. You will be prompted to enter a username, email address, and strong password.

```bash
python3 manage.py createsuperuser
```

Once this command completes a new superuser will have been added to the database. Now restart the development server so we can test the login:

```bash
python3 manage.py runserver
```

## Advance configuration

Django does a pretty good job of creating a basic admin site using the information from the registered models:

1. Each model has a list of individual records, identified by the string created with the model's **str**() method, and linked to detail views/forms for editing. By default, this view has an action menu at the top that you can use to perform bulk delete operations on records.

2. The model detail record forms for editing and adding records contain all the fields in the model, laid out vertically in their declaration order.

You can further customize the interface to make it even easier to use. Some of the things you can do are:

1. List views:

- Add additional fields/information displayed for each record.
- Add filters to select which records are listed, based on date or some other selection value (e.g. Book loan status).
- Add additional options to the actions menu in list views and choose where this menu is displayed on the form.

2. Detail views

- Choose which fields to display (or exclude), along with their order, grouping, whether they are editable, the widget used, orientation etc.
- Add related fields to a record to allow inline editing (e.g. add the ability to add and edit book records while you're creating their author record).

You can find a complete reference of all the admin site customization choices in The Django Admin site [Django Docs](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/).

## Register a ModelAdmin class

To change how a model is displayed in the admin interface you define a ModelAdmin class (which describes the layout) and register it with the model.
