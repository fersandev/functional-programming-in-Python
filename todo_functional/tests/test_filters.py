from datetime import date
from core.models import Task, Priority
from core.filters import make_priority_filter, make_tag_filter, make_overdue_filter, apply_filters

def test_make_priority_filter_keeps_equal_or_higher():
    predicate = make_priority_filter(Priority.MEDIUM)
    assert predicate(Task(1, "A", Priority.HIGH)) is True
    assert predicate(Task(2, "B", Priority.MEDIUM)) is True
    assert predicate(Task(3, "C", Priority.LOW)) is False

def test_two_closures_from_same_factory_are_independent():
    high_filter = make_priority_filter(Priority.HIGH)
    low_filter = make_priority_filter(Priority.LOW)

    task = Task(1, "A", Priority.MEDIUM)
    assert high_filter(task) is False
    assert low_filter(task) is True

def test_make_tag_filter():
    predicate = make_tag_filter("urgent")
    assert predicate(Task(1, "A", Priority.LOW, tags=("urgent", "home"))) is True
    assert predicate(Task(2, "B", Priority.LOW, tags=("home",))) is False

def test_make_overdue_filter_fixes_today_inside_the_closure():
    predicate = make_overdue_filter(today=date(2026, 6, 1))
    overdue_task = Task(1, "A", Priority.LOW, due_date=date(2020, 1, 1))
    future_task = Task(2, "B", Priority.LOW, due_date=date(2030, 1, 1))
    assert predicate(overdue_task) is True
    assert predicate(future_task) is False

def test_apply_filters_combines_predicates_with_and():
    tasks = (
        Task(1, "A", Priority.HIGH, tags=("home",)),
        Task(2, "B", Priority.HIGH, tags=("work",)),
        Task(3, "C", Priority.LOW, tags=("work",)),
    )
    result = apply_filters(tasks, make_priority_filter(Priority.HIGH), make_tag_filter("work"))
    assert [t.id for t in result] == [2]
