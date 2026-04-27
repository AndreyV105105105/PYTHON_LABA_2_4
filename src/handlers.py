import asyncio
from src.models import Task
from src.loggins import logger


class ConsoleTaskHandler:
    """Реализация обработчика, выводящая информацию в консоль"""

    async def handle(self, task: Task) -> None:
        logger.info(f"Начало обработки задачи {task.id} (статус: {task.status})")

        # Имитация асинхронной неблокирующей операции
        await asyncio.sleep(0.5)

        logger.info(f"Задача {task.id} успешно выполнена. Данные: {task.payload}")