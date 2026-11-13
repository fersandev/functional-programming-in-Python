from core.models import Task, Priority
from core.stats import expensive_summary

def test_expensive_summary_computes_correct_totals():
    tasks = (
        Task(1, "A", Priority.HIGH, completed=True),
        Task(2, "B", Priority.HIGH, completed=False),
        Task(3, "C", Priority.LOW, completed=False),
    )
    expensive_summary.cache_clear()
    summary = expensive_summary(tasks)

    assert summary["total"] == 3
    assert summary["completed"] == 1
    assert summary["pending"] == 2
    assert summary["by_priority"][Priority.HIGH] == 2

def test_expensive_summary_is_cached_on_repeated_calls_with_equal_input():
    tasks = (Task(1, "A", Priority.HIGH),)
    expensive_summary.cache_clear()

    expensive_summary(tasks)
    hits_before = expensive_summary.cache_info().hits

    expensive_summary(tasks)
    hits_after = expensive_summary.cache_info().hits

    assert hits_after == hits_before + 1

def test_expensive_summary_treats_different_tasklists_as_different_cache_keys():
    expensive_summary.cache_clear()

    expensive_summary((Task(1, "A", Priority.HIGH),))
    expensive_summary((Task(2, "B", Priority.LOW),))

    assert expensive_summary.cache_info().hits == 0
    assert expensive_summary.cache_info().misses == 2
