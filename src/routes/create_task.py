from typing import Annotated

from pydantic import BaseModel, StringConstraints


class CreateTaskResponse(BaseModel):
    title: Annotated[
        str, StringConstraints(strip_whitespace=True, min_length=5, max_length=10)
    ]


def create_task(body: CreateTaskResponse):
    return {"title": body.title}
