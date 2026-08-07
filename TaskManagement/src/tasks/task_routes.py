from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.tasks import task_controller
from src.tasks.task_dtos import TaskSchema
from src.utils.db import get_db
from src.utils.helpers import is_authenticated
from src.users.user_model import UserModel


task_routes = APIRouter(prefix= "/tasks")
    
@task_routes.post("/create", status_code=status.HTTP_201_CREATED)
def create_task(body: TaskSchema, db:Session = Depends(get_db), user: UserModel = Depends(is_authenticated)):
    return task_controller.create_task(body, db, user)

@task_routes.get("/all-tasks", status_code=status.HTTP_200_OK)
def get_tasks(db:Session = Depends(get_db), user: UserModel = Depends(is_authenticated)):
    return task_controller.get_tasks(db)

@task_routes.get("/get/{task_id}", status_code=status.HTTP_200_OK)
def get_task_by_id(task_id: int, db:Session = Depends(get_db), user: UserModel = Depends(is_authenticated)):
    return task_controller.get_task_by_id(task_id, db)

@task_routes.put("/update/{task_id}", status_code=status.HTTP_201_CREATED)
def update_task_by_id(body: TaskSchema, task_id: int,  db:Session = Depends(get_db), user: UserModel = Depends(is_authenticated)):
    return task_controller.update_task_by_id(body, task_id, db)

@task_routes.delete("/delete/{task_id}", status_code=status.HTTP_200_OK)
def delete_task_by_id(task_id: int,  db:Session = Depends(get_db), user: UserModel = Depends(is_authenticated)):
    return task_controller.delete_task_by_id(task_id, db)
