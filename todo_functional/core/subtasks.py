from core.models import Task, TaskList

def count_all_tasks(task: Task) -> int:
    if not task.subtasks:
        return 1
    return 1 + sum(count_all_tasks(sub) for sub in task.subtasks)

def all_completed(task: Task) -> bool:
    return task.completed and all(all_completed(sub) for sub in task.subtasks)

def flatten_tasks(task: Task) -> TaskList:
    result = (task,)
    for sub in task.subtasks:
        result = result + flatten_tasks(sub)
    return result

def flatten_task_list(tasks: TaskList) -> TaskList:
    result: TaskList = ()
    for task in tasks:
        result = result + flatten_tasks(task)
    return result
