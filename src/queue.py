class TaskQueue:
    def __init__(self):
        self._tasks = []

    def __iter__(self):
        for task in self._tasks:
            yield task

    def add_task(self, task):
        self._tasks.append(task)

    def filter_by_status(self, status: str):
        for task in self:
            if task.status == status:
                yield task

    def filter_by_priority(self, priority: int):
        for task in self:
            if task.priority == priority:
                yield task

    def get_first_by_status(self, status: str):
        generator = self.filter_by_status(status)
        try:
            item = next(generator)
            return item
        except StopIteration:
            return None