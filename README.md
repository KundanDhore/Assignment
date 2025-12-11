# Bookstore & Weather Django App

A modular Django web application featuring a RESTful Bookstore API with a dynamic frontend and a Weather dashboard integrating external third-party data.

## Project Overview

This project demonstrates a hybrid Django architecture:
1.  **Bookstore App:** A full CRUD system using **Django REST Framework** (backend) and **JavaScript Fetch API** (frontend).
2.  **Weather App:** A server-side rendered dashboard that consumes the **WeatherAPI.com** external API.
3.  **Database:** Powered by **PostgreSQL**.

## Tech Stack
* **Backend:** Python 3, Django 4+, Django REST Framework (DRF)
* **Database:** PostgreSQL
* **Frontend:** HTML5, Bootstrap 5, Vanilla JavaScript (ES6)
* **External API:** WeatherAPI.com, Python `requests` library

**Installation & Setup Guide**

Follow the steps below to set up and run the project on your local machine.

**1. Clone the Repository**
git clone <your-repo-url>
cd bookstore_project

**2. Create and Activate Virtual Environment**
python -m venv venv
venv\Scripts\activate

**3. Install Dependencies**
pip install django djangorestframework psycopg2-binary requests

**4. Database Configuration**
**A. Create the PostgreSQL Database**
Open terminal or pgAdmin and run:

psql -U postgres
CREATE DATABASE bookstore_db;
\q

**B. Update Django Settings**

Edit bookstore_project/settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bookstore_db',
        'USER': 'postgres',          # Replace with your Postgres username
        'PASSWORD': 'your_password', # Replace with your Postgres password
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

**5. API Key Configuration**

Add your WeatherAPI key inside weather/views.py:

# weather/views.py
api_key = 'YOUR_WEATHERAPI_KEY_HERE'

**6. Run Migrations**
python manage.py makemigrations
python manage.py migrate

**7. Run the Development Server**
python manage.py runserver

