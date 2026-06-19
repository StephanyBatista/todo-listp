from models.task import Task


class TaskRepository:
    def __init__(self):
        self._tasks = []
        self._next_id = 1

    def get_all(self) -> list[Task]:
        return self._tasks

    def get_by_id(self, task_id: int) -> Task | None:
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def save(self, task: Task) -> Task:
        if task.id is None:
            task.id = self._next_id
            self._next_id += 1
            self._tasks.append(task)
        return task

    def delete(self, task_id: int):
        self._tasks = [task for task in self._tasks if task.id != task_id]
