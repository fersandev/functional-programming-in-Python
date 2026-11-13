import json
from core.models import Task, Priority
from core.export import export_task, JSONFormat, CSVFormat, MarkdownFormat

def _task():
    return Task(1, "Buy bread", Priority.HIGH, completed=False, tags=("home",))

def test_export_json_produces_valid_json_with_expected_fields():
    result = export_task(JSONFormat(), _task())
    data = json.loads(result)
    assert data["title"] == "Buy bread"
    assert data["priority"] == "HIGH"
    assert data["completed"] is False

def test_export_csv_produces_comma_separated_row():
    result = export_task(CSVFormat(), _task())
    assert result == "1,Buy bread,HIGH,False,,home"

def test_export_markdown_produces_checkbox_line():
    result = export_task(MarkdownFormat(), _task())
    assert result == "- [ ] **Buy bread** (HIGH)"

def test_export_markdown_marks_completed_tasks():
    done = Task(1, "Done", Priority.LOW, completed=True)
    result = export_task(MarkdownFormat(), done)
    assert result == "- [x] **Done** (LOW)"
