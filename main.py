from task import add_task, view_tasks, complete_task, delete_task
from file_handler import save_tasks, load_tasks


def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO TASK SYSTEM =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task: ")

            if title.strip() == "":
                print("Task cannot be empty.")
            else:
                add_task(tasks, title)
                save_tasks(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            view_tasks(tasks)

            if len(tasks) > 0:
                number = int(input("Enter task number: "))
                complete_task(tasks, number)
                save_tasks(tasks)

        elif choice == "4":
            view_tasks(tasks)

            if len(tasks) > 0:
                number = int(input("Enter task number: "))
                delete_task(tasks, number)
                save_tasks(tasks)

        elif choice == "5":
            save_tasks(tasks)
            print("Thank you for using the To-Do Task System!")
            break

        else:
            print("Invalid choice. Please try again.")


main()
