from core.models import Priority
from core.validation import create_task, Ok, Err

def test_create_task_with_valid_title_returns_ok():
    result = create_task(task_id=1, title="Buy milk", priority=Priority.LOW)
    assert isinstance(result, Ok)
    assert result.value.title == "Buy milk"

def test_create_task_with_empty_title_returns_err():
    result = create_task(task_id=1, title="   ", priority=Priority.LOW)
    assert isinstance(result, Err)
    assert "empty" in result.error

def test_create_task_strips_whitespace_from_title():
    result = create_task(task_id=1, title="  with spaces  ", priority=Priority.LOW)
    assert result.value.title == "with spaces"

def test_map_chains_only_on_ok():
    result = create_task(task_id=1, title="X", priority=Priority.LOW).map(lambda t: t.title.upper())
    assert result.value == "X"

def test_map_is_a_no_op_on_err():
    result = create_task(task_id=1, title="", priority=Priority.LOW).map(lambda t: t.title.upper())
    assert isinstance(result, Err)
