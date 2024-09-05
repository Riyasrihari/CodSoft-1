import json
import os

# Define the path for storing the tasks
TASKS_FILE = 'tasks.json'

def load_tasks():
    """Load tasks from the JSON file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, description):
    """Add a new task."""
    tasks.append({"description": description, "completed": False})
    save_tasks(tasks)
    print(f"Task added: {description}")

def list_tasks(tasks):
    """List all tasks."""
    if not tasks:
        print("No tasks to show.")
        return

    for index, task in enumerate(tasks):
        status = "Done" if task["completed"] else "Pending"
        print(f"{index + 1}. {task['description']} - {status}")

def complete_task(tasks, task_number):
    """Mark a task as completed."""
    try:
        task_number = int(task_number) - 1
        if 0 <= task_number < len(tasks):
            tasks[task_number]["completed"] = True
            save_tasks(tasks)
            print(f"Task #{task_number + 1} marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks, task_number):
    """Delete a task."""
    try:
        task_number = int(task_number) - 1
        if 0 <= task_number < len(tasks):
            removed_task = tasks.pop(task_number)
            save_tasks(tasks)
            print(f"Task #{task_number + 1} deleted: {removed_task['description']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            description = input("Enter the task description: ")
            add_task(tasks, description)
        elif choice == '2':
            list_tasks(tasks)
        elif choice == '3':
            list_tasks(tasks)
            task_number = input("Enter the task number to mark as completed: ")
            complete_task(tasks, task_number)
        elif choice == '4':
            list_tasks(tasks)
            task_number = input("Enter the task number to delete: ")
            delete_task(tasks, task_number)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
