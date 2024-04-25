import pytest
import sqlite3
from datetime import datetime
from task_model import TaskModel
from task import Task


# Fixture for the database connection and cursor
@pytest.fixture
def database_connection():
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        NAME TEXT NOT NULL,
        description TEXT ,
        Due_Date TEXT ,
        priority TEXT ,
        status TEXT ,
        List_Name TEXT
        )""")
    conn.commit()
    yield conn, cur
    conn.close()


# Fixture for a sample task object
def task_model():
    return TaskModel

# Fixture for a sample task object
@pytest.fixture
def sample_task():
    return Task(
        name="Test Task",
        description="This is a test task",
        due_date="2023-12-31",
        priority=True,
        status=True,
        list_name="Test List"
    )


# Constants for expected values
UPDATED_NAME = "Updated Task"
UPDATED_DESCRIPTION = "This is an updated task"
UPDATED_DUE_DATE = "2024-01-01"
UPDATED_PRIORITY = "Medium"
UPDATED_STATUS = "In progress"
UPDATED_LIST_NAME = "Updated List"


# Test the __init__ method of the Task class
def test_init(sample_task):
    assert sample_task.name == "Test Task"
    assert sample_task.description == "This is a test task"
    assert sample_task.due_date == "2023-12-31"
    assert sample_task.priority == True
    assert sample_task.list_name == "Test List"


# Test the add_task method of the Task class
def test_add_task(task_model, sample_task):
    # Now you should be able to call add_task
    task_model.add_task(sample_task)

    # Perform assertions
    task_id = sample_task.id
    result = task_model.conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()

    assert result is not None
    assert result[0] == task_id
    assert result[1] == sample_task.name
    assert result[2] == sample_task.description
    assert result[3] == sample_task.due_date
    assert result[4] == sample_task.priority
    assert result[5] == sample_task.status
    assert result[6] == sample_task.list_name
# Test the delete_task method of the Task class
def test_delete_task(database_connection, sample_task):
    conn, cur = database_connection
    sample_task.add_task()
    sample_task_id = sample_task.id
    Task.delete_task(sample_task_id)
    # ... (similar assertions as in your original test)


# Test the query method of the Task class
def test_query(database_connection, sample_task):
    conn, cur = database_connection
    sample_task.add_task()
    tasks = Task.query(filter="name = 'Test Task'", order="id DESC")
    assert len(tasks) == 1
    assert tasks[0].name == sample_task.name
    # ... (similar assertions for other attributes)


# Test the update method of the Task class
def test_update(database_connection, sample_task):
    conn, cur = database_connection
    sample_task.add_task()

    # Test updating the task name
    sample_task.name = UPDATED_NAME
    sample_task.update(sample_task.id)
    # ... (similar assertions for other attributes)

    # Test updating other attributes
    # ... (similar assertions for other attributes)
