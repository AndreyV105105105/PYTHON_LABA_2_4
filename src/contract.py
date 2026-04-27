from typing import Protocol, runtime_checkable
from src.models import Task

# по контракту должен возвращаться список тасков
@runtime_checkable
class TaskSource(Protocol):
    def get_tasks(self) -> list[Task]:
        ...