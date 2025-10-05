# Movie Ticket Booking Backend

## Overview

This is a Django REST Framework backend for a Movie Ticket Booking System.  
It implements user authentication with JWT, movie management, show scheduling, seat booking, and cancellation.  
Swagger UI is included for API documentation and testing.

---

## Tech Stack

- Python 3.8+
- Django 4+
- Django REST Framework
- djangorestframework-simplejwt (JWT Authentication)
- drf-yasg (Swagger API documentation)
- SQLite (default development database)

---

## Project Structure

movie_booking_backend/
├── backend/ # Django project main folder
│ ├── settings.py # Project settings including JWT & Swagger config
│ ├── urls.py # URL routes including Swagger docs and main app API
│ └── wsgi.py
├── booking/ # Main app containing booking system logic
│ ├── models.py # Django models for Movie, Show, Booking
│ ├── serializers.py # DRF serializers for request/response transformation
│ ├── views.py # API endpoint logic
│ ├── urls.py # App-specific urls for API routes
├── manage.py # Django management commands
└── requirements.txt # Project dependencies

text

---

## Setup Instructions

1. **Clone or download the project folder**

2. **Create and activate a Python virtual environment**

python -m venv env

On Windows (PowerShell):
.\env\Scripts\Activate.ps1

On Windows (cmd):
env\Scripts\activate

On macOS/Linux:
source env/bin/activate

text

3. **Install dependencies**

pip install -r requirements.txt

text

4. **Apply database migrations**

python manage.py makemigrations
python manage.py migrate

text

5. **Create a superuser (for admin access) (optional but recommended)**

python manage.py createsuperuser

text

6. **Run the development server**

python manage.py runserver

text

7. **Accessing the API documentation**

Visit the Swagger UI at:

http://127.0.0.1:8000/swagger/

text

Use this interface to explore and test the API endpoints.

---

## API Endpoints Overview

- `POST /api/signup/` : Register a new user
- `POST /api/login/` : Obtain JWT tokens
- `GET /api/movies/` : List all movies
- `GET /api/movies/{movie_id}/shows/` : List shows for a movie
- `POST /api/shows/{show_id}/book/` : Book a seat for a show (authenticated)
- `POST /api/bookings/{booking_id}/cancel/` : Cancel a booking (authenticated)
- `GET /api/my-bookings/` : List current user's bookings (authenticated)

---

## Notes

- JWT access tokens must be included in the Authorization header for protected endpoints.
- Swagger UI shows locked icons indicating which endpoints require authentication.
- This project uses SQLite by default which is suitable for development/testing.

---

## Contact
 sreenivasreddy533@gmail.com
For questions or issues, please contact the project author.

---

This README provides setup, usage, and API overview for running the Movie Ticket Booking backend project.
