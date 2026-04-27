import pytest
from src.models import Task
from src.exceptions import TaskInvalidStatusError, TaskInvalidPriorityError


def test_task_creation_success():
    """Проверка успешного создания задачи с правильными данными"""
    task = Task(task_id="1", description="Тест", priority=4, status="new", payload={"key": "value"})
    assert task.priority == 4
    assert task.status == "new"


def test_task_invalid_priority():
    """Проверка, что неверный приоритет вызывает кастомную ошибку"""
    with pytest.raises(TaskInvalidPriorityError):
        # Пытаемся передать приоритет 1000
        Task(task_id="2", description="Тест", priority=1000, status="new", payload={})


def test_task_invalid_status():
    """Проверка, что неверный статус вызывает кастомную ошибку"""
    with pytest.raises(TaskInvalidStatusError):
        Task(task_id="3", description="Тест", priority=2, status="pornographic", payload={})


def test_task_is_ready_property():
    """Проверка вычисляемого свойства is_ready"""
    task = Task(task_id="4", description="Тест", priority=1, status="ready", payload={"data": 1})
    assert task.is_ready is True

    # Меняем статус и проверяем, что свойство пересчиталось
    task.status = "done"
    assert task.is_ready is False


def test_task_created_at_readonly():
    """Проверка, что created_at нельзя изменить (только для чтения)"""
    task = Task(task_id="15", description="Тест", priority=1, status="new", payload={})
    with pytest.raises(AttributeError):
        task.created_at = "новое время"