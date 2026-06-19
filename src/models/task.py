class Task:
    def __init__(self, title: str, done: bool = False):
        self.id: int | None = None
        self.title: str = title
        self.done: bool = done

    def mark_done(self):
        self.done = True
