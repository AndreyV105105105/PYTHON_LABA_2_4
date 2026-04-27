from typing import List

from src.loggins import logger
from src.models import Task



class ApiSource:
    """Имитирует получение задач из внешнего API."""
    def get_tasks(self) -> List[Task]:
        logger.info("Запрос к API-заглушке")
        # Имитация успешного ответа
        return [
            Task(task_id="api-task-300", description="Пост", priority=3, status="new", payload={"user_id": 105}),
            Task(task_id="api-task-105", description="Лайк", priority=2, status="new", payload={"user_id": 300})
        ]
