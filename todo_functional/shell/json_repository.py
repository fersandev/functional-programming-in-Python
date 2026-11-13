import json
from datetime import date
from pathlib import Path
from core.models import Task, TaskList, Priority
from shell.decorators import logged, timed

def _task_to_dict(task: Task) -> dict:
    return {
        "id": task.id,
        "title": task.title,
        "priority": task.priority.name,
        "completed": task.completed,
        "due_date": task.due_date.isoformat() if task.due_date else None,
        "tags": list(task.tags),
        "subtasks": [_task_to_dict(sub) for sub in task.subtasks],
    }

def _dict_to_task(data: dict) -> Task:
    return Task(
        id=data["id"],
        title=data["title"],
        priority=Priority[data["priority"]],
        completed=data["completed"],
        due_date=date.fromisoformat(data["due_date"]) if data["due_date"] else None,
        tags=tuple(data.get("tags", ())),
        subtasks=tuple(_dict_to_task(sub) for sub in data.get("subtasks", ())),
    )

class JsonFileRepository:
    def __init__(self, filepath: str):
        self.filepath = Path(filepath)

    @logged
    @timed
    def load(self) -> TaskList:
        if not self.filepath.exists():
            return ()
        with open(self.filepath, "r", encoding="utf-8") as f:
            raw = json.load(f)
        return tuple(_dict_to_task(item) for item in raw)

    @logged
    @timed
    def save(self, tasks: TaskList) -> None:
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump([_task_to_dict(t) for t in tasks], f, indent=2, ensure_ascii=False)
