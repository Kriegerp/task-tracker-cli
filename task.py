import sys
import json

def load_tasks():
    try: 
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
        return tasks
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

def find_task_by_id(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None

print(sys.argv)

if len(sys.argv) <= 1:
    print("Please enter arguments")

elif sys.argv[1] == "add":
    if len(sys.argv) <= 2:
        print("Please enter what you want to add")
    else:
        tasks = load_tasks()

        if len(tasks) == 0:
            new_id = 1
        else:
            new_id = max([task["id"] for task in tasks]) + 1

        task = {
            "id": new_id,
            "description": sys.argv[2],
            "status": "todo",
        }

        tasks.append(task)

        save_tasks(tasks)

elif sys.argv[1] == "list":
    tasks = load_tasks()

    if len(sys.argv) <= 2:
        for task in tasks:
            print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")
    else:
        status_filter = sys.argv[2]
        for task in tasks:
            if task["status"] == status_filter:
                print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")



elif sys.argv[1] == "update":
    if len(sys.argv) < 4:
        print("Please enter what description you want to update")
    elif not sys.argv[2].isdigit():
        print("Please enter a valid task ID")
    else:
        tasks = load_tasks()
        task = find_task_by_id(tasks, int(sys.argv[2]))
        if task:
            task["description"] = sys.argv[3]
            print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")
        else:
            print("ID", sys.argv[2], "not found")
 
        save_tasks(tasks)

elif sys.argv[1] == "delete":
    if len(sys.argv) <= 2:
        print("Please enter which task ID you want to delete")
    elif not sys.argv[2].isdigit():
        print("Please enter a valid task ID")
    else:
        tasks = load_tasks()
        task = find_task_by_id(tasks, int(sys.argv[2]))
        if task:
            tasks.remove(task)
            print("Deleted the task:", sys.argv[2])
        else:
            print("ID", sys.argv[2], "not found")
        save_tasks(tasks)

elif sys.argv[1] == "mark-done" or sys.argv[1] == "mark-in-progress":
    if len(sys.argv) <= 2:
        print("Please enter which task ID you want to update")
    elif not sys.argv[2].isdigit():
        print("Please enter a valid task ID")
    else:
        tasks = load_tasks()
        task = find_task_by_id(tasks, int(sys.argv[2]))
        if sys.argv[1] == "mark-done":
            new_status = "done"
        elif sys.argv[1] == "mark-in-progress":
            new_status = "in-progress"
        
        if task:
            task["status"] = new_status
            print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")
        else:
            print("ID", sys.argv[2], "not found")
        save_tasks(tasks)