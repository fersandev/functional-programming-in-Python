from datetime import date
from core.models import Task, Priority
from core.queries import (
    pending_tasks,
    sort_by_priority,
    completion_rate,
    has_overdue_tasks,
    group_by_priority,
)

def _mixed_tasks():
    return (
        Task(1, "A", Priority.LOW, completed=True),
        Task(2, "B", Priority.HIGH, completed=False, due_date=date(2020, 1, 1)),
        Task(3, "C", Priority.MEDIUM, completed=False),
    )

def test_pending_tasks_excludes_completed():
    tasks = _mixed_tasks()
    result = pending_tasks(tasks)
    assert all(not t.completed for t in result)
    assert len(result) == 2

def test_sort_by_priority_orders_high_to_low():
    tasks = _mixed_tasks()
    result = sort_by_priority(tasks)
    assert [t.priority for t in result] == [Priority.HIGH, Priority.MEDIUM, Priority.LOW]

def test_completion_rate_on_mixed_tasks():
    tasks = _mixed_tasks()
    assert completion_rate(tasks) == 1 / 3

def test_completion_rate_on_empty_list_is_zero_not_a_crash():
    assert completion_rate(()) == 0.0

def test_has_overdue_tasks_detects_past_due_date():
    tasks = _mixed_tasks()
    assert has_overdue_tasks(tasks, today=date(2026, 1, 1)) is True

def test_has_overdue_tasks_is_false_when_all_future_or_completed():
    tasks = (Task(1, "A", Priority.LOW, completed=True, due_date=date(2000, 1, 1)),)
    assert has_overdue_tasks(tasks, today=date(2026, 1, 1)) is False

def test_group_by_priority_groups_correctly():
    tasks = _mixed_tasks()
    grouped = group_by_priority(tasks)
    assert len(grouped[Priority.HIGH]) == 1
    assert len(grouped[Priority.LOW]) == 1
    assert len(grouped[Priority.MEDIUM]) == 1
