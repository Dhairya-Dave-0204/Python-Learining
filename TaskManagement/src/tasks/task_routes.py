from fastapi import APIRouter, Depends

from src.tasks import task_controller
from src.tasks.task_dtos import TaskSchema
from src.utils.db import get_db

task_routes = APIRouter(prefix= "/tasks")
    
@task_routes.post("/create")
def create_task(body: TaskSchema, db = Depends(get_db)):
    return task_controller.create_task(body, db)

@task_routes.get("/all-tasks")
def get_tasks(db = Depends(get_db)):
    return task_controller.get_tasks(db)

@task_routes.get("/get/{task_id}")
def get_task_by_id(task_id: int, db = Depends(get_db)):
    return task_controller.get_task_by_id(task_id, db)