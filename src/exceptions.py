
class TaskError(Exception):
    """Базовое исключение для всех ошибок, связанных с задачами"""
    pass

class TaskValidationError(TaskError):
    """Ошибка валидации данных задачи"""
    pass

class TaskInvalidStatusError(TaskValidationError):
    """Передача недопустимого статуса"""
    pass

class TaskInvalidPriorityError(TaskValidationError):
    """Приоритет выходит за заданные границы"""
    pass