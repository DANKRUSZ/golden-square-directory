

def check_task_is_todo(text):
    if "#TODO" in text:
        return True
    return False