from fastapi import APIRouter

from src.tasks import task_controller
from src.tasks.task_dtos import TaskSchema

task_routes = APIRouter(prefix= "/tasks")

@task_routes.post("/create")
def create_task(body: TaskSchema):
    return task_controller.create_task(body)