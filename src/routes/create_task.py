from typing import Annotated

from pydantic import BaseModel, StringConstraints

from models.task import Task
from repositories import task_repo
from routes.task_response import TaskResponse


class CreateTaskRequest(BaseModel):
    title: Annotated[
        str, StringConstraints(strip_whitespace=True, min_length=5, max_length=128)
    ]


def create_task(body: CreateTaskRequest):
    task = Task(title=body.title)
    saved = task_repo.save(task)
    return TaskResponse.from_task(saved)
