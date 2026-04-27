import pytest
from src.queue import TaskQueue
from src.models import Task


def test_queue_iteration():
    queue = TaskQueue()
    task1 = Task(task_id="1", description="Тест", priority=4, status="new", payload={"key": "value"})
    task2 = Task(task_id="2", description="Тест2", priority=2, status="done", payload={"key": "value"})

    queue.add_task(task1)
    queue.add_task(task2)

    assert list(queue) == [task1, task2]
    assert list(queue) == [task1, task2]


def test_queue_filter_by_status():
    queue = TaskQueue()
    task1 = Task(task_id="1", description="Тест", priority=4, status="new", payload={"key": "value"})
    task2 = Task(task_id="2", description="Тест2", priority=2, status="done", payload={"key": "value"})

    queue.add_task(task1)
    queue.add_task(task2)

    filtered_queue = queue.filter_by_status('new')

    assert list(filtered_queue) == [task1]

def test_get_first_by_status_found():
    queue = TaskQueue()
    task1 = Task(task_id="1", description="Тест", priority=4, status="new", payload={"key": "value"})
    task2 = Task(task_id="2", description="Тест2", priority=2, status="done", payload={"key": "value"})

    queue.add_task(task1)
    queue.add_task(task2)

    first_item = queue.get_first_by_status('done')
    assert first_item == task2

def test_get_first_by_status_not_found():
    queue = TaskQueue()
    task1 = Task(task_id="1", description="Тест", priority=4, status="new", payload={"key": "value"})
    task2 = Task(task_id="2", description="Тест2", priority=2, status="done", payload={"key": "value"})

    queue.add_task(task1)
    queue.add_task(task2)

    first_item = queue.get_first_by_status('vvndvndwcvnowdvnw')
    assert first_item is None
