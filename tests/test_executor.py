import pytest
from src.models import Task
from src.executor import TaskExecutor
from src.context_managers import ExecutorContextManager


class DummySuccessHandler:
    """Запоминает все задачи, которые ему передали."""
    def __init__(self):
        self.handled_tasks = []

    async def handle(self, task: Task) -> None:
        self.handled_tasks.append(task)

class DummyFailingHandler:
    """Всегда падает с ошибкой."""
    async def handle(self, task: Task) -> None:
        raise ValueError("Сымитированная ошибка базы данных!")


@pytest.mark.asyncio
async def test_executor_processes_tasks():
    """Проверка, что исполнитель корректно передает задачи обработчикам"""
    executor = TaskExecutor()
    handler = DummySuccessHandler()
    executor.register_handler(handler)

    task = Task(task_id="async-1", description="Тест", priority=1, status="new", payload={})
    await executor.submit_task(task)

    await executor.run()

    assert len(handler.handled_tasks) == 1
    assert handler.handled_tasks[0].id == "async-1"

@pytest.mark.asyncio
async def test_executor_handles_errors_gracefully():
    """Проверка централизованной обработки ошибок"""
    executor = TaskExecutor()
    fail_handler = DummyFailingHandler()
    success_handler = DummySuccessHandler()

    # Регистрируем оба
    executor.register_handler(fail_handler)
    executor.register_handler(success_handler)

    task = Task(task_id="async-2", description="Тест на не падение", priority=1, status="new", payload={})
    await executor.submit_task(task)

    await executor.run()

    # Проверяем, что несмотря на падение первого обработчика, второй успешно отработал
    assert len(success_handler.handled_tasks) == 1
    assert success_handler.handled_tasks[0].id == "async-2"

@pytest.mark.asyncio
async def test_context_manager_executes_without_errors():
    """Проверка асинхронного контекстного менеджера."""
    async with ExecutorContextManager() as manager:
        assert manager is not None