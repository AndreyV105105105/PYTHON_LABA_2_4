import os

from src.auxilary_functions.create_json import create_test_json_file
from src.auxilary_functions.task_output import task_output
from src.loggins import setup_logging, logger
from src.processor import TaskProcessor
from src.sources.api_source import ApiSource
from src.sources.generator_source import GeneratorSource
from src.sources.file_source import FileSource




def main():
    """Основная функция, демонстрирующая работу системы."""

    setup_logging()

    # создание json файла
    json_filename = "tasks.json"
    create_test_json_file(json_filename)

    # инициализация процессора
    processor = TaskProcessor()

    # Инициализация источников
    sources = [
        ApiSource(),
        GeneratorSource(count=2),
        FileSource(file_path=json_filename)
    ]

    # Регистрация с проверкой контракта
    for s in sources:
        try:
            processor.register_source(s)
        except TypeError as e:
            logger.error(f"Не удалось зарегистрировать источник: {e}")

    # Сбор и вывод задач
    all_tasks = processor.collect_tasks()
    task_output(all_tasks)

    # удаление демонстрационного json файла
    os.remove(json_filename)


if __name__ == "__main__":
    main()
