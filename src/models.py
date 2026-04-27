import datetime
from typing import Any

from src.descriptors.non_data_descriptor import NonDataDescriptor
from src.descriptors.priority_descriptor import PriorityDescriptor
from src.descriptors.status_descriptor import StatusDescriptor


class Task:

    priority = PriorityDescriptor()
    status = StatusDescriptor()
    nondata = NonDataDescriptor()

    def __init__(self, task_id: str, description: str, priority: int, status: str, payload: Any):
        self.id = task_id
        self.description = description
        self.priority = priority
        self.status = status
        self.payload = payload
        self._created_at = datetime.datetime.now()

    @property
    def is_ready(self) -> bool:
        """Проверяем, готова ли задача к выполнению"""
        if self.status == 'ready' and self.payload is not None:
            return True
        return False

    @property
    def created_at(self) -> datetime:
        return self._created_at

