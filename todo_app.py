# Small Python Project: To-Do List App (Command-Line Based)

# Step 1: Setup Project Directory
# Create a folder named 'todo_app'
# Inside the folder, create a file named 'todo.py'

# Step 2: Code the application

# todo.py
import os

# File to store tasks
todo_file = "tasks.txt"

# Function to load tasks from file
def load_tasks():
    if not os.path.exists(todo_file):
        return []
    with open(todo_file, "r") as f:
        return [line.strip() for line in f.readlines()]

# Function to save tasks to file
def save_tasks(tasks):
    with open(todo_file, "w") as f:
        for task in tasks:
            f.write(task + "\n")

# Function to show menu
def show_menu():
    print("\nTo-Do List Application")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

# Main function
def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            if not tasks:
                print("\nNo tasks found.")
            else:
                print("\nTasks:")
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task}")

        elif choice == "2":
            new_task = input("Enter new task: ")
            tasks.append(new_task)
            save_tasks(tasks)
            print("Task added.")

        elif choice == "3":
            if not tasks:
                print("No tasks to remove.")
            else:
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task}")
                try:
                    task_num = int(input("Enter task number to remove: "))
                    if 1 <= task_num <= len(tasks):
                        removed = tasks.pop(task_num - 1)
                        save_tasks(tasks)
                        print(f"Removed: {removed}")
                    else:
                        print("Invalid number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select from menu.")

# Entry point
if __name__ == "__main__":
    main()

# Step 3: Run the Application
# In your terminal:
# cd path/to/todo_app
# python todo.py
