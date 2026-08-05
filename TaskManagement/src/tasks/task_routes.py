from fastapi import APIRouter

from src.tasks import task_controller 

task_routes = APIRouter(prefix= "/tasks")

@task_routes.post("/create")
def create_task():
    return task_controller.create_task()