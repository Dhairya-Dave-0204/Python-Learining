from sqlalchemy.orm import Session

from src.tasks.task_dtos import TaskSchema
from src.tasks.task_model import TaskModel

def create_task(body: TaskSchema, db: Session):

    new_task = TaskModel(
        title = body.title,
        description = body.description,
        is_complete = body.is_complete
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return { "status": True, "message": "Task created successfully!", "data": new_task }