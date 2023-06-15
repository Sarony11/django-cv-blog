# django-cv-blog
This repo wants to demostrate how to create a full stack web app with Django. 

It will not cover how to design html/css templates.

# Steps
### Step 1: Set up a Django project
To begin, make sure you have Django installed on your system. You can use the following command to install Django using pip:

```shell
python -m venv env # create virtual environment for coding
touch requirements.txt
Django==4.2.2 > requirements.txt
pip install -r requirements.txt
```
Once Django is installed, you can create a new Django project by running the following command in your terminal:

```shell
django-admin startproject cv_blog
```

This will create a new directory called "cv_blog" with the basic structure of a Django project.

### Step 2: Create a Django app
In Django, functionality is organized into apps. Each app represents a specific component or feature of your website. For your CV and blogging website, we'll create a separate app for each.

To create a new app, run the following command in your terminal, making sure you're in the root directory of your Django project:

```python
cd cv_blog
python manage.py startapp cv
```

This will create a new directory called "cv" within your project directory, which will contain the files and code for your CV-related functionality. Once created, you also need to edit the file cv_blog/settings.py and add cv app to INSTALLED_APPS = ['cv'].

### Step 3: Configure the database
Django uses a database to store and retrieve data. By default, Django uses SQLite as the database backend, which is a lightweight and easy-to-use database. However, you can also configure Django to use other databases like MySQL or PostgreSQL if needed.

In your project's settings file (`settings.py`), you'll find a `DATABASES` section. By default, it should be configured to use SQLite. If you're okay with using SQLite, you don't need to make any changes. However, if you prefer to use a different database, you'll need to update the settings accordingly.

Here's an example of how the `DATABASES` section looks for SQLite:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
If you want to use a different database, you'll need to provide the appropriate settings for that database, such as the database name, username, password, host, and port.

### Step 4: Define models
In Django, models are used to define the structure and behavior of your data. They represent database tables and encapsulate the data-related logic. For your CV and blogging website, you'll need to define models to represent your CV information and blog posts.

Inside the `cv` app directory, open the `models.py` file and define your models using Django's model classes. Here's an example to get you started:

```python
from django.db import models

class CV(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    class Meta:
        app_label = 'cv'
    # Add more fields as needed

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        app_label = 'cv'
    # Add more fields as needed
```

In this example, we've defined two models: `CV` and `BlogPost`. You can customize the fields based on your specific requirements. Once you've defined the models, save the file.

### Step 5: Create database tables
After defining your models, you need to create the corresponding database tables. Django provides a handy command called makemigrations to generate the necessary database migration files based on your model changes, and then the migrate command to apply those migrations and create the tables.

Run the following commands in your terminal:

```shell
python manage.py makemigrations
python manage.py migrate
```
The makemigrations command will analyze your models and generate migration files based on the changes detected. The migrate command will apply those migrations and create the corresponding database tables.


### Step 6: Register models in the admin site
Django provides an admin site that allows you to manage your application's data through a user-friendly interface. To make your models accessible in the admin site, you need to register them.

Open the `admin.py` file within your `cv` app directory. Add the following code to register your models:

```python
from django.contrib import admin
from .models import CV, BlogPost

admin.site.register(CV)
admin.site.register(BlogPost)
```

By registering the models, Django will generate the necessary UI for you to perform CRUD (Create, Read, Update, Delete) operations on your CV and blog post data within the admin site.

### Step 7: Create views
Views in Django handle the logic of your web application. They receive requests from users, process the data, and return responses. In this step, we'll create views for displaying your CV and blog posts.

Inside the `cv` app directory, create a new file called `views.py`. Open the file and add the following code:

```python
from django.shortcuts import render
from .models import CV, BlogPost

def home_view(request):
    home = CV.objects.first()
    return render(request, 'home.html', {'home': home})

def cv_view(request):
    cv = CV.objects.first()
    return render(request, 'cv.html', {'cv': cv})

def blog_post_list_view(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'blog_post_list.html', {'blog_posts': blog_posts})

def blog_post_detail_view(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog_post_detail.html', {'blog_post': blog_post})
```

In this example, we've defined some views: `home_view`, `cv_view` and `blog_post_list_view`. `home_view` is going to be the home page and the root "/", rending the ``home.html` template. The `cv_view` retrieves the first CV object from the database and renders the `cv.html` template, passing the `cv` object to the template context. The `blog_post_list_view` retrieves all blog posts from the database and renders the `blog_post_list.html` template, passing the list of blog posts to the template context.

### Step 8: Create templates
Templates in Django define how your web pages should look. In this step, we'll create templates for displaying your home, CV and blog posts.

Inside the `cv` app directory, create a new directory called `templates`. Inside the `templates` directory, create another directory called `cv`. This is where we'll store the templates for the CV-related functionality.

Create a new file called `cv.html` inside the `cv` directory. Open the file and add the HTML and template tags to structure your CV page. You can customize the content and design based on your preferences and requirements.

Here's a basic example to get you started:

```html
<!DOCTYPE html>
<html>
<head>
    <title>CV</title>
</head>
<body>
    <h1>{{ cv.title }}</h1>
    <p>{{ cv.description }}</p>
</body>
</html>
```

Similarly, create another directory called `blog` inside the `templates` directory. Inside the `blog` directory, create a file called `blog_post_list.html`. Open the file and add the HTML and template tags to structure your blog post list page. Again, you can customize the content and design as needed.

Here's a basic example:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Blog</title>
</head>
<body>
    <h1>Blog Posts</h1>
    <ul>
        {% for post in blog_posts %}
            <li>{{ post.title }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

These are just simple examples to illustrate the structure. You can enhance and style the templates according to your preferences. To finish this you can also create a new file called `home.html` and add:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Homepage</title>
</head>
<body>
    <h1>Welcome to My Website</h1>
    <p>This is the homepage.</p>
</body>
</html>
```

### Step 9: Define URL patterns
URL patterns in Django determine how URLs are mapped to views. In this step, we'll define the URL patterns for your CV and blog post functionality.

Inside the `cv` app directory, create a new file called `urls.py`. Open the file and add the following code:

```python
from django.urls import path
from . import views

app_name = 'cv'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('cv/', views.cv_view, name='cv'),
    path('blog/', views.blog_post_list_view, name='blog_post_list'),
]
```

In this example, we've defined two URL patterns. The first URL pattern maps the `/cv/` URL to the `cv_view` view, and the second URL pattern maps the `/blog/` URL to the `blog_post_list_view` view.

### Step 10: Include app URLs in the project URLs
To make your app's URLs accessible in your project, you need to include them in the project's URL configuration.

Open the `urls.py` file in your project's directory (not the one inside the `cv` app directory) and add the following code:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cv.urls')),
]
```

In this code, we've included the `cv.urls` module using the `include()` function. This will include the URLs defined in the `urls.py` file inside the `cv` app.

### Step 11: Create superuser
To access the Django admin site and manage your CV and blog post data, you need to create a superuser account. The superuser account has full privileges to perform administrative tasks.

In your terminal, run the following command:

```
python manage.py createsuperuser
```

You'll be prompted to provide a username, email (optional), and password for the superuser. Follow the prompts and provide the required information.

Once the superuser is created, you can use the provided credentials to log in to the admin site at `http://localhost:8000/admin/` (assuming you're running the development server locally).

### Step 12: Create URLs for blog post detail view
In addition to the blog post list view, it's common to have a detail view for each individual blog post. We'll now create URLs and views for the blog post detail view.

In the `urls.py` file inside the `cv` app directory, add the following code below the existing URL patterns:

```python
from django.urls import path
from . import views

app_name = 'cv'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('cv/', views.cv_view, name='cv'),
    path('blog/', views.blog_post_list_view, name='blog_post_list'),
    path('blog/<int:pk>/', views.blog_post_detail_view, name='blog_post_detail'),
]
```

In this code, we've added a new URL pattern that captures an integer parameter (`<int:pk>`) representing the primary key of the blog post. It maps to the `blog_post_detail_view` view, which will be responsible for displaying the details of a specific blog post.

### Step 15: Style your templates with CSS (optional)
To enhance the visual appeal of your website, you can style your templates using CSS. You can create a separate CSS file or add inline styles within your HTML templates.

Here's a basic example of adding inline styles to the `cv.html` template:

```html
<!DOCTYPE html>
<html>
<head>
    <title>CV</title>
    <style>
        h1 {
            color: #333;
            font-size: 24px;
        }
        p {
            color: #666;
            font-size: 16px;
        }
    </style>
</head>
<body>
    <h1>{{ cv.title }}</h1>
    <p>{{ cv.description }}</p>
</body>
</html>
```

In this example, we've added inline styles to customize the appearance of the heading and paragraph elements.

You can also link an external CSS file to your templates by adding a `<link>` tag within the `<head>` section of your HTML templates. For example:

```html
<!DOCTYPE html>
<html>
<head>
    <title>CV</title>
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>
<body>
    <!-- Rest of the template -->
</body>
</html>
```

Make sure to create a `styles.css` file inside a `css` directory in your project's static files directory, and define your CSS styles in that file.

### Step 16: Test your website
At this point, you have set up the necessary components for your CV and blogging website in Django. It's time to test your website and see it in action!

Start the Django development server by running the following command in your terminal:

```shell
python manage.py runserver
```

This will start the server, and you should see output similar to:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Open your web browser and navigate to `http://127.0.0.1:8000/cv/` to view your CV page. Verify that the CV information is displayed correctly.

Next, navigate to `http://127.0.0.1:8000/blog/` to view the list of blog posts. Make sure the blog post titles are shown.

To test the blog post detail view, you can click on one of the blog post titles in the list to see the individual blog post page.

Ensure that everything looks and functions as expected.

## Database Management

### Add data to the database from the admin console
Once you have the superuser created, run the development server (python manage.py runserver) and access the admin interface by visiting http://127.0.0.1:8000/admin/. Log in with your superuser credentials and navigate to the CV model's admin page. From there, you can add new CV objects and fill in the necessary details.

### Add data to the database as code
Now, you can add data to the CV table. You can do this by either using the Django admin interface or programmatically in a script or Django shell.

To add data via the Django admin interface, you'll need to create a superuser first (if you haven't already done so). Run the following command and follow the prompts:

Alternatively, you can add data programmatically by writing a script or using the Django shell. Here's an example of how you can add a CV object in the Django shell:

```shell
python manage.py shell
```

Once in the shell, run the following commands:
```python
from cv.models import CV

cv = CV.objects.create(title='My CV', description='This is my CV description')
```

This will create a new CV object with the specified title and description.

After following these steps, you should have the CV model correctly defined and some data added to the CV table in the database. Verify that the data is present in the database and then restart the development server (python manage.py runserver). Access the cv URL to see if the CV title and description are displayed correctly on the page.