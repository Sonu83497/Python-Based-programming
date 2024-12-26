# A simple To-Do List application

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Stop")

def view_tasks(tasks):
    if not tasks:
        print("\nList is Empty.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"'{task}' has been added to your to-do list.")

def remove_task(tasks):
    task_num = int(input("Enter the task number to remove: "))
    if 0 < task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)
        print(f"'{removed_task}' has been removed from your to-do list.")
    else:
        print("Invalid task number!")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Choose any one option (1-4): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Exit 'To-Do List'")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
