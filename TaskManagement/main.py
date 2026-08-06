from fastapi import FastAPI

from src.utils.db import Base, engine
from src.tasks.task_routes import task_routes
from src.users.user_routes import user_router

Base.metadata.create_all(engine)

app = FastAPI(
    title = "Task Management App"
)

app.include_router(task_routes)
app.include_router(user_router)