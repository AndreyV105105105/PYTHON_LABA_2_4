from typing import List
from src.contract import TaskSource
from src.loggins import logger
from src.models import Task

class TaskProcessor:
    """
    Класс, который регистрирует источники и собирает с них задачи.
    Выполняет runtime-проверку соответствия контракту.
    """
    def __init__(self):
        self._sources: List[TaskSource] = []

    def register_source(self, source):
        if isinstance(source, TaskSource):
            self._sources.append(source)
            logger.info(f"Источник '{type(source).__name__}' успешно зарегистрирован.")
        else:
            logger.error(f"Объект '{type(source).__name__}' НЕ соответствует контракту TaskSource!")
            raise TypeError(f"Invalid source")

    def collect_tasks(self) -> List[Task]:
        logger.info("Начат сбор задач со всех зарегистрированных источников")
        all_tasks = []
        for src in self._sources:
            all_tasks.extend(src.get_tasks())
        logger.info(f"Сбор завершен. Всего получено задач: {len(all_tasks)}")
        return all_tasks
