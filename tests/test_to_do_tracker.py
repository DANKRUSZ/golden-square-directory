import pytest 
from lib.to_do_tracker import TaskTracker

# Test to check tasks are added to list

def test_add_task_to_list():
    tasktracker = TaskTracker()
    tasktracker.add("Tidy my room")
    result = tasktracker.return_task_list()
    assert result == ["Tidy my room"]

def test_add_multiple_tasks():
    tasktracker = TaskTracker()
    tasktracker.add("Tidy my room")
    tasktracker.add("Clean the kitchen")
    tasktracker.add("Take the bins out")
    tasktracker.add("Go to the gym")
    result = tasktracker.return_task_list()
    assert result == ["Tidy my room", "Clean the kitchen", 
    "Take the bins out", "Go to the gym"]

def test_tasks_removed():
    tasktracker = TaskTracker()
    tasktracker.add("Tidy my room")
    tasktracker.add("Clean the kitchen")
    result =tasktracker.remove_completed_tasks("Tidy my room")
    assert result == ["Clean the kitchen"]

def test_multiple_taks_removed():
    tasktracker = TaskTracker()
    tasktracker.add("Tidy my room")
    tasktracker.add("Clean the kitchen")
    tasktracker.add("Take the bins out")
    tasktracker.add("Go to the gym")
    result = tasktracker.remove_completed_tasks("Take the bins out")
    result = tasktracker.remove_completed_tasks("Go to the gym")
    assert result == ["Tidy my room", "Clean the kitchen"]

def test_task_not_in_list():
    #tasktracker = TaskTracker()
    #tasktracker.add("Tidy my room")
    #with pytest.raises(Exception) as e:
        #tasktracker.remove_completed_tasks("Clean the kitchen")
    #error_message = str(e.value)
    #assert error_message == "Task not in to do list"
    pass