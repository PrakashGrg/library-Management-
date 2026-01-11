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


```github

git add .

git commit -m "text"

git push origin main