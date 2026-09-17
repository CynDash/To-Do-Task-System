"""Task operations for the To-Do Task System."""

from typing import TypedDict


class Task(TypedDict):
    """Structure used for a stored task."""

    title: str
    status: str


PENDING = "Pending"
COMPLETED = "Completed"


def add_task(tasks: list[Task], title: str) -> None:
    """Add a new pending task."""
    tasks.append({"title": title.strip(), "status": PENDING})
    print("Task added successfully!")


def view_tasks(tasks: list[Task]) -> bool:
    """Display all tasks and return whether at least one exists."""
    if not tasks:
        print("\nNo tasks found.")
        return False

    print("\n" + "=" * 60)
    print("YOUR TASKS")
    print("=" * 60)

    for index, task in enumerate(tasks, start=1):
        status = task["status"]
        marker = "✓" if status == COMPLETED else " "
        print(f"{index:>3}. [{marker}] {task['title']} — {status}")

    pending = sum(task["status"] != COMPLETED for task in tasks)
    completed = len(tasks) - pending
    print("-" * 60)
    print(f"Total: {len(tasks)} | Pending: {pending} | Completed: {completed}")
    return True


def complete_task(tasks: list[Task], number: int) -> bool:
    """Mark a task as completed. Return True when successful."""
    if number < 1 or number > len(tasks):
        print("Invalid task number.")
        return False

    task = tasks[number - 1]
    if task["status"] == COMPLETED:
        print("That task is already completed.")
        return False

    task["status"] = COMPLETED
    print("Task completed!")
    return True


def delete_task(tasks: list[Task], number: int) -> bool:
    """Delete a task by its displayed number. Return True when successful."""
    if number < 1 or number > len(tasks):
        print("Invalid task number.")
        return False

    deleted = tasks.pop(number - 1)
    print(f"Task deleted: {deleted['title']}")
    return True
