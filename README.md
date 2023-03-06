# Django Storefront Intro to Django Project
A storefront project the introduces the user/coder to the fundamentals of django such as Views, Models, Migrations, and connecting your DB to Django.

## To create project 
1. Install django inside a created virtual environment:
```bash
pipenv install django
``` 

2. Activate virtual environment (exit with 'exit' or ctrl+d) so we can use the python interpreter 
```bash
pipenv shell
``` 
3. Start and name a new project project ('.' tells django to use the current directory as the project directory). django-admin is a utility that comes with django and allows you to use runserver, migrate, etc
```bash
django-admin startproject name_of_project .
``` 

4. Manage.py is now a wrapper around django-admin so from now on use manage.py instead of django-admin Start up server 
```bash
python3 manage.py runserver
``` 

## To add an app to our django application
Create it first:

```bash
python manage.py startapp app_name
``` 

Register it in the settings module of the root app (setting.py file):

INSTALLED_APPS = [
    ...,
    'app_name',
    ...
]

## View
- Request Handler
- here we write functions that take a request and return a response
- You can take a view at my Playground app and view how thats set up as well as take a look at setting up templates, and mapping the urls to views 

## Building Data Models
Note: Take a look at Model Diagrams to view what our Models should look like 

Models are used to define what structure your DB will take 
There are 5 type of relationships that were implemented:

1. one to one
2. one to many
3. many to many 
4. circular 
5. generic 

You can take a look at store for a view of one to one, one to many, and many to many relationship examples.
Similarly, you can take a look at likes app to view generic relationship implementation. 

## Database and Migrations

Migrations are used to create update our DB tables off our models. In order to RUN A MIGRATION:

```bash
python manage.py makemigrations
``` 

Run makemigrations every time you make changes to models.
Then to EXECUTE ALL PENDING MIGRATIONS:

```bash
python manage.py migrate
``` 

which will return a db.sqlite3 file where you can view your tables/or if you have a db connected(MySQL) all the migrations 
will be applied to it. 

To REVERT MIGRATIONS:
```bash
python manage.py migrate app_name number_of_migration
``` 

Note:

To fix _mysql is not defined, Django on Mac M1 with MySQL DB error

```bash
(mach-o file, but is an incompatible architecture (have 'x86_64', need 'arm64'))
    version_info, _mysql.version_info, _mysql.__file__
NameError: name '_mysql' is not defined
``` 

we do , 
1. 
```bash
pipenv shell

pipenv install pymysql
``` 
2. At the beginning of the settings.py in my main folder, I add:
``` 
import pymysql
``` 

3. Followed by, somewhere near the top of this file (I added it after the databases section):
``` 
# Fake PyMySQL’s version and install as MySQLdb

# https://adamj.eu/tech/2020/02/04/how-to-use-pymysql-with-django/

pymysql.version_info = (1, 4, 2, “final”, 0)

pymysql.install_as_MySQLdb()
``` 

## Django ORM (object relational mapper)
Django ORM maps object to relational records and lets you interact with your database.

For examples look at playground folder -> views.py and you'll see a couple examples

Most of the methods return 