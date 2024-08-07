todo_list = []
file_name = "todo_list.txt"

def load_tasks():
    try:
        with open(file_name, "r") as file:
            for line in file:
                todo_list.append(line.strip())
    except FileNotFoundError:
        pass  # No tasks to load if the file doesn't exist

def save_tasks():
    with open(file_name, "w") as file:
        for task in todo_list:
            file.write(task + "\n")

def display_menu():
    print("Welcome to the Todo List Application!")
    print("Please choose an option:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

def add_task():
    task = input("Enter the task you want to add: ")
    if task.strip():
        todo_list.append(task)
        save_tasks()
        print(f"Task '{task}' added.")
    else:
        print("Task cannot be empty. Please enter a valid task.")

def remove_task():
    if not todo_list:
        print("Your Todo List is empty.")
        return

    view_tasks()
    try:
        task_number = int(input("Enter the task number to remove: "))
        if 0 < task_number <= len(todo_list):
            removed_task = todo_list.pop(task_number - 1)
            save_tasks()
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number. Please enter a number between 1 and", len(todo_list))
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def view_tasks():
    if todo_list:
        print("Your Todo List:")
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")
    else:
        print("Your Todo List is empty.")

def main():
    load_tasks()
    while True:
        display_menu()
        choice = input("> ")
        if choice == '1':
            add_task()
        elif choice == '2':
            remove_task()
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()