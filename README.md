# To-Do Task System

A simple, professional **console-based To-Do Task System** built with Python.  
The application keeps the original file-handling approach and stores tasks locally in `tasks.txt`.

## Features

- Add new tasks
- View all tasks
- Mark tasks as completed
- Delete tasks
- Display task totals, pending tasks, and completed tasks
- Persistent local file storage
- Handles invalid menu choices and task numbers without crashing
- Handles missing or malformed storage data gracefully
- No external Python packages required

## Project Structure

```text
todo_task_system/
├── main.py            # Console application and menu
├── task.py            # Task operations and task model
├── file_handler.py    # Save/load tasks from tasks.txt
├── tasks.txt          # Local task storage
├── README.md          # Project documentation
├── .gitignore         # Git ignore rules
└── LICENSE            # MIT License
```

## Requirements

- Python 3.10 or newer

No external dependencies are required.

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/todo-task-system.git
```

2. Open the project directory:

```bash
cd todo-task-system
```

3. Run the application:

```bash
python main.py
```

On some systems, use:

```bash
python3 main.py
```

## Data Storage

Tasks are saved automatically to:

```text
tasks.txt
```

Each line uses this format:

```text
Task title|Status
```

Example:

```text
Finish project documentation|Pending
Upload project to GitHub|Completed
```

The file is intentionally kept simple so the project demonstrates basic Python file handling.

## Usage

When the program starts, choose an option from the menu:

```text
1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Exit
```

Changes are saved automatically after adding, completing, or deleting a task, and again when exiting.

## Code Quality

The project is separated into clear responsibilities:

- `main.py` handles the user interface and program flow.
- `task.py` handles task-related operations.
- `file_handler.py` handles persistent storage.

The code also uses:

- Functions with clear responsibilities
- Type hints
- Docstrings
- Context managers for file operations
- Error handling for invalid user input and file errors
- `if __name__ == "__main__"` as the application entry point

## Future Improvements

Possible future extensions include:

- Edit an existing task
- Search and filter tasks
- Add due dates and priorities
- Export tasks to CSV or JSON
- Add automated tests
- Add a graphical user interface

## License

This project is licensed under the MIT License. See `LICENSE` for details.
