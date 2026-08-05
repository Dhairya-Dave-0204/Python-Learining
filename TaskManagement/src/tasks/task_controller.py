from src.tasks.task_dtos import TaskSchema

def create_task(body: TaskSchema):
    return { "status": True, "message": "Task created successfully!", "data": body }