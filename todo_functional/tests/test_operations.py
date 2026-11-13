from core.models import Task, Priority
from core.operations import add_task, complete_task, remove_task, update_task

def _sample_tasks():
    return (
        Task(1, "Study", Priority.HIGH),
        Task(2, "Exercise", Priority.MEDIUM),
        Task(3, "Read", Priority.LOW),
    )

def test_add_task_appends_without_mutating_original():
    tasks = _sample_tasks()
    new_task = Task(4, "New", Priority.LOW)

    result = add_task(tasks, new_task)

    assert result == tasks + (new_task,)
    assert len(tasks) == 3

def test_complete_task_marks_only_the_matching_task():
    tasks = _sample_tasks()
    result = complete_task(tasks, task_id=2)

    assert result[0].completed is False
    assert result[1].completed is True
    assert result[2].completed is False
    assert tasks[1].completed is False

def test_complete_task_with_unknown_id_changes_nothing():
    tasks = _sample_tasks()
    result = complete_task(tasks, task_id=999)

    assert result == tasks

def test_remove_task_excludes_matching_id():
    tasks = _sample_tasks()
    result = remove_task(tasks, task_id=1)

    assert len(result) == 2
    assert all(task.id != 1 for task in result)
    assert len(tasks) == 3

def test_update_task_applies_arbitrary_field_changes():
    tasks = _sample_tasks()
    result = update_task(tasks, task_id=3, title="Read a long book", priority=Priority.HIGH)

    updated = next(t for t in result if t.id == 3)
    assert updated.title == "Read a long book"
    assert updated.priority == Priority.HIGH
    assert tasks[2].title == "Read"
