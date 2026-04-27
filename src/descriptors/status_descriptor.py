from src.exceptions import TaskInvalidStatusError, TaskValidationError
from src.loggins import logger

class StatusDescriptor:
    def __init__(self):
        # Список разрешенных статусов
        self.allowed_statuses = ['new', 'ready', 'done']

    def __set_name__(self, owner, name):
        self.private_name = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.private_name, None)

    def __set__(self, instance, value):
        if not isinstance(value, str):
            logger.error(f"Попытка установить нестроковый статус: {value}")
            raise TaskValidationError("Статус должен быть строкой")

        if value not in self.allowed_statuses:
            logger.warning(f"Статус {value} не в допустимом списке статусов")
            raise TaskInvalidStatusError("Недопустимый статус")

        setattr(instance, self.private_name, value)

