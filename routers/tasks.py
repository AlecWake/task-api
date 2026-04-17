from fastapi import APIRouter, HTTPException
from schemas.task import TaskCreate, TaskReplace, TaskResponse, TaskUpdate
from database import SessionLocal
from models import Task

router = APIRouter()

@router.get("/", response_model=list[TaskResponse])
def get_all_tasks():
    db = SessionLocal()
    all_tasks = db.query(Task).all()
    return all_tasks

@router.get("/search", response_model=list[TaskResponse])
def search(completed: bool | None = None, title: str | None = None):
    db = SessionLocal()

    query = db.query(Task)

    if completed is not None:
        query = query.filter(Task.completed == completed)

    if title is not None:
        query = query.filter(Task.title.contains(title))

    results = query.all()

    return results

@router.get("/{task_id}", response_model = TaskResponse)
def get_task(task_id: int):
    db = SessionLocal()
    
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is not  None:
        return task
    raise HTTPException(status_code = 404, detail = "Item not Found")

@router.post("/", response_model = TaskResponse, status_code = 201)
def create_task(task: TaskCreate):
    db = SessionLocal()

    new_task = Task(
        title=task.title,
        completed=False
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

@router.delete("/{task_id}", status_code = 204)
def delete_task(task_id: int):
    db = SessionLocal()

    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code = 404, detail = "Item not Found")
    
    db.delete(task)
    db.commit()
    

@router.patch("/{task_id}", response_model = TaskResponse)
def update_task(task_id: int, update: TaskUpdate):
    db = SessionLocal()

    task = db.query(Task).filter(Task.id == task_id).first()
    
    if task is None:
        raise HTTPException(status_code=404, detail="Item not Found")
    
    if update.title is not None:
        task.title = update.title

    if update.completed is not None:
        task.completed = update.completed
    
    db.commit()
    db.refresh(task)
    
    return task

@router.put("/{task_id}", response_model = TaskResponse)
def replace_task(task_id: int, update: TaskReplace):
    db = SessionLocal()

    task = db.query(Task).filter(Task.id == task_id).first()
    
    if task is None:
        raise HTTPException(status_code=404, detail="Item not Found")
    
    task.title = update.title
    task.completed = update.completed

    db.commit()
    db.refresh(task)

    return task