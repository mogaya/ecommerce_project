# Authentication Setup

This API uses Django’s built-in authentication system with Basic Authentication. Here’s how to test and use authentication:

Authentication Method:

Basic Authentication: Requires a username and password in the request headers.
Setup Steps:

Clone the repository.
Install dependencies:

pip install -r requirements.txt

Run the server:

python manage.py runserver

Create a superuser:

python manage.py createsuperuser

How to Test:

Use Postman to add an Authorization header:
Key: Authorization
Value: Basic <base64-encoded-username:password>
Access a protected endpoint (e.g., /api/products/list).
Ensure a 200 OK response with valid credentials or 401 Unauthorized for invalid ones.
