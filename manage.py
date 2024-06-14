import pandas as pd
import random

# Initialize an empty task list
tasks = pd.DataFrame(columns=['description', 'priority'])

# Load tasks from a CSV file
def load_tasks():
    global tasks
    try:
        tasks = pd.read_csv('tasks.csv')
    except FileNotFoundError:
        tasks = pd.DataFrame(columns=['description', 'priority'])

# Save tasks to a CSV file
def save_tasks():
    tasks.to_csv('tasks.csv', index=False)

# Load tasks initially
load_tasks()

# Function to add a task to the list
def add_task(description, priority):
    global tasks  # Declare tasks as a global variable
    new_task = pd.DataFrame({'description': [description], 'priority': [priority]})
    tasks = pd.concat([tasks, new_task], ignore_index=True)
    save_tasks()

# Function to remove a task by description
def remove_task(description):
    global tasks  # Declare tasks as a global variable
    if description in tasks['description'].values:
        tasks = tasks[tasks['description'] != description].reset_index(drop=True)
        save_tasks()
        print("Task removed successfully.")
    else:
        print("No task available.")

# Function to list all tasks
def list_tasks():
    if tasks.empty:
        print("No tasks available.")
    else:
        print(tasks)

# Function to recommend a task
def recommend_task():
    if not tasks.empty:
        # Get high-priority tasks
        high_priority_tasks = tasks[tasks['priority'] == 'High']
        
        if not high_priority_tasks.empty:
            # Choose a random high-priority task
            random_task = random.choice(high_priority_tasks['description'].tolist())
            print(f"Recommended task: {random_task} - Priority: High")
        else:
            print("No high-priority tasks available for recommendation.")
    else:
        print("No tasks available for recommendations.")

# Main menu
while True:
    print("\nTask Management App")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. List Tasks")
    print("4. Recommend Task")
    print("5. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        description = input("Enter task description: ")
        priority = input("Enter task priority (Low/Medium/High): ").capitalize()
        add_task(description, priority)
        print("Task added successfully.")

    elif choice == "2":
        description = input("Enter task description to remove: ")
        remove_task(description)

    elif choice == "3":
        list_tasks()

    elif choice == "4":
        recommend_task()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please select a valid option.")
