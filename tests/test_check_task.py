from lib.check_task import check_task_is_todo


def test_task_is_todo():
    result = check_task_is_todo("#TODO: Clean my room")
    assert result == True

def test_task_hoover_is_todo():
    result = check_task_is_todo("#TODO, hoover my kitchen")
    assert result == True


def test_take_wash_clothes_is_todo():
    result = check_task_is_todo("Washing clothes in on my #TODO list.")
    assert result == True

def test_washing_clothes_is_false():
    result = check_task_is_todo("Washing clothes in on my #todo list")
    assert result == False

def test_hoovering_is_false():
    result = check_task_is_todo("I need to hoover my bathroom")
    assert result == False

def test_task_is_false():
    result = check_task_is_todo("TODO: Tidy the study#")
    assert result == False

def test_text_is_empty():
    result = check_task_is_todo("")
    assert result == False