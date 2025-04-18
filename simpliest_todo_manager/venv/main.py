import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

tasks = []


class taskModel(BaseModel):
    title: str = Field(min_length=3)
    description: str
    isCompleted: bool = Field(default=False)


@app.get("/tasks")
def get_tasks():
    return tasks


@app.patch("/tasks/{task_id}")
def get_tasks(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            task["isCompleted"] = True
            return {"success": True, "message": "задание обновленно"}
    raise HTTPException(status_code=404, detail="задание не найдено")


@app.post("/tasks")
def post_task(new_task: taskModel):
    tasks.append(
        {
            "id": len(tasks) + 1,
            "title": new_task.title,
            "description": new_task.description,
            "isCompleted": False,
        }
    )
    return {"success": True, "message": "задание добавлено"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
