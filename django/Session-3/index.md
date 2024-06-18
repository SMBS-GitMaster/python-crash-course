# Session 3: Exploring Django Views, URLs, and Templates

1. **Create and Understand Basic Views:**

   - Views in Django handle HTTP requests and return appropriate responses. To create a basic view:
     - Define a function in your app's `views.py` file.
     - Map a URL to this view in your app's `urls.py`.
     - Example view function:
       ```python
       def hello_world(request):
           return HttpResponse("Hello, world!")
       ```

2. **Configure URLs:**

   - URLs are defined in your app's `urls.py`. Each URL pattern is associated with a view function.
   - Example URL configuration:

     ```python
     from django.urls import path
     from . import views

     urlpatterns = [
         path('hello/', views.hello_world, name='hello-world'),
     ]
     ```

3. **Introduction to Templates:**

   - Templates allow you to separate HTML from Python code. Create a `templates/` folder in your app.
   - Example template (`myapp/templates/myapp/hello.html`):
     ```html
     <!DOCTYPE html>
     <html>
       <head>
         <title>Hello World</title>
       </head>
       <body>
         <h1>Hello, {{ name }}!</h1>
       </body>
     </html>
     ```

4. **Render Templates from Views:**

   - In your view function, use the `render` shortcut to render a template:

     ```python
     from django.shortcuts import render

     def hello_world(request):
         return render(request, 'myapp/hello.html', {'name': 'Django'})
     ```

     - This passes the `name` variable to the template.
