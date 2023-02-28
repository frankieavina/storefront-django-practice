# Django Storefront Intro to Django Project
A storefront project the introduces the user/coder to the fundamentals of django
such as Views, Models, Migrations, and connecting your DB to Django.

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

which will return a db.sqlite3 file where you can view your tables as well

To REVERT MIGRATIONS:
```bash
python manage.py migrate app_name number_of_migration
``` 