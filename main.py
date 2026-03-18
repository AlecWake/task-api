from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

tasks = [
    {"id": 1, "title": "Learn FastAPI", "completed": False},
    {"id": 2, "title": "Build first endpoint", "completed": True},
    {"id": 3, "title": "Practice query params", "completed": False}
]

class TaskCreate(BaseModel):
    title: str

class TaskUpdate(BaseModel):
    title: str = None
    completed: bool = None

class TaskReplace(BaseModel):
    title: str
    completed: bool

@app.get("/")
def root():
    return {"current": "Task API is running"}

@app.get("/tasks/search")
def search(completed: bool = None, title: str = None):
    results = []
    if title != None and completed != None:
        for task in tasks:
            if (task["completed"] == completed) and (title.lower() in task["title"].lower()):
                results.append(task)
        return results
    elif title != None and completed == None:
        for task in tasks:
            if (title.lower() in task["title"].lower()):
                results.append(task)
        return results
    elif title == None and completed != None:
        for task in tasks:
            if (task["completed"] == completed):
                results.append(task)
        return results
    else:
        return tasks

@app.get("/tasks/{task_id}")
def get_tasks(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code = 404, detail = "Item not Found")

@app.post("/tasks")
def create_task(task: TaskCreate):
    largest_id = -1
    if tasks == []:
        largest_id = 0
    else:
        for single_task in tasks:
            if single_task["id"] > largest_id:
                largest_id = single_task["id"]
    tasks.append({"id": largest_id + 1, "title": task.title, "completed": False})
    return {"id": largest_id + 1, "title": task.title, "completed": False}

@app.delete("/tasks/{id_to_delete}", status_code = 204)
def delete_task(id_to_delete: int):
    index = 0
    for task in tasks:
        if task["id"] == id_to_delete:
            del tasks[index]
            return
        index += 1
    raise HTTPException(status_code = 404, detail = "Item not Found")

@app.patch("/tasks/{task_id}")
def update_task(task_id: int, update: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            if update.title is not None:
                task["title"] = update.title
            if update.completed is not None:
                task["completed"] = update.completed
            return task
    raise HTTPException(status_code=404, detail="Item not Found")

@app.put("/tasks/{task_id}")
def replace_task(task_id: int, update: TaskReplace):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = update.title
            task["completed"] = update.completed
            return task
    raise HTTPException(status_code=404, detail="Item not Found")       