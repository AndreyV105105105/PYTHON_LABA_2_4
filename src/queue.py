class TaskQueueIter:
    def __init__(self, data):
        self.data = data
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= len(self.data):
            raise StopIteration

        item = self.data[self.idx]
        self.idx += 1
        return item


class TaskQueue:
    def __init__(self):
        self._tasks = []

    def __iter__(self):
        return TaskQueueIter(self._tasks)

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
            return next(generator)
        except StopIteration:
            return None