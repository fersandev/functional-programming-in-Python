from core.models import Task, Priority
from core.subtasks import count_all_tasks, all_completed, flatten_tasks, flatten_task_list

def _tree():
    return Task(
        1, "Project", Priority.HIGH, completed=False,
        subtasks=(
            Task(2, "Design", Priority.MEDIUM, completed=True),
            Task(
                3, "Implementation", Priority.HIGH, completed=False,
                subtasks=(
                    Task(4, "Backend", Priority.HIGH, completed=True),
                    Task(5, "Frontend", Priority.HIGH, completed=False),
                ),
            ),
        ),
    )

def test_count_all_tasks_base_case_no_subtasks():
    leaf = Task(1, "Solo", Priority.LOW)
    assert count_all_tasks(leaf) == 1

def test_count_all_tasks_counts_every_node_in_the_tree():
    assert count_all_tasks(_tree()) == 5

def test_all_completed_is_false_if_any_descendant_is_pending():
    assert all_completed(_tree()) is False

def test_all_completed_is_true_when_entire_tree_is_done():
    fully_done = Task(
        1, "Root", Priority.LOW, completed=True,
        subtasks=(Task(2, "Child", Priority.LOW, completed=True),),
    )
    assert all_completed(fully_done) is True

def test_flatten_tasks_preserves_all_nodes_in_depth_order():
    flat = flatten_tasks(_tree())
    assert [t.id for t in flat] == [1, 2, 3, 4, 5]

def test_flatten_task_list_flattens_multiple_top_level_trees():
    tasks = (_tree(), Task(6, "Standalone", Priority.LOW))
    flat = flatten_task_list(tasks)
    assert [t.id for t in flat] == [1, 2, 3, 4, 5, 6]
