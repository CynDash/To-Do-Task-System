"""File persistence for the To-Do Task System."""

from pathlib import Path

from task import Task, PENDING, COMPLETED


FILE_NAME = "tasks.txt"
DATA_FILE = Path(__file__).resolve().parent / FILE_NAME
SEPARATOR = "|"


def save_tasks(tasks: list[Task]) -> None:
    """Save all tasks to the local text file."""
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            for task in tasks:
                file.write(f"{task['title']}{SEPARATOR}{task['status']}\n")
    except OSError as error:
        print(f"Error saving tasks: {error}")


def load_tasks() -> list[Task]:
    """Load valid tasks from the local text file.

    Missing storage is treated as a first run. Malformed lines are skipped
    rather than crashing the application.
    """
    tasks: list[Task] = []

    if not DATA_FILE.exists():
        return tasks

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                raw = line.rstrip("\n\r")
                if not raw:
                    continue

                data = raw.split(SEPARATOR, maxsplit=1)
                if len(data) != 2:
                    print(f"Warning: skipped malformed line {line_number}.")
                    continue

                title, status = (part.strip() for part in data)
                if not title or status not in {PENDING, COMPLETED}:
                    print(f"Warning: skipped invalid line {line_number}.")
                    continue

                tasks.append({"title": title, "status": status})
    except OSError as error:
        print(f"Error loading tasks: {error}")

    return tasks
