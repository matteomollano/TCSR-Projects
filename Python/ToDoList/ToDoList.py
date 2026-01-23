class ToDoList:
    
    # Constructor
    def __init__(self):
        self.tasks = []
    
    # Input: a user's task
    # Function will add this task to the tasks list
    def add(self, task):
        self.tasks.append(task)
    
    # Input: the id for a task (index in the list)
    # Function will remove the corresponding task from the tasks lists
    # tasks = ["do my homework", "brush my teeth", "play soccer"]
    def remove(self, task_id):
        self.tasks.pop(task_id - 1)
        
    def display(self):
        length = len(self.tasks)
        if length == 0:
            print("Your to do list is empty.")
        else:
            for task_id in range(length):
                print(f"{task_id + 1}. {self.tasks[task_id]}")
                # print(str(task_id) + ". " + self.tasks[task_id]) # winston
                       
# Object
mylist = ToDoList()

print("Welcome to your to do list!")
print("Choose between the following options:")
print("1. Add a task")
print("2. Remove a task")
print("3. Display the to do list")
while True:
    choice = input("Your choice: ").strip()
    if choice == "1":
        task = input("Enter a task: ")
        mylist.add(task)
    elif choice == "2":
        task_id = int(input("Enter the id for the task you want to remove: "))
        mylist.remove(task_id)
    elif choice == "3":
        mylist.display()
    else:
        print("Invalid choice. Enter 1, 2, or 3 only.")
    print()