def remove_task(tasks: tuple, task_id: int) -> tuple:
    return tuple(t for t in tasks if t.id != task_id)

def test_remove_task_removes_only_the_indicated_task():
    tasks = (
        Task(1, "A", Priority.LOW, completed=False),
        Task(2, "B", Priority.LOW, completed=False),
        Task(3, "C", Priority.HIGH, completed=False),
    )
    result = remove_task(tasks, task_id=2)

    assert len(result) == 2
    assert all(t.id != 2 for t in result)              # task 2 is gone
    assert result[0].id == 1 and result[1].id == 3      # the rest remain, in order
    assert len(tasks) == 3                               # and CRITICAL: the original tuple is still intact

test_remove_task_removes_only_the_indicated_task()
print("Test passed")
