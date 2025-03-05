# tasks.py
from fastapi import APIRouter, HTTPException
from configuration import collection_todo  # นำเข้าจาก config
from database.schemas import all_tasks
from database.models import Todo
from bson.objectid import ObjectId
from datetime import datetime
from typing import Optional

router = APIRouter(prefix="/tasks")

@router.get("/")
async def get_all_todos(search: Optional[str] = None):
    try:
        query = {}
        if search:  # ถ้ามีพารามิเตอร์ search ให้ค้นหาตาม title
            query["title"] = {"$regex": search, "$options": "i"}

        data = collection_todo.find(query)
        return {"status_code": 200, "data": all_tasks(data)}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Some error occurred: {e}")

@router.post("/")
async def create_task(new_task: Todo):
    try:
        resp = collection_todo.insert_one(dict(new_task))
        return {"status_code": 200, "id": str(resp.inserted_id)}
    except Exception as e: 
        raise HTTPException(status_code=500, detail=f"Some error occurred: {e}")

@router.put("/{task_id}")
async def update_task(task_id: str, updated_task: dict):
    try:
        id = ObjectId(task_id)
        existing_doc = collection_todo.find_one({"_id": id})
        
        if not existing_doc or existing_doc.get("is_deleted", False):
            raise HTTPException(status_code=404, detail="Task does not exist")

        updated_task["updated_at"] = datetime.timestamp(datetime.now())
        print(updated_task)

        resp = collection_todo.update_one({"_id": id}, {"$set": updated_task})

        if resp.modified_count == 0:
            raise HTTPException(status_code=400, detail="No changes were made")

        return {"status_code": 200, "message": "Task Updated Successfully"}

    except Exception as e: 
        raise HTTPException(status_code=500, detail=f"Some error occurred: {str(e)}")

@router.delete("/{task_id}")
async def delete_task(task_id: str):
    try:
        id = ObjectId(task_id)
        existing_doc = collection_todo.find_one({"_id": id})
        
        if not existing_doc or existing_doc.get("is_deleted", False):
            raise HTTPException(status_code=404, detail="Task does not exist")

        resp = collection_todo.delete_one({"_id": id})
        return {"status_code": 200, "message": "Task Deleted Successfully"}

    except Exception as e: 
        raise HTTPException(status_code=500, detail=f"Some error occurred: {str(e)}")
