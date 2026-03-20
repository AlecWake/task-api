from fastapi import APIRouter, HTTPException
from schemas.task import TaskCreate, TaskReplace, TaskResponse, TaskUpdate

router = APIRouter()

tasks = [
    {"id": 1, "title": "Learn FastAPI", "completed": False},
    {"id": 2, "title": "Build first endpoint", "completed": True},
    {"id": 3, "title": "Practice query params", "completed": False}
]

@router.get("/search")
def search(completed: bool | None = None, title: str | None = None):
    results = []

    for task in tasks:
        if completed is not None and task["completed"] != completed:
            continue

        if title is not None and title.lower() not in task["title"].lower():
            continue

        results.append(task)

    return results

@router.get("/{task_id}", response_model = TaskResponse)
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code = 404, detail = "Item not Found")

@router.post("/", response_model = TaskResponse, status_code = 201)
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

@router.delete("/{task_id}", status_code = 204)
def delete_task(task_id: int):
    index = 0
    for task in tasks:
        if task["id"] == task_id:
            del tasks[index]
            return
        index += 1
    raise HTTPException(status_code = 404, detail = "Item not Found")

@router.patch("/{task_id}", response_model = TaskResponse)
def update_task(task_id: int, update: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            if update.title is not None:
                task["title"] = update.title
            if update.completed is not None:
                task["completed"] = update.completed
            return task
    raise HTTPException(status_code=404, detail="Item not Found")

@router.put("/{task_id}", response_model = TaskResponse)
def replace_task(task_id: int, update: TaskReplace):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = update.title
            task["completed"] = update.completed
            return task
    raise HTTPException(status_code=404, detail="Item not Found")