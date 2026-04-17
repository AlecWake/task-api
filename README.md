# Task API

A FastAPI-based task management API that supports full CRUD operations using PostgreSQL and SQLAlchemy for persistent data storage.

## Features
- Create tasks
- Retrieve all tasks
- Retrieve a single task by ID
- Search tasks with query parameters (`title`, `completed`)
- Update tasks partially with PATCH
- Replace tasks fully with PUT
- Delete tasks

## Tech Stack
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Uvicorn

## Project Structure
project/
│── main.py
│── database.py
│── models.py
│── requirements.txt
│── README.md
│── routers/
│   └── tasks.py
│── schemas/
│   └── task.py

## Key Concepts Implemented
- FastAPI routing for clean endpoint organization
- Pydantic schemas for request and response validation
- SQLAlchemy ORM for database interaction
- PostgreSQL integration for persistent storage
- CRUD operations using real database data
- Query filtering with optional search parameters
- Proper HTTP status codes and error handling

## API Endpoints
- `GET /`
- `GET /tasks`
- `GET /tasks/search`
- `GET /tasks/{task_id}`
- `POST /tasks`
- `PATCH /tasks/{task_id}`
- `PUT /tasks/{task_id}`
- `DELETE /tasks/{task_id}`

## Example Request Body
### Create Task
```json
{
  "title": "Finish backend roadmap work"
}