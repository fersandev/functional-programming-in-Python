from functools import partial
from core.models import TaskList, Priority
from core.filters import make_priority_filter, make_overdue_filter
from core.queries import sort_by_priority, pending_tasks

def pipe(*funcs):
    def piped(x):
        result = x
        for f in funcs:
            result = f(result)
        return result
    return piped

def compose(*funcs):
    def composed(x):
        result = x
        for f in reversed(funcs):
            result = f(result)
        return result
    return composed

def urgent_pending_tasks(tasks: TaskList, today) -> TaskList:
    overdue = make_overdue_filter(today)
    process = pipe(
        pending_tasks,
        lambda ts: tuple(filter(overdue, ts)),
        sort_by_priority,
    )
    return process(tasks)


is_high_priority = make_priority_filter(Priority.HIGH)
high_priority_tasks = partial(filter, is_high_priority)
