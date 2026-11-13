from functools import lru_cache
from core.models import TaskList, Priority

@lru_cache(maxsize=64)
def expensive_summary(tasks: TaskList) -> dict:
    total = len(tasks)
    completed = sum(1 for t in tasks if t.completed)
    by_priority = {
        p: sum(1 for t in tasks if t.priority == p)
        for p in Priority
    }
    return {
        "total": total,
        "completed": completed,
        "pending": total - completed,
        "by_priority": by_priority,
    }
