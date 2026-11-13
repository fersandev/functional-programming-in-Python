from typing import Protocol
from core.models import TaskList

class TaskRepository(Protocol):
    def load(self) -> TaskList:
        ...

    def save(self, tasks: TaskList) -> None:
        ...
