import json

from src.loggins import logger


def create_test_json_file(filename: str):
    """Создает тестовый JSON-файл для демонстрации работы filesource."""
    # data навайбкодил
    data = [
        {"id": "json-file-task-1", "payload": {"source": "disk", "priority": "high"}},
        {"id": "json-file-task-2", "payload": {"source": "disk", "status": "pending"}}
    ]
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    logger.info(f"Создан тестовый файл '{filename}'")