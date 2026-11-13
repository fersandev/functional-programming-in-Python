from core.models import Task, Priority
from shell.json_repository import JsonFileRepository

def test_save_then_load_roundtrip_preserves_data(tmp_path):
    filepath = tmp_path / "tasks.json"
    repo = JsonFileRepository(str(filepath))

    tasks = (
        Task(1, "Buy bread", Priority.MEDIUM, tags=("home",)),
        Task(
            2, "Project", Priority.HIGH, completed=False,
            subtasks=(Task(3, "Subtask", Priority.LOW, completed=True),),
        ),
    )

    repo.save(tasks)
    loaded = repo.load()

    assert loaded == tasks

def test_load_on_missing_file_returns_empty_tuple(tmp_path):
    filepath = tmp_path / "not_exist.json"
    repo = JsonFileRepository(str(filepath))

    assert repo.load() == ()
