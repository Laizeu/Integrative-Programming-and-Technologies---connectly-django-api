# Connectly Django API

Connectly Django API is a backend REST API built with Django for managing users and posts. The project demonstrates core backend development concepts including CRUD operations, validation, relational data handling, API security, and scalable design patterns.

The API has been extended with social interaction features such as likes and comments, Google OAuth authentication, and a personalized news feed with sorting and pagination.

The endpoints were tested using Postman.


## Features
### Core API Features
- CRUD operations for Users and Posts
- Input validation for API requests
- Relational data integrity using Django models
- Secure authentication
- Password encryption
- HTTPS support
- Role-based access control
### Design Improvements
- Singleton Pattern for shared resources
- Factory Pattern for modular object creation
- Improved scalability and maintainability
### Social Interaction Features
- Users can like posts
- Users can comment on posts
- Retrieve comments for a specific post
- Post details include like count and comment count
###  Authentication
- Google OAuth login integration
- Secure login using Google accounts
### News Feed System
- Personalized news feed endpoint
- Sorting posts by date
- Pagination support for efficient data retrieval

## Tech Stack
Backend Framework
- Django

API Framework
- Django REST Framework

Authentication
- Google OAuth
- Django authentication system
  
Database
- SQLite (development)

Tools
- Postman (API testing)

## Setup & Run
1. Clone the repo 
2. Create & activate virtual environment
   ```bash
   cd connectly_project
   python3 -m venv env
   source env/bin/activate
3. Install dependencies
   ```bash
   pip install -r requirements.txt
4. Run migrations
   ```bash
   python3 manage.py migrate
5. Start server
   - Standard server
   ```bash
   python3 manage.py runserver
   ```
   - HTTPS server
   ``` bash
   python3 manage.py runserver_plus --cert-file cert.pem --key-file key.pem
   ```

## API Endpoints

## Base
```test
- https://127.0.0.1:8000
```
## Users
```text
- GET /posts/users/
- POST /posts/users/create/
```
```bash
{"username":"laiza","email":"laiza@example.com"}.
```
## Posts
```text
- GET /posts/posts/                                   # Retrieve all posts
- POST /posts/posts/create                            # Create a new post
```
```bash
{"content":"Hello this is Laiza's first post!","author":1}
```
## Likes
```text
- POST  /posts/{id}/like/                              # Like a post
```
## Comments
```text
- POST http://127.0.0.1:8000/posts/7/comment/          # Add comment to a post
- GET http://127.0.0.1:8000/posts/1/comments/          # Retrieve comments for a post
```
```bash
{
  "text": "This is a comment by Laiza",
  "author": 1,
  "post": 1
}
```
## Authentication
```text
- POST  /api/token/                          # Request authentication token
- POST  /auth/google/login/                  # Google OAuth login
- GET   /accounts/google/login/              # Start Google OAuth login
- GET   /accounts/google/login/callback/     # Google OAuth callback
```
## News Feed
```text
- GET   /posts/feed/                         # Retrieve personalized news feed
- GET   /posts/feed/?ordering=-created_at    # Sort posts by newest
- GET   /posts/feed/?page=1                  # Pagination (page 1)
- GET   /posts/feed/?page=2                  # Pagination (page 2)
```

## File Structure
```text
connectly_project/
│
├── config/                 # Project configuration
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── posts/                  # Posts application
│   ├── migrations/
│   │   └── 0001_initial.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py           # Post, Like, Comment models
│   ├── urls.py             # API routes
│   ├── views.py            # API endpoints logic
│   └── tests.py
│
├── env/                    # Virtual environment
├── db.sqlite3              # SQLite database
├── requirements.txt
├── manage.py               # Django management script
└── README.md
```

### Author
```md
IPT Group 10
