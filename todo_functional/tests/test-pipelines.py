from datetime import date
from core.models import Task, Priority
from core.pipelines import pipe, compose, urgent_pending_tasks, high_priority_tasks

def test_pipe_applies_functions_left_to_right():
    add_one = lambda x: x + 1
    double = lambda x: x * 2
    pipeline = pipe(add_one, double)
    assert pipeline(3) == 8

def test_compose_applies_functions_right_to_left():
    add_one = lambda x: x + 1
    double = lambda x: x * 2
    pipeline = compose(add_one, double)
    assert pipeline(3) == 7

def test_urgent_pending_tasks_filters_and_sorts():
    tasks = (
        Task(1, "Overdue low", Priority.LOW, due_date=date(2020, 1, 1)),
        Task(2, "Overdue high", Priority.HIGH, due_date=date(2020, 1, 1)),
        Task(3, "Future", Priority.HIGH, due_date=date(2030, 1, 1)),
        Task(4, "Done and overdue", Priority.HIGH, completed=True, due_date=date(2020, 1, 1)),
    )
    result = urgent_pending_tasks(tasks, today=date(2026, 1, 1))
    assert [t.id for t in result] == [2, 1]

def test_high_priority_tasks_partial_application():
    tasks = (
        Task(1, "A", Priority.HIGH),
        Task(2, "B", Priority.LOW),
    )
    result = tuple(high_priority_tasks(tasks))
    assert [t.id for t in result] == [1]
