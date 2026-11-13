from datetime import date
from core.models import Task, Priority, TaskList

def make_priority_filter(min_priority: Priority):
    def predicate(task: Task) -> bool:
        return task.priority.value >= min_priority.value
    return predicate

def make_tag_filter(tag: str):
    def predicate(task: Task) -> bool:
        return tag in task.tags
    return predicate

def make_overdue_filter(today: date):
    def predicate(task: Task) -> bool:
        return (not task.completed) and task.due_date is not None and task.due_date < today
    return predicate

def apply_filters(tasks: TaskList, *predicates) -> TaskList:
    return tuple(
        task for task in tasks
        if all(predicate(task) for predicate in predicates)
    )
