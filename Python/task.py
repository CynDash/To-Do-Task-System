def add_task(tasks, title):
    task = {
        "title": title,
        "status": "Pending"
    }

    tasks.append(task)
    print("Task added successfully!")


def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks found.")
        return

    print("\n===== YOUR TASKS =====")

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['title']} - {task['status']}")


def complete_task(tasks, number):
    if number < 1 or number > len(tasks):
        print("Invalid task number.")
        return

    tasks[number - 1]["status"] = "Completed"
    print("Task completed!")


def delete_task(tasks, number):
    if number < 1 or number > len(tasks):
        print("Invalid task number.")
        return

    tasks.pop(number - 1)
    print("Task deleted!")