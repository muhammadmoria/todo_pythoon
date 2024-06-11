TODO_FILE = "todo.txt"

def view_tasks():
    try:
        with open(TODO_FILE, 'r') as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks found!")
            else:
                print("Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks found!")

def add_task(task):
    try:
        with open(TODO_FILE, 'a') as file:
            file.write(task + "\n")
        print("Task added successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_task(task_id):
    try:
        with open(TODO_FILE, 'r') as file:
            tasks = file.readlines()
        with open(TODO_FILE, 'w') as file:
            for i, task in enumerate(tasks, start=1):
                if i != task_id:
                    file.write(task)
        print("Task deleted successfully!")
    except FileNotFoundError:
        print("No tasks found!")
    except IndexError:
        print("Invalid task ID!")
    except Exception as e:
        print(f"An error occurred: {e}")
