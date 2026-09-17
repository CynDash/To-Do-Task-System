FILE_NAME = "tasks.txt"


def save_tasks(tasks):
    file = open(FILE_NAME, "w")

    for task in tasks:
        file.write(task["title"] + "|" + task["status"] + "\n")

    file.close()


def load_tasks():
    tasks = []

    try:
        file = open(FILE_NAME, "r")

        for line in file:
            data = line.strip().split("|")

            if len(data) == 2:
                task = {
                    "title": data[0],
                    "status": data[1]
                }

                tasks.append(task)

        file.close()

    except FileNotFoundError:
        pass

    return tasks