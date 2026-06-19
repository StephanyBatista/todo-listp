from exceptions import NotFoundError
from repositories import task_repo


def done_task(task_id: int):
    task = task_repo.get_by_id(task_id)

    if task is None:
        raise NotFoundError("Task not found")

    task.mark_done()
    task_repo.save(task)
