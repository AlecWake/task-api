from fastapi import FastAPI, HTTPException
from routers import tasks

app = FastAPI()

@app.get("/")
def root():
    return {"current": "Task API is running"}

app.include_router(tasks.router, prefix = "/tasks")