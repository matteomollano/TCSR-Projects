to_do_list = {}

{1: 'do my hw', 2:'feed my dog', 3:'eat lunch', 4:'clean up the house'}

while True:
    # adding  
    task = input("Enter a task: ")
    id = len(to_do_list) + 1
    to_do_list[id] = task
    print(to_do_list)
    
    # remove
    task_id = int(input('Enter task id to remove: '))
    ids = to_do_list.keys()
    while task_id not in ids:
        task_id = int(input("Invalid task id. Re-enter: "))
    task = to_do_list.pop(task_id)
    print("Task", task, "removed successfully")
    print(to_do_list)