# ===== Importing external modules ===========
from datetime import datetime
import os

# ==== Functions ====
"""
Function to detemine if the task number is valid
"""
def get_valid_task_number(user_tasks):
    try:
        choice = int(input("Enter task number or -1 to return: "))
        if choice == -1:
            return -1
        elif 1 <= choice <= len(user_tasks):
            return choice
        else:
            print("Invalid task number.")
            return get_valid_task_number(user_tasks)
    except ValueError:
        print("Invalid input. Enter a number.")
        return get_valid_task_number(user_tasks)


"""
Function to register a user if the user does not already exist
"""
def reg_user():
    # Test if user already exists
    while True:
        new_username = input("Enter the new username here: \n")
        if new_username in user_info:
            print("This username already exists. Try again.")
        else:
            break

    # If user doesn't exist test the confirmation password and add them to user.txt 
    new_password = input("Enter the new password here: \n")
    con_password = input("Password confirmation: \n")
    if new_password == con_password:
        admin = input("Are you an admin? (yes/no): ").strip().lower() == "yes"
        with open("user.txt", "a") as file:
            file.write(f"{new_username}, {new_password}, {admin}\n")
        user_info[new_username] = new_password
        if admin:
            admin_users.add(new_username)
        print("User registered successfully.")
    else:
        print("Passwords do not match.")


"""
Function to add a new task for a user
"""
def add_task():
     # Get the information about the new task
    username = input("Enter username for assigned task: ")
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    while True:
        due_date = input("Enter due date (e.g. 25 Oct 2025): ")
        try:
            datetime.strptime(due_date, '%d %b %Y')
            break
        except ValueError:
            print("Invalid date format. Please use '25 Oct 2025'.")
    
    assigned_date = datetime.today().strftime('%d %b %Y')
    completed = "No"

    # Write the new task to tasks.txt
    with open("tasks.txt", "a") as file:
        file.write(f"{username}, {title}, {description}, {assigned_date}, {due_date}, {completed}\n")
    print("Task added successfully.")


"""
Function to view all tasks
"""
def view_all():
    print("\n--------------------------------------VIEW ALL TASKS---------------------------------------------\n")
    with open("tasks.txt", "r") as file:
        for task in file:
            parts = task.strip().split(", ")
            # Test for malformed lines
            if len(parts) != 6:
                print(f"Skipping malformed line: {task.strip()}")
                continue
            # Split each task into items
            username, title, description, assigned, due, complete = parts
            # Display each task in a readable format
            print(f"Task: {title}\nAssigned to: {username}\nDate assigned: {assigned}\nDue date: {due}\nTask complete? {complete}\nTask description:\n{description}\n" + "-" * 40)
    print("\n---------------------------------------------END-------------------------------------------------\n")


"""
Function to view tasks assigned to the current user and allow editing/completing
"""
def view_mine(current_user):
    print("\n--------------------------------------VIEW MY TASKS---------------------------------------------\n")
    # Read all tasks from file
    with open("tasks.txt", 'r') as file:
        tasks = file.readlines()

    # Collect tasks assigned to current user using a normal for loop
    user_tasks = []
    for task in tasks:
        # Test for malformed lines
        parts = task.strip().split(', ')
        if len(parts) != 6:
            print(f"Skipping malformed line: {task.strip()}")
            continue

        if task.startswith(current_user):
            user_tasks.append(task)

    # Display tasks with corresponding number
    for index, task in enumerate(user_tasks, start=1):
        parts = task.strip().split(', ')
        if len(parts) != 6:
            print(f"Skipping malformed line: {task.strip()}")
            continue
        username, title, description, assigned, due, complete = parts
        print(f"\nTask {index}:\nTask: {title}\nAssigned to: {username}\nDate assigned: {assigned}\nDue date: {due}\nTask complete? {complete}\nTask description:\n{description}\n" + "-" * 40)
    print("\n---------------------------------------------END-------------------------------------------------\n")

    index = get_valid_task_number(user_tasks)
    if index == -1:
        return

    try:
        # Test if task is already completed
        task_line = user_tasks[index - 1]
        if ", Yes" in task_line:
            print("Task already completed. Cannot edit.")
            return

        action = input("Do you want to mark the task as complete (c) or edit the task (e): ").lower()
        all_index = tasks.index(task_line)
       
        # Mark the task as completed
        if action == 'c':
            tasks[all_index] = task_line.replace("No", "Yes")
        # Edit the task    
        elif action == 'e':
            new_user = input("Enter the new username: ")
            new_due = input("Enter the new due date: ")
            parts = task_line.strip().split(', ')
            parts[0] = new_user
            parts[4] = new_due
            tasks[all_index] = ', '.join(parts) + '\n'

        with open("tasks.txt", 'w') as file:
            file.writelines(tasks)
        print("Task updated.")

    except (ValueError, IndexError):
        print("Invalid selection.")


"""
Function to display all completed tasks
"""
def view_completed():
    print("\n-----------------------------------VIEW COMPLETED TASKS------------------------------------------\n")
    with open("tasks.txt", "r") as file:
        for task in file:
            parts = task.strip().split(", ")
            # Test for malformed lines
            if len(parts) != 6:
                continue
             # Test if the task is completed and display the task if true
            if parts[-1].lower() == "yes":
                username, title, description, assigned, due, complete = parts
                print(f"Task: {title}\nAssigned to: {username}\nDate assigned: {assigned}\nDue date: {due}\nTask complete? {complete}\nTask description:\n{description}\n" + "-" * 40)
    print("\n---------------------------------------------END-------------------------------------------------\n")


"""
Function to delete a task by number
"""
def delete_task():
    with open("tasks.txt", 'r') as file:
        tasks = file.readlines()

    # Create a task number for each task 
    for i, task in enumerate(tasks):
        print(f"{i + 1}: {task.strip()}")

    try:
        # Using the task number delete a specific task
        num = int(input("Enter task number you want to delete: ")) - 1
        del tasks[num]
        # Overwrite task.txt 
        with open("tasks.txt", 'w') as f:
            f.writelines(tasks)
        print("Task deleted.")

    except ValueError:
        print("Invalid selection.")
    except IndexError:
        print("Invalid selection.") 


"""
Function to generate reports and save them to files
"""
def generate_reports():
    # Open 'tasks.txt' and read all task entries into a list
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    
    # Total number of tasks
    total = len(tasks)
    # Count how many tasks are completed
    completed = 0
    for task in tasks:
        if task.strip().endswith("Yes"):
            completed += 1
    
    # Calculate the number of incomplete tasks
    incomplete = total - completed
    overdue = 0
    today = datetime.today()
    
    # Check for overdue tasks
    for task in tasks:
        parts = task.strip().split(', ')
        if len(parts) != 6:
            continue
        complete = parts[-1]
        due_date = parts[-2]
        due_date_obj = datetime.strptime(due_date, '%d %b %Y')
        if complete == "No" and due_date_obj < today:
            overdue += 1

    with open("task_overview.txt", "w") as file:
        file.write(f"Total tasks: {total}\nCompleted: {completed}\nIncomplete: {incomplete}\nOverdue: {overdue}\n")
        file.write(f"% Incomplete: {incomplete/total*100:.2f}%\n% Overdue: {overdue/total*100:.2f}%\n")

    # Create a dictionary to store tasks per user
    user_tasks = {}
    for user in user_info:
        user_tasks[user] = []

    # Assign tasks to their respective users    
    for task in tasks:
        username = task.split(', ')[0]
        if username in user_tasks:
            user_tasks[username].append(task)

    # Write task statistics to 'user_overview.txt'
    with open("user_overview.txt", 'w') as f:
        f.write(f"Total users: {len(user_info)}\nTotal tasks: {total}\n")
        for user, uts in user_tasks.items():
            total_user_tasks = len(uts)
            if total_user_tasks == 0:
                continue
            
            user_completed = 0
            for t in uts:
                if t.strip().endswith("Yes"):
                    user_completed += 1
           
            user_overdue = 0
            for t in uts:
                parts = t.strip().split(', ')
                if len(parts) == 6 and parts[-1] == "No":
                    due_date = datetime.strptime(parts[4], '%d %b %Y')
                    if due_date < today:
                        user_overdue += 1
            
            f.write(f"\nUser: {user}\nTasks assigned: {total_user_tasks}\n% of total tasks: {total_user_tasks/total*100:.2f}%\n")
            f.write(f"% completed: {user_completed/total_user_tasks*100:.2f}%\n% incomplete: {(total_user_tasks-user_completed)/total_user_tasks*100:.2f}%\n")
            f.write(f"% overdue: {user_overdue/total_user_tasks*100:.2f}%\n")


"""
Function to display statistics from report files
"""
def display_statistics():
    # Check if 'tasks_overview.txt' or 'user_overview.txt' do not exist
    # If either is missing, call generate_reports() to create the reports
    if not os.path.exists("task_overview.txt") or not os.path.exists("user_overview.txt"):
        generate_reports()
    
    # Display the contents of the task overview report 
    print("\n--- Task Overview ---")
    with open("task_overview.txt", 'r') as f:
        print(f.read())

    # Display the contents of the user overview report
    print("\n--- User Overview ---")
    with open("user_overview.txt", 'r') as f:
        print(f.read())


# ==== Login Section ====
# Read usernames and passwords from user.txt
user_info = {}
admin_users = set()

with open("user.txt", "r") as file:
    for line in file:
        parts = line.strip().split(", ")
        if len(parts) == 3:
            username, password, admin = parts
            user_info[username] = password
            if admin.lower() == "true":
                admin_users.add(username)
        elif len(parts) == 2:
            username, password = parts 
            user_info[username] = password               

# Use a while loop to validate login
print("=== Login System ===")
while True:
    username_input = input("Enter username: ")
    password_input = input("Enter password: ")

    if username_input in user_info and user_info[username_input] == password_input:
        current_user = username_input
        print(f"Login successful! Welcome, {current_user}.\n")
        break
    else:
        print("Invalid credentials. Please try again.\n")

while True:
    # Present the admin menu to the user if the user is admin and
    # make sure that the user input is converted to lower case.
    if current_user in admin_users:
        menu = input('''\nSelect one of the following options:
    r - register a user
    a - add task
    va - view all tasks
    vm - view my tasks
    vc - view completed tasks
    del - delete tasks
    ds - display statistics
    gr - generate reports
    e - exit
: ''').lower()
    # Present the non-admin menu if user is not admin
    else:
        menu = input('''\nSelect one of the following options:
    a - add task
    va - view all tasks
    vm - view my tasks
    e - exit
: ''').lower()

    if menu == 'r':
        reg_user()
    elif menu == 'a':
        add_task()
    elif menu == 'va':
        view_all()
    elif menu == 'vm':
        view_mine(current_user)
    elif menu == 'vc':
        view_completed()
    elif menu == 'del':
        delete_task()
    elif menu == 'ds':
        display_statistics()
    elif menu == 'gr':
        generate_reports()
    elif menu == 'e':
        print('Goodbye!!!')
        break
    else:
        print("You have entered an invalid input. Please try again")
