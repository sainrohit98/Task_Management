# Task Management API

## Overview

This project is a simple Task Management API built using Django and Django REST Framework. The API provides functionalities for user authentication, task management, and task member management.

## Features

- **User Authentication**: Register and login using token-based authentication.
- **Task Management**: 
  - Create, read, update, and delete tasks.
  - Assign members to tasks.
  - Update task status (Todo, Inprogress, Done).
- **Task Member Management**: Add or remove members from a task and view the list of members associated with a task.

## Requirements

- Python 3
- Django 
- Django REST Framework
- SQLite (default database, but you can change to another database if needed)

## Setup Instructions

1. **Clone the repository**:

    ```bash
    git clone https://github.com/sainrohit98/Task_Management.git
    cd task_management
    ```

2. **Create a virtual environment and activate it**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run migrations**:

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser** (optional, for accessing the admin panel):

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

## API Endpoints

### Authentication

- **Register a new user**: `POST /register/`
- **Login**: `POST /login/`

### Tasks

- **List/Create Tasks**: `GET/POST /tasks/`
- **Retrieve/Update/Delete Task**: `GET/PUT/DELETE /tasks/{id}/`
- **Update Task Status**: `PATCH /tasks/{id}/status/`
- **Manage Task Members**: `PUT /tasks/{id}/members/manage/`
- **View Task Members**: `GET /tasks/{id}/members/`

## Usage

- **Register a new user**:

    ```bash
    POST /register/
    {
        "username": "testuser",
        "password": "testpassword",
        "email": "testuser@example.com"
    }
    ```

- **Login**:

    ```bash
    POST /login/
    {
        "username": "testuser",
        "password": "testpassword"
    }
    ```

    This will return an authentication token that should be used in the `Authorization` header for subsequent requests:

    ```
    Authorization: Token your_token_here
    ```

- **Create a task**:

    ```bash
    POST /tasks/
    {
        "title": "New Task",
        "description": "Task description",
        "due_date": "2024-08-20"
    }
    ```

- **Update task status**:

    ```bash
    PATCH /tasks/{id}/status/
    {
        "status": "Inprogress"
    }
    ```

- **Add members to a task**:

    ```bash
    PUT /tasks/{id}/members/manage/
    {
        "members": [1, 2]  # List of user IDs
    }
    ```

