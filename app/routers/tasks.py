from fastapi import APIRouter, HTTPException, status
from typing import List
from app.models import Task
from app.database import db

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

@router.get("", response_model=List[Task])
def get_tasks():
    """获取所有任务列表"""
    return db

@router.get("/{task_id}", response_model=Task)
def get_task(task_id: int):
    """根据 ID 获取特定任务"""
    for task in db:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="未找到该任务")

@router.post("", response_model=Task, status_code=status.HTTP_201_CREATED)
# ... (rest of the file remains same, just replacing the HTTPException messages)
def create_task(task: Task):
    """创建新任务"""
    new_task = task.model_dump()
    new_task["id"] = len(db) + 1
    db.append(new_task)
    return new_task

@router.put("/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    """更新任务状态"""
    for index, task in enumerate(db):
        if task["id"] == task_id:
            data = updated_task.model_dump()
            data["id"] = task_id
            db[index] = data
            return db[index]
    raise HTTPException(status_code=404, detail="未找到该任务")

@router.delete("/{task_id}")
def delete_task(task_id: int):
    """删除任务"""
    for index, task in enumerate(db):
        if task["id"] == task_id:
            db.pop(index)
            return {"message": "任务删除成功"}
    raise HTTPException(status_code=404, detail="未找到该任务")
