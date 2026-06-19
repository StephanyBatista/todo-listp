from repositories import task_repo
from routes.task_response import TaskResponse


def list_tasks():
    tasks = task_repo.get_all()
    return [TaskResponse.from_task(task) for task in tasks]
