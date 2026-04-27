import json
from typing import List

from src.loggins import logger
from ..models import Task


class FileSource:
    """Читает задачи из json-файла."""
    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_tasks(self) -> List[Task]:
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                # 1. Получаем данные в формате json
                raw_data = json.load(f)

            # 2. Превращаем словари в объекты Task
            tasks = []
            for item in raw_data:
                # Создаем экземпляр Task для каждой записи в json
                task_obj = Task(
                    task_id=item["id"],
                    description=item.get("description", "Нет описания"),
                    priority=item.get("priority", 1),
                    status=item.get("status", "new"),
                    payload=item.get("payload", {})
                )
                tasks.append(task_obj)

            logger.info(f"Успешно загружено {len(tasks)} задач из файла {self.file_path}")
            return tasks

        except FileNotFoundError:
            logger.error(f"Файл {self.file_path} не найден!")
            return []
        except (json.JSONDecodeError, KeyError) as e:
            logger.error(f"Ошибка в структуре JSON или данных: {e}")
            return []
