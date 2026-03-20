# Task API

A FastAPI-based task management API that supports full CRUD operations using an in-memory data store.

## Features
- Create tasks
- Retrieve a single task by ID
- Search tasks with query parameters (title, completed)
- Update tasks partially (PATCH)
- Replace tasks بالكامل (PUT)
- Delete tasks

## Tech Stack
- Python
- FastAPI
- Pydantic

## Project Structure
project/
│── main.py
│── routers/
│ └── tasks.py
│── schemas/
│ └── task.py

## Key Concepts Implemented
- Pydantic schemas for request and response validation
- Separation of concerns using routers
- Clean API structure and endpoint organization
- Proper HTTP status codes and error handling

## Example Endpoints
- `GET /tasks/search`
- `GET /tasks/{task_id}`
- `POST /tasks`
- `PATCH /tasks/{task_id}`
- `PUT /tasks/{task_id}`
- `DELETE /tasks/{task_id}`

## Notes
This project uses an in-memory list for storage and is intended for learning backend fundamentals and API design.