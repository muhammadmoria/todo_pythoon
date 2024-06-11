from todo_functions import *

def main():
    print("Welcome to the To-Do List Application!")

    while True:
        print("\nPlease select an option:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '3':
            task_id = int(input("Enter the task ID to delete: "))
            delete_task(task_id)
        elif choice == '4':
            print("Exiting the application...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
