import json
import random
from datetime import datetime

class Task:
    def __init__(self, task_id, title, description, created_at):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.created_at = created_at


class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_from_file()

   
    def load_from_file(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                for item in data:
                    task = Task(
                        item["id"],
                        item["title"],
                        item["description"],
                        item["created_at"]
                    )
                    self.tasks.append(task)
        except FileNotFoundError:
            print("No existing file found. Creating new tasks.json...")
            self.save_to_file()
        except json.JSONDecodeError:
            print("JSON decode error! Resetting file.")
            self.tasks = []
            self.save_to_file()

    def save_to_file(self):
        try:
            data = []
            for task in self.tasks:
                data.append({
                    "id": task.task_id,
                    "title": task.title,
                    "description": task.description,
                    "created_at": task.created_at
                })

            with open(self.filename, "w") as f:
                json.dump(data, f, indent=4)

        except Exception as e:
            print("Error while saving!", e)

   
    def add_task(self):
        title = input("Task Title: ")
        description = input("Description: ")
        task_id = random.randint(100, 999)
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        new_task = Task(task_id, title, description, created_at)
        self.tasks.append(new_task)
        print("\nTask added successfully!\n")

    
    def view_tasks(self):
        if not self.tasks:
            print("No tasks found!")
            return

        print("\n====== All Tasks ======")
        for index, task in enumerate(self.tasks):
            print(f"{index+1}. ID: {task.task_id}, Title: {task.title}")
            print(f"   Description: {task.description}")
            print(f"   Created At : {task.created_at}\n")

   
    def update_task(self):
        self.view_tasks()

        try:
            choice = int(input("Enter task number to update: "))
            task = self.tasks[choice - 1]

            new_title = input("New Title: ")
            new_desc = input("New Description: ")

            task.title = new_title
            task.description = new_desc

            print("\nTask updated successfully!\n")

        except (ValueError, IndexError):
            print("Invalid task number!")

   
    def delete_task(self):
        self.view_tasks()

        try:
            choice = int(input("Enter task number to delete: "))
            deleted_task = self.tasks.pop(choice - 1)
            print(f"Task '{deleted_task.title}' deleted successfully!\n")

        except (ValueError, IndexError):
            print("Invalid task number!")



task_manager = TaskManager()

while True:
    print("===== Student Task Tracker =====")
    print("1. Add New Task")
    print("2. View All Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task_manager.add_task()
    elif choice == "2":
        task_manager.view_tasks()
    elif choice == "3":
        task_manager.update_task()
    elif choice == "4":
        task_manager.delete_task()
    elif choice == "5":
        task_manager.save_to_file()
        print("Tasks saved! Exiting program.")
        break
    else:
        print("Invalid choice! Try again.\n")
