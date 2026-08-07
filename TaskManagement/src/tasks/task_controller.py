from sqlalchemy.orm import Session
from fastapi import HTTPException

from src.tasks.task_dtos import TaskSchema
from src.tasks.task_model import TaskModel

from src.users.user_model import UserModel

def create_task(body: TaskSchema, db: Session, user:UserModel):

    new_task = TaskModel(
        title = body.title,
        description = body.description,
        is_complete = body.is_complete,
        user_id = user.id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return { "status": True, "message": "Task created successfully!", "data": new_task }

def get_tasks(db:Session, user:UserModel):
    try:
        tasks = db.query(TaskModel).filter(TaskModel.user_id == user.id).all()
       
        return { "status": True, "message": "Tasks retrieved successfully!", "data": tasks }
    except:
       print("Error in getting all tasks")

def get_task_by_id(task_id: int, db:Session, user: UserModel):
    task = db.query(TaskModel).get(task_id)

    if not task:
        raise HTTPException(404, detail= "No task found for this ID")

    return { "status": True, "message": "Task retrieved successfully!", "data": task }

def update_task_by_id(body: TaskSchema, task_id: int, db: Session):
    task = db.query(TaskModel).get(task_id)    
    if not task:
        raise HTTPException(404, detail= "No task found for this ID")

    task.title = body.title
    task.description = body.description
    task.is_complete = body.is_complete

    db.add(task)
    db.commit()
    db.refresh(task)

    return { "status": True, "message": "Task updated successfully!", "data": task }

def delete_task_by_id(task_id: int, db: Session):
    task = db.query(TaskModel).get(task_id)    
    if not task:
        raise HTTPException(404, detail= "No task found for this ID")

    db.delete(task)
    db.commit()

    return { "status": True, "message": "Task updated successfully!"}

