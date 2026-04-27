import time
from src.loggins import logger


class ExecutorContextManager:
    """Асинхронный контекстный менеджер для замера времени и управления ресурсами"""

    async def __aenter__(self):
        self.start_time = time.time()
        logger.info("Старт асинхронной сессии обработки задач")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        elapsed_time = time.time() - self.start_time
        logger.info(f"Сессия завершена. Затрачено времени: {elapsed_time:.2f} сек")

        if exc_type:
            logger.error(f"Сессия прервана критической ошибкой: {exc_val}")

        # Возвращаем False, чтобы не глушить фатальные исключения
        return False