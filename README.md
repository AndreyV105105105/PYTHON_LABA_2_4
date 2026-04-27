## Лабораторная работа 3

### Реализованные концепции:
1. **Протокол итерации**: 
   - Очередь полностью совместима со стандартными конструкциями Python.
   - Поддерживается безопасный повторный обход коллекции.
2. **Ленивые вычисления**:
   - Реализована потоковая фильтрация с использованием `yield`.
   - Методы-фильтры не создают промежуточных списков в памяти.
3. **Безопасное извлечение**:
   - Реализован метод `get_first_by_status` с ручным продвижением итератора через функцию `next()` и перехватом исключения `StopIteration`.

### Пример использования ленивой очереди:

```python
from src.queue import TaskQueue
from src.models import Task

queue = TaskQueue()
queue.add_task(Task(task_id="1", description="reverver vreverve", priority=5, status="ready", payload={}))
queue.add_task(Task(task_id="2", description="erve APvevevI", priority=3, status="new", payload={}))

# Ленивая фильтрация
ready_tasks = queue.filter_by_status("ready")
for task in ready_tasks:
    print(task.description)

# Безопасное получение первой подходящей задачи
urgent_task = queue.get_first_by_status("critical")
if urgent_task is None:
    print("None critical")
```

### Запуск тестов коллекции
```bash
python -m pytest tests/test_queue.py -v
```