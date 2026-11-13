from dataclasses import dataclass
from typing import Callable, Union
from core.models import Task, Priority

@dataclass(frozen=True)
class Ok:
    value: object

    def map(self, func: Callable) -> "Ok":
        return Ok(func(self.value))

    def unwrap_or(self, default):
        return self.value

@dataclass(frozen=True)
class Err:
    error: str

    def map(self, func: Callable) -> "Err":
        return self

    def unwrap_or(self, default):
        return default

Result = Union[Ok, Err]

def create_task(
    task_id: int,
    title: str,
    priority: Priority,
    due_date=None,
) -> Result:
    if not title or not title.strip():
        return Err("title cannot be empty")
    if len(title) > 200:
        return Err("title cannot exceed 200 characters")
    return Ok(Task(id=task_id, title=title.strip(), priority=priority, due_date=due_date))
