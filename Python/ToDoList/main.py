
to_do_list = {}

while True:
    
    # for i in range(len(to_do_list)):
    #     print(to_do_list)
    
    length = len(to_do_list)
    
    if length == 0:
        print("To do list is empty!")
        choice = 1
    else:
        print("\nTo Do List:")
        for id, task in to_do_list.items():
            print(str(id) + ".", task)
        choice = input("What would you like to do?\n1) Add a task\n2) Remove a task\nSelection: ")
        choice = int(choice)
    
    if choice == 1:
        task = input("Enter a task: ")
        # length = len(to_do_list)
        to_do_list[length+1] = task
    elif choice == 2:
        ids = list(to_do_list.keys())
        print('Possible ids to remove', ids)
        id = int(input("Enter task id to remove: "))
        
        while id not in ids:
            id = int(input("Invalid task id. Re-enter: "))
        task = to_do_list.pop(id)
        print(task, 'was successfully removed')