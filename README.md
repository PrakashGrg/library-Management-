# Library Management API

Complete Django REST API for book management with admin, Swagger docs, and filtering.

##  Quick Setup

```powershell
# 1. Create environment
python -m venv env
env\Scripts\Activate.ps1

# 2. Install dependencies
pip install --upgrade pip
pip install django==5.1 djangorestframework drf-yasg django-jazzmin django-filter

# 3. Setup project
django-admin startproject myproject .
python manage.py startapp library

# 4. Create code files (models.py, views.py, etc.)
# Copy from project files...

# 5. Database migrations
python manage.py makemigrations
python manage.py migrate

# 6. Create admin user
python manage.py createsuperuser

# 7. Run server
python manage.py runserver


## gitHub

git add .

git commit -m "text"

git push origin main

1.  Django REST Framework Tutorial
    https://www.django-rest-framework.org/tutorial/quickstart/
    "Official DRF tutorial - exact CRUD + serializers"

2.  Django Models & Validation
    https://docs.djangoproject.com/en/5.1/topics/db/models/#validating-objects
    "How clean() method works for future date validation"

3.  Django Admin Customization
    https://docs.djangoproject.com/en/5.1/ref/contrib/admin/#modeladmin-objects
    "List_display, filters, search_fields exactly like your project"

4.  STEP-BY-STEP TUTORIALS
    Django + DRF CRUD Tutorial
    https://www.geeksforgeeks.org/python/django-rest-api-crud-with-drf/​
    "Complete ListCreateAPIView + RetrieveUpdateDestroyAPIView"

5.  Django Library Management
    https://pythongeeks.org/django-library-management-system/​
    "Book model + CRUD operations tutorial"

6.  DRF Filtering Tutorial
    https://www.django-rest-framework.org/api-guide/filtering/#djangofilterbackend
    "Exact genre & is_available filtering code"

7.  PACKAGE DOCUMENTATION
    Jazzmin Admin
    https://django-jazzmin.readthedocs.io/
    "Beautiful admin setup exactly like JAZZMIN_SETTINGS"

8.  drf-yasg Swagger
    https://drf-yasg.readthedocs.io/en/stable/
    "Exact schema_view + swagger/redoc setup"

9.  TESTING REFERENCES
    Django Testing Docs
    https://docs.djangoproject.com/en/5.1/topics/testing/tools/#assertraises
    "TestCase + APITestCase for model & API tests"

10. COMPLETE WORKING GITHUB EXAMPLES
    Django Library CRUD
    https://github.com/wpcodevo/Django_Crud_Project​
    "Full working DRF CRUD project"

11. Simple Library API
    https://github.com/BurhanMohammad/Django-librarymanagement​

12. Django REST CRUD (30min)
    https://www.youtube.com/watch?v=KAMNkuqZGzQ

