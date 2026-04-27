## Лабораторная работа 4: Асинхронный исполнитель задач

### Реализованные концепции:
1. **Асинхронная модель управления**:
   - Использование `asyncio.Queue` для потокобезопасной передачи задач.
2. **Контракты обработчиков**:
   - Реализован `TaskHandler` с асинхронным методом `handle`.
3. **Замер времени и отслеживание сбоев**:
   - Создан асинхронный контекстный менеджер для замера времени сессии и перехвата критических сбоев.

### Пример использования:

```python
import asyncio
from src.models import Task
from src.executor import TaskExecutor
from src.handlers import ConsoleTaskHandler
from src.context_managers import ExecutorContextManager

async def main():
    # Инициализация с ограничением размера очереди
    executor = TaskExecutor(max_size=100)
    executor.register_handler(ConsoleTaskHandler())

    # Асинхронное добавление задач в очередь
    await executor.submit_task(Task("1", "выпить 0.5 честера", 5, "new", {}))
    await executor.submit_task(Task("2", "выпить ещё 0.5 честера", 2, "new", {}))

    # Запуск через контекстный менеджер
    async with ExecutorContextManager():
        await executor.run()

if __name__ == "__main__":
    asyncio.run(main())