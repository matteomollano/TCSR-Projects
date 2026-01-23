import sqlite3

conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()

# CREATE TABLE Tasks -> create a table called Tasks
create_tasks_table = """
CREATE TABLE IF NOT EXISTS Tasks (
    task_id INTEGER PRIMARY KEY,
    task VARCHAR(64)
)
"""
cursor.execute(create_tasks_table)

def add_task(task):
    query = "INSERT INTO Tasks (task) VALUES (?)"
    cursor.execute(query, (task, ))
    
def display_tasks():
    query = "SELECT * FROM Tasks"
    cursor.execute(query)
    results = cursor.fetchall()
    print("To do list:")
    for row in results:
        id = row[0]
        task = row[1]
        print(f"{id}. {task}")
        
def remove_task(task_id):
    query = "DELETE FROM Tasks WHERE task_id = (?)"
    cursor.execute(query, (task_id, ))
    
def get_id_list():
    query = "SELECT task_id FROM Tasks"
    cursor.execute(query)
    result = cursor.fetchall()
    ids_list = []
    for row in result:
        ids_list.append(str(row[0]))
    return ids_list
  
print('Welcome to your to do list!')
while True:  
    # get the number of tasks already in the to do list
    cursor.execute("SELECT count(*) FROM Tasks")
    count = cursor.fetchone()[0]

    # no tasks in the to do list
    if count == 0:
        print("Your to do list is empty. Let's add some tasks")
        new_task = input('Enter a new task: ')
        add_task(new_task)
    else:
        choice = input('Enter 1 to add task or 2 to remove task: ')
        while choice not in ['1', '2']:
            choice = input('Enter 1 or 2 only: ')
       
        # add task
        if choice == '1':
            new_task = input('Enter a new task: ')
            add_task(new_task)
        
        # remove task
        else:
            # ensure the id is valid
            id = input('Enter id to remove: ')
            ids = get_id_list()
            while id not in ids:
                id = input(f"Not a valid id. You must enter an id that is in {ids}: ")    
            id = int(id)
        
            # remove the task
            remove_task(id)
    
    display_tasks()
    print()