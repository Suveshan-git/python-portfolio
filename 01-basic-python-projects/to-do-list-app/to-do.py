import json
import os
from datetime import datetime

# File to save tasks
TASKS_FILE = "tasks.json"

# Load existing tasks or start fresh
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(tasks):
    title = input("Enter task title: ").strip()
    due_date = input("Enter due date (YYYY-MM-DD) or leave blank: ").strip()
    
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "due_date": due_date if due_date else None,
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("\nYour Tasks:")
    for task in tasks:
        status = "(Done)" if task["completed"] else "(Pending)"
        due = f"(Due: {task['due_date']})" if task["due_date"] else ""
        print(f"{task['id']}. {status} {task['title']} {due}")

# Mark a task as completed
def complete_task(tasks):
    task_id = input("Enter task ID to mark as completed: ").strip()
    for task in tasks:
        if str(task["id"]) == task_id:
            task["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed!")
            return
    print("Task not found.")

# Delete a task
def delete_task(tasks):
    task_id = input("Enter task ID to delete: ").strip()
    for task in tasks:
        if str(task["id"]) == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("Task deleted.")
            return
    print("Task not found.")

# Main menu loop
def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List CLI")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
