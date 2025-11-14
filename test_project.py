import pytest
from project import TodoList

@pytest.fixture
def empty_todo_list():
    """Provides an empty TodoList instance for testing."""
    return TodoList()

@pytest.fixture
def populated_todo_list():
    """Provides a TodoList instance with some tasks for testing."""
    todo = TodoList()
    todo.add_task("Buy groceries")
    todo.add_task("Walk the dog")
    return todo

def test_add_task(empty_todo_list):
    empty_todo_list.add_task("Learn Python")
    assert len(empty_todo_list.get_tasks()) == 1
    assert empty_todo_list.get_tasks()[0] == {"task": "Learn Python", "completed": False}

def test_add_task_invalid_input(empty_todo_list):
    with pytest.raises(ValueError):
        empty_todo_list.add_task("")
    with pytest.raises(ValueError):
        empty_todo_list.add_task(123)  # Invalid type

def test_complete_task(populated_todo_list):
    populated_todo_list.complete_task(0)
    assert populated_todo_list.get_tasks()[0]["completed"] is True
    assert populated_todo_list.get_tasks()[1]["completed"] is False

def test_complete_task_invalid_index(populated_todo_list):
    with pytest.raises(IndexError):
        populated_todo_list.complete_task(-1)
    with pytest.raises(IndexError):
        populated_todo_list.complete_task(len(populated_todo_list.get_tasks()))

def test_delete_task(populated_todo_list):
    populated_todo_list.delete_task(0)
    assert len(populated_todo_list.get_tasks()) == 1
    assert populated_todo_list.get_tasks()[0]["task"] == "Walk the dog"

def test_delete_task_invalid_index(populated_todo_list):
    with pytest.raises(IndexError):
        populated_todo_list.delete_task(-1)
    with pytest.raises(IndexError):
        populated_todo_list.delete_task(len(populated_todo_list.get_tasks()))

def test_get_tasks(empty_todo_list, populated_todo_list):
    assert empty_todo_list.get_tasks() == []
    expected_tasks = [
        {"task": "Buy groceries", "completed": False},
        {"task": "Walk the dog", "completed": False}
    ]
    assert populated_todo_list.get_tasks() == expected_tasks
