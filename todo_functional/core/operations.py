from dataclasses import replace
from core.models import Task, TaskList

def add_task(tasks: TaskList, new_task: Task) -> TaskList:
    return tasks + (new_task,)

def complete_task(tasks: TaskList, task_id: int) -> TaskList:
    return tuple(
        replace(task, completed=True) if task.id == task_id else task
        for task in tasks
    )

def remove_task(tasks: TaskList, task_id: int) -> TaskList:
    return tuple(task for task in tasks if task.id != task_id)

def update_task(tasks: TaskList, task_id: int, **changes) -> TaskList:
    return tuple(
        replace(task, **changes) if task.id == task_id else task
        for task in tasks
    )
