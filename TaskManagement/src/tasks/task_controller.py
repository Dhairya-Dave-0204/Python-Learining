from sqlalchemy.orm import Session
from fastapi import HTTPException

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

def get_tasks(db:Session):
    try:
        tasks = db.query(TaskModel).all()
       
        return { "status": True, "message": "Tasks retrieved successfully!", "data": tasks }
    except:
       print("Error in getting all tasks")

def get_task_by_id(task_id: int, db:Session):
    task = db.query(TaskModel).get(task_id)

    if not task:
        raise HTTPException(404, detail= "No task found for this ID")

    return { "status": True, "message": "Task retrieved successfully!", "data": task }