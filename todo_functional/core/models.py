from dataclasses import dataclass
from enum import Enum
from datetime import date

class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

@dataclass(frozen=True)
class Task:
    id: int
    title: str
    priority: Priority
    completed: bool = False
    due_date: date | None = None
    tags: tuple[str, ...] = ()
    subtasks: tuple["Task", ...] = ()

TaskList = tuple[Task, ...]
