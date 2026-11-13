from functools import singledispatch
from core.models import Task

class ExportFormat:
    pass

class JSONFormat(ExportFormat):
    pass

class CSVFormat(ExportFormat):
    pass

class MarkdownFormat(ExportFormat):
    pass

@singledispatch
def export_task(fmt: ExportFormat, task: Task) -> str:
    raise NotImplementedError(f"no exporter registered for {type(fmt).__name__}")

@export_task.register
def _(fmt: JSONFormat, task: Task) -> str:
    import json
    return json.dumps({
        "id": task.id,
        "title": task.title,
        "priority": task.priority.name,
        "completed": task.completed,
        "due_date": task.due_date.isoformat() if task.due_date else None,
        "tags": list(task.tags),
    })

@export_task.register
def _(fmt: CSVFormat, task: Task) -> str:
    due = task.due_date.isoformat() if task.due_date else ""
    tags = "|".join(task.tags)
    return f"{task.id},{task.title},{task.priority.name},{task.completed},{due},{tags}"

@export_task.register
def _(fmt: MarkdownFormat, task: Task) -> str:
    checkbox = "x" if task.completed else " "
    return f"- [{checkbox}] **{task.title}** ({task.priority.name})"

def export_all(fmt: ExportFormat, tasks) -> str:
    return "\n".join(export_task(fmt, task) for task in tasks)
