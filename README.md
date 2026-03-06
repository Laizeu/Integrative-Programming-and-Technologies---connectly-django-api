# Connectly Django API

## Project Branch

The **final and latest tested version** of this project is located in the branch:

**Milestone-2**

All features for Milestone 2 (Likes, Comments, Google OAuth integration, and News Feed with sorting and pagination) were consolidated, merged, committed, and pushed to this branch.

To use the latest version of the project:

```bash
git checkout Milestone-2
```


# AI Disclosure Statement

```markdown
AI tools (such as ChatGPT) were used to assist with documentation formatting, explanation of concepts, and guidance for testing API endpoints.  

All system design, implementation, testing, and integration of features (CRUD operations, validation, relationships, security, design patterns, likes, comments, Google OAuth, and news feed functionality) were implemented and verified by the project team.
```

Connectly Django API is a backend REST API built with Django for managing users and posts. The project demonstrates core backend development concepts including CRUD operations, validation, relational data handling, API security, and scalable design patterns.

The API has been extended with social interaction features such as likes and comments, Google OAuth authentication, and a personalized news feed with sorting and pagination.

The endpoints were tested using Postman.

## Project Overview

Connectly is a simplified social media backend API that allows users to create posts, interact through likes and comments, authenticate using Google OAuth, and view a personalized news feed.

The project demonstrates key backend engineering concepts including REST API design, database relationships, authentication, security, pagination, and scalable architecture patterns.

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

### Base URL
```test
- http://127.0.0.1:8000
```
### Users
```text
- GET /posts/users/
- POST /posts/users/create/
```
```json
{"username":"laiza","email":"laiza@example.com"}.
```
### Posts
```text
- GET /posts/posts/                                   # Retrieve all posts
- POST /posts/posts/create                            # Create a new post
```
```json
{"content":"Hello this is Laiza's first post!","author":1}
```
### Likes
```text
- POST  /posts/{id}/like/                              # Like a post
```
### Comments
```text
- POST /posts/{id}/comment/      # Add comment to a post
- GET /posts/{id}/comments/      # Retrieve comments for a post
```
```json
{
  "text": "This is a comment by Laiza",
  "author": 1,
  "post": 1
}
```
### Authentication
```text
- POST  /api/token/                          # Request authentication token
- POST  /auth/google/login/                  # Google OAuth login
- GET   /accounts/google/login/              # Start Google OAuth login
- GET   /accounts/google/login/callback/     # Google OAuth callback
```
### News Feed
```text
- GET   /posts/feed/                         # Retrieve personalized news feed
- GET   /posts/feed/?ordering=-created_at    # Sort posts by newest
- GET   /posts/feed/?page=1                  # Pagination (page 1)
- GET   /posts/feed/?page=2                  # Pagination (page 2)
```
## Testing

All API endpoints were tested using **Postman**.

The following features were tested:

- Token authentication
- News feed retrieval
- Post sorting
- Pagination
- Personalized feed filtering
- Like interactions
- Comment interactions
- Error handling
- Google OAuth authentication

Both successful and error scenarios were verified.

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

## Project Status

Milestone 2 – Completed  
Includes Likes, Comments, Google OAuth authentication, and News Feed with sorting and pagination.

### Author
```md
IPT Group 10
