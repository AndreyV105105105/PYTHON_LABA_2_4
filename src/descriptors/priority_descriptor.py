import logging
from src.exceptions import TaskInvalidPriorityError, TaskValidationError

logger = logging.getLogger(__name__)

class PriorityDescriptor:
    def __init__(self, min_priority: int = 1, max_priority: int = 10):
        self.min_priority = min_priority
        self.max_priority = max_priority

    def __set_name__(self, owner, name):
        self.private_name = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.private_name, None)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            logger.error(f"Попытка установить нечисловой приоритет: {value}")
            raise TaskValidationError("Приоритет должен быть целым неотрицательным числом")

        if not (self.min_priority <= value <= self.max_priority):
            logger.warning(f"Приоритет {value} вне допустимого диапазона ({self.min_priority}-{self.max_priority})")
            raise TaskInvalidPriorityError(f'Приоритет должен существовать в границах от {self.min_priority} до {self.max_priority}')

        setattr(instance, self.private_name, value)