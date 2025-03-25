from fastapi import FastAPI, HTTPException
from typing import List
from datetime import datetime
from models import Task, tasks
from schemas import TaskCreate, TaskResponse

app = FastAPI()


@app.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate):
    """Create a new task"""
    new_task = Task(
        title=task.title,
        description=task.description,
        deadline=task.deadline
    )
    tasks[new_task.id] = new_task
    return new_task.dict()  # Используем метод dict()


@app.get("/tasks", response_model=List[TaskResponse])
def list_tasks():
    """List all tasks sorted by deadline (nearest first)"""
    task_list = [task.dict() for task in tasks.values()]  # Преобразуем в словари
    task_list.sort(key=lambda x: datetime.strptime(x["deadline"], "%d-%m-%Y"))
    return task_list


@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    """Delete a task by ID"""
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_id]
    return {"message": "Task deleted successfully"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
