class TaskResponse:
    def __init__(self, id: int, title: str, done: bool):
        self.id = id
        self.title = title
        self.done = done

    @classmethod
    def from_task(cls, task):
        return cls(id=task.id, title=task.title, done=task.done)
