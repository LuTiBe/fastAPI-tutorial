from fastapi import FastAPI
from models import Task  # Importiere das Task-Modell

app = FastAPI()

tasks = []  # Leere Liste für Aufgaben

@app.post("/tasks/")
def create_task(title: str):
    task = Task(title=title, completed=False)  # Verwende das Task-Modell
    tasks.append(task.dict())
    return task

@app.get("/tasks/")
def get_tasks():
    return tasks
