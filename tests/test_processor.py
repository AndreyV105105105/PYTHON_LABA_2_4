import pytest
from src.processor import TaskProcessor
from src.models import Task


# Правильный источник для тестов
class ValidSource:
    def get_tasks(self):
        # Добавили новые обязательные параметры
        return [Task(task_id="крутой", description="Тест", priority=1, status="new", payload={})]


# Неправильный источник, не соответствующий контракту
class InvalidSource:
    def get_kal(self):
        return []


def test_register_valid_source():
    """Проверяет, что корректный источник успешно регистрируется"""
    processor = TaskProcessor()
    source = ValidSource()
    processor.register_source(source)
    assert len(processor._sources) == 1
    assert processor._sources[0] == source


def test_reject_invalid_source():
    """Проверяет, что процессор выбрасывает TypeError для некорректного источника"""
    processor = TaskProcessor()
    source = InvalidSource()
    with pytest.raises(TypeError, match="Invalid source"):
        processor.register_source(source)


def test_collect_tasks_from_multiple_sources():
    """Проверяет, что процессор корректно собирает задачи с нескольких источников"""
    processor = TaskProcessor()
    processor.register_source(ValidSource())
    processor.register_source(ValidSource())  # Регистрируем дважды

    tasks = processor.collect_tasks()
    assert len(tasks) == 2
    assert all(isinstance(t, Task) for t in tasks)


def test_collect_tasks_with_no_sources():
    """Проверяет, что сбор задач возвращает пустой список, если нет источников"""
    processor = TaskProcessor()
    tasks = processor.collect_tasks()
    assert tasks == []
