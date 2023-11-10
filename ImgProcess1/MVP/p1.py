class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

class TaskList: #Model
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_tasks(self):
        return self.tasks

    def mark_as_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True #Setting the status of task as completed



class TaskView: #View
    def show_tasks(self, tasks): #When Choice 2 is given...
        print("Tasks:")
        for i, task in enumerate(tasks):
            status = "Done" if task.completed else "Not Done"
            print(f"{i + 1}. {task.description} - {status}")

    def show_message(self, message):
        print(message)



class TaskController: #Controller
    def __init__(self):
        self.task_list = TaskList() #Creating a Model 
        self.view = TaskView() #Creating a View

    def add_task(self, description): #When choice is 1
        task = Task(description) #Creating a new Task object with the given description
        self.task_list.add_task(task)

    def list_tasks(self): #When choice is 2
        tasks = self.task_list.get_tasks()
        self.view.show_tasks(tasks)

    def complete_task(self, task_index): #When choice is 3
        self.task_list.mark_as_completed(task_index)

    def run(self):
        while True:
            choice = input("Options: (1) Add Task, \n(2) List Tasks, \n(3) Complete Task, \n(q) Quit: \n")
            if choice == '1':
                description = input("Enter task description: ")
                self.add_task(description)
            elif choice == '2':
                self.list_tasks()
            elif choice == '3':
                task_index = int(input("Enter task index to mark as completed: ")) - 1
                self.complete_task(task_index)
            elif choice == 'q':
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    controller = TaskController()
    controller.run()
