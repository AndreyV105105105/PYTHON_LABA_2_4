import asyncio
import os

from src.auxilary_functions.create_json import create_test_json_file
from src.loggins import setup_logging, logger
from src.processor import TaskProcessor
from src.sources.api_source import ApiSource
from src.sources.generator_source import GeneratorSource
from src.sources.file_source import FileSource

from src.executor import TaskExecutor
from src.handlers import ConsoleTaskHandler
from src.context_managers import ExecutorContextManager


async def async_main():
    """Асинхронная точка входа в программу"""
    setup_logging()

    json_filename = "tasks.json"
    create_test_json_file(json_filename)

    processor = TaskProcessor()
    sources = [
        ApiSource(),
        GeneratorSource(count=3),
        FileSource(file_path=json_filename)
    ]

    for s in sources:
        try:
            processor.register_source(s)
        except TypeError as e:
            logger.error(f"Не удалось зарегистрировать источник: {e}")

    all_tasks = processor.collect_tasks()

    executor = TaskExecutor(max_size=100)

    # Регистрируем обработчика
    executor.register_handler(ConsoleTaskHandler())

    # Загружаем задачи в асинхронную очередь
    for task in all_tasks:
        await executor.submit_task(task)

    # Запуск обработки внутри контекстного менеджера
    async with ExecutorContextManager():
        await executor.run()

    os.remove(json_filename)


def main():
    """Синхронная обертка для запуска Event Loop"""
    asyncio.run(async_main())


if __name__ == "__main__":
    main()