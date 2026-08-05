from fastapi import FastAPI

from src.utils.db import Base, engine
from src.tasks.task_routes import task_routes

Base.metadata.create_all(engine)

app = FastAPI(
    title = "Task Management App"
)

app.include_router(task_routes)