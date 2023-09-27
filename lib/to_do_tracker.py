

class TaskTracker():

    def __init__(self):
        self.todo_list = []
        pass

    def add(self, task):
        # Parameters: string - task
        #adding a task to a to do list
        self.todo_list.append(task)

    def return_task_list(self):
        #return my to do list of tasks added in def add
        return self.todo_list
        

    def remove_completed_tasks(self, task):
        #Parameters: task - a task I have completed
        #remove tasks I have completed from my to do list
        # Raise an exception if the task entered is not in list
        for item in self.todo_list:
            if item == task:
                self.todo_list.remove(task)
            else:
                raise Exception("Task not in to do list")
        return self.todo_list
    



