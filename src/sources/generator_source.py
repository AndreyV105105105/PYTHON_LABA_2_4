from typing import List

from src.loggins import logger
from src.models import Task



class GeneratorSource:
    """Генерирует задачи циклом."""
    def __init__(self, count: int = 3):
        self._count = count

    def get_tasks(self) -> List[Task]:
        logger.info(f"Генерация {self._count} задач")
        return [Task(task_id=f"gen-{i + 1}", description=f"Сгенерированная задача {i+1}", priority=1, status="new", payload={"step": i + 1}) for i in range(self._count)]
