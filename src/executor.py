import asyncio
from src.contract import TaskHandler
from src.loggins import logger
from src.models import Task


class TaskExecutor:
    def __init__(self, max_size=100):
        self.max_size = max_size
        self._queue = asyncio.Queue(maxsize=max_size)
        self.handlers = []

    def register_handler(self, handler):
        if isinstance(handler, TaskHandler):
            self.handlers.append(handler)
            logger.info(f"Обработчик '{type(handler).__name__}' успешно зарегистрирован.")
        else:
            logger.error(f"Объект '{type(handler).__name__}' НЕ соответствует контракту TaskHandler!")
            raise TypeError("Invalid handler")

    async def submit_task(self, task: Task):
        await self._queue.put(task)
        logger.info(f"Задача {task.id} добавлена в очередь.")

    async def run(self):
        """Пакетная обработка: работает, пока очередь не опустеет."""
        logger.info("Запуск обработки задач.")
        while not self._queue.empty():
            task = await self._queue.get()

            for handler in self.handlers:
                try:
                    await handler.handle(task)
                except Exception as e:
                    # Централизованная обработка ошибок
                    logger.error(f"Ошибка в {type(handler).__name__} при обработке {task.id}: {e}")

            # Сообщаем очереди, что задача полностью отработана
            self._queue.task_done()

        logger.info("Очередь пуста, обработка завершена.")