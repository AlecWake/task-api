from fastapi import FastAPI, HTTPException

app = FastAPI()

tasks = [
    {"id": 1, "title": "Learn FastAPI", "completed": False},
    {"id": 2, "title": "Build first endpoint", "completed": True},
    {"id": 3, "title": "Practice query params", "completed": False}
]

@app.get("/")
def root():
    return {"current": "Task API is running"}

@app.get("/tasks/{task_id}")
def get_tasks(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code = 404, detail = "Item not Found")

@app.get("/tasks/search")
def search(completed: bool = None, title = None: str = None):
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