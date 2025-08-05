# File to store tasks
FILENAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Main app logic
def main():
    tasks = load_tasks()
    print("To-Do List App")

    while True:
        print("\n1. Add Tasks\n2. View Tasks\n3. Delete Task\n4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            new_task = input("Enter new task: ")
            tasks.append(new_task)
            save_tasks(tasks)
            print("Task added!")

        elif choice == "2":
                if tasks:
                    print("\nYour Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                else:
                    print("No tasks yet!")
    
        elif choice == "3":
            del_task = input("Enter exact task to delete: ")
            if del_task in tasks:
                tasks.remove(del_task)
                save_tasks(tasks)
                print("Task deleted!")
            else:
                print("Task not found.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

main()
