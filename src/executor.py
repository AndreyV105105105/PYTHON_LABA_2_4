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

    async def _worker(self, worker_id: int):
        """Воркер, который бесконечно тянет задачи из очереди и обрабатывает их."""
        while True:
            task = await self._queue.get()
            for handler in self.handlers:
                try:
                    await handler.handle(task)
                except Exception as e:
                    logger.error(f"Воркер {worker_id}: Ошибка в {type(handler).__name__} при обработке {task.id}: {e}")

            self._queue.task_done()

    async def run(self, num_workers: int = 3):
        """Пакетная обработка: запускает пул воркеров и ждёт опустошения очереди."""
        logger.info(f"Запуск {num_workers} асинхронных воркеров.")

        workers = [asyncio.create_task(self._worker(i)) for i in range(num_workers)]

        await self._queue.join()

        for w in workers:
            w.cancel()

        logger.info("Очередь пуста, обработка завершена.")