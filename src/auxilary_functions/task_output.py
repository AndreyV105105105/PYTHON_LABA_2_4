
def task_output(tasks):
    """Выводит итоговый список задач."""
    print("ИТОГОВЫЙ СПИСОК ПОЛУЧЕННЫХ ЗАДАЧ")
    if tasks:
        for task in tasks:
            print(f"ID: {task.id:<20} Payload: {task.payload}")
    else:
        print("Задачи не найдены.")