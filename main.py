from file_handler import load_tasks, save_tasks
from task import add_task, complete_task, delete_task, view_tasks


APP_TITLE = "TO-DO TASK SYSTEM"


def print_menu() -> None:
    print("\n" + "=" * 42)
    print(f"{APP_TITLE:^42}")
    print("=" * 42)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")
    print("-" * 42)


def read_task_number(prompt: str) -> int | None:
    value = input(prompt).strip()
    try:
        number = int(value)
    except ValueError:
        print("Please enter a valid task number.")
        return None

    if number < 1:
        print("Task number must be greater than 0.")
        return None

    return number


def main() -> None:
    tasks = load_tasks()

    print(f"\nWelcome to the {APP_TITLE.title()}!")
    print(f"{len(tasks)} task(s) loaded from storage.")

    while True:
        print_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            title = input("Enter task: ").strip()
            if not title:
                print("Task cannot be empty.")
                continue

            if "|" in title or "\n" in title or "\r" in title:
                print("Task cannot contain the '|' character or line breaks.")
                continue

            add_task(tasks, title)
            save_tasks(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            if not view_tasks(tasks):
                continue

            number = read_task_number("Enter task number to complete: ")
            if number is not None and complete_task(tasks, number):
                save_tasks(tasks)

        elif choice == "4":
            if not view_tasks(tasks):
                continue

            number = read_task_number("Enter task number to delete: ")
            if number is not None and delete_task(tasks, number):
                save_tasks(tasks)

        elif choice == "5":
            save_tasks(tasks)
            print("\nTasks saved successfully.")
            print("Thank you for using the To-Do Task System!")
            break

        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
