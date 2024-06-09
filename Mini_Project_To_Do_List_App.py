# Project Requirements

# User Interface (UI):
# Create a command-line interface (CLI) for the To-Do List Application.
# Display a welcoming message and a menu with the following options:
        # Welcome to the To-Do List App!

        # Menu:
        # 1. Add a task
        # 2. View tasks
        # 3. Mark a task as complete
        # 4. Delete a task
        # 5. Quit


# To-Do List Features:
# Implement the following features for the To-Do List:
# Adding a task.
# Viewing the list of tasks 
# Marking a task as complete. (Bonus) (Hint: Use string manipulation to add "X" to the end of a task)
# Deleting a task.
# Quitting the application.



import os

def clear ():
    os.system('cls' if os.name == 'nt' else 'clear')

task_list = {}

def new_id(): #Function to return new ID for a new task
    last_id = max(task_list.keys()) if task_list else 0
    return last_id + 1

def new_task():
    new_task_id = new_id()
    while True:
        task = input ("Please enter a new task: \n")
        print (f"Task: {task}")
        correct = input ("Does this information look correct? (y/n) \n")
        if correct.lower() == 'y':
            #Create task
            task_list[new_task_id] = {'Task': task, 'Status': 'Incomplete'}
            break
        else:
            clear ()
            continue

def view_task_list():
    if not task_list:
        print("No tasks available to view.")
    else:
        print("To-Do List: \n")
        for task_id, task_info in task_list.items():
            print (f'Item: {task_id}')
            print (f'Task: {task_info['Task']}')
            print (f'Status: {task_info['Status']}')
            print("-" * 20)

    input ("Press Enter to return to the main menu...")


def mark_task ():
    if not task_list:
        print("No tasks available to mark as completed.")
        input("Press Enter to return to the main menu...")
        return

    print ("Which task would you like to mark as completed? \n")
    for task_id, task_info in task_list.items():
            print (f'Item: {task_id}')
            print (f'Task: {task_info['Task']}')
            print (f'Status: {task_info['Status']}')
            print("-" * 20)
    while True:
        try:
            task_id = int(input("Please enter the Item number to update status to completed: \n"))
            if task_id in task_list:
                task_list[task_id]['Status'] = 'Completed'
                print (f'Item: {task_id} {task_info['Task']} has been updated to completed.')
                task_list[task_id]['Task'] += " X"
                input("Press Enter to return to the main menu...")
                break
            else:
                print("Invalid item. Please enter a correct item number.")
        except ValueError:
            print("Invalid input. Please enter a numeric item number.")

def delete_task ():
    if not task_list:
        print("No tasks available to delete.")
        input("Press Enter to return to the main menu...")
        return

    print ("Which task would you like to remove from the list? \n")
    for task_id, task_info in task_list.items():
            print (f'Item: {task_id}')
            print (f'Task: {task_info['Task']}')
            print (f'Status: {task_info['Status']}')
            print("-" * 20)

    while True:
        try:
            task_id = int(input ("Enter the item number you'd like to remove from the list. \n"))
            if task_id in task_list:
                removed_task = task_list.pop(task_id)
                print (f"{removed_task['Task']} has been removed from the list.")
                input("Press Enter to return to the main menu...")
                break
            else:
                print(f"{task_id} is not in the list. Please enter a valid item number.")
        except ValueError:
            print("Invalid input. Please enter a numeric item number.")



def main ():
    while True:
        ans = input ('''
        Welcome to the To-Do List App!

        Menu:
        1. Add a task
        2. View tasks
        3. Mark a task as complete
        4. Delete a task
        5. Quit

        Please enter your selection (1-5): ''')
        if ans == '1':
            clear()
            new_task() # Function to add a new task
        elif ans == '2':
            clear()
            view_task_list() # Function to view tasks
        elif ans == '3':
            clear()
            mark_task() # Function to mark task as complete
        elif ans == '4':
            clear()
            delete_task() # Function to delete a task
        elif ans == '5':
            print("Thanks for using our To-Do List App!")
            break
        else:
            print('Please enter a valid number.')

main()
