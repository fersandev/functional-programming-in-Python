from datetime import date
from core.models import Task, Priority
from core.operations import add_task, complete_task
from core.queries import pending_tasks, sort_by_priority, completion_rate, has_overdue_tasks
from core.validation import create_task, Ok, Err
from core.filters import make_priority_filter, apply_filters
from core.pipelines import urgent_pending_tasks
from core.subtasks import count_all_tasks, all_completed, flatten_task_list
from core.export import export_all, MarkdownFormat
from core.recurring import next_occurrences
from core.stats import expensive_summary
from shell.ports import TaskRepository
from shell.json_repository import JsonFileRepository

def run(repo: TaskRepository) -> None:
    tasks = repo.load()

    result = create_task(task_id=len(tasks) + 1, title="Finish the book", priority=Priority.HIGH)
    match result:
        case Ok(new_task):
            tasks = add_task(tasks, new_task)
        case Err(error):
            print(f"Could not create task: {error}")

    print("Pending:", len(pending_tasks(tasks)))
    print("% completed:", completion_rate(tasks) * 100)
    print("Any overdue?:", has_overdue_tasks(tasks, today=date.today()))

    high_priority = make_priority_filter(Priority.HIGH)
    print("High priority:", len(apply_filters(tasks, high_priority)))
    print("Urgent pending:", urgent_pending_tasks(tasks, today=date.today()))

    for task in tasks:
        if task.subtasks:
            print(f"{task.title}: {count_all_tasks(task)} tasks total, "
                  f"complete={all_completed(task)}")

    print(export_all(MarkdownFormat(), flatten_task_list(tasks)))

    print("Next 3 weekly review dates:",
          next_occurrences(start=date.today(), interval_days=7, count=3))
    print(expensive_summary(tasks))

    repo.save(tasks)

def main() -> None:
    repo: TaskRepository = JsonFileRepository("tasks.json")
    run(repo)

if __name__ == "__main__":
    main()
