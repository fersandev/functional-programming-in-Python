from datetime import date
from functools import reduce
from core.models import Task, TaskList, Priority

def pending_tasks(tasks: TaskList) -> TaskList:
    return tuple(filter(lambda t: not t.completed, tasks))

def sort_by_priority(tasks: TaskList) -> TaskList:
    return tuple(sorted(tasks, key=lambda t: t.priority.value, reverse=True))

def completion_rate(tasks: TaskList) -> float:
    if not tasks:
        return 0.0
    completed_count = reduce(
        lambda acc, task: acc + (1 if task.completed else 0),
        tasks,
        0,
    )
    return completed_count / len(tasks)

def has_overdue_tasks(tasks: TaskList, today: date) -> bool:
    return any(
        (not t.completed) and (t.due_date is not None) and (t.due_date < today)
        for t in tasks
    )

def group_by_priority(tasks: TaskList) -> dict[Priority, TaskList]:
    def step(acc: dict, task: Task) -> dict:
        acc.setdefault(task.priority, []).append(task)
        return acc

    grouped = reduce(step, tasks, {})
    return {priority: tuple(items) for priority, items in grouped.items()}
