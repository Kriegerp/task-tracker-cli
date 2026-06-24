import sys
import json

def load_tasks():
    try: 
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
        return tasks
    except (FileNotFoundError, json.JSONDecodeError):
        return []

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

        with open("tasks.json", "w") as f:
            json.dump(tasks, f)

elif sys.argv[1] == "list":
    tasks = load_tasks()

    for task in tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")

elif sys.argv[1] == "update":
    if len(sys.argv) < 4:
        print("Please enter what description you want to update")
    else:
        tasks = load_tasks()
        found = False
        for task in tasks:
            if int(sys.argv[2]) == task["id"]:
                found = True
                task["description"] = sys.argv[3]
                print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")
        if not found:
            print("ID", sys.argv[2], "not found")
 
        with open("tasks.json", "w") as f:
            json.dump(tasks, f)

elif sys.argv[1] == "delete":
    if len(sys.argv) <= 2:
        print("Please enter which task ID you want to delete")
    else:
        tasks = load_tasks()
        found = False
        for task in tasks:
            if int(sys.argv[2]) == task["id"]:
                found = True
                tasks.remove(task)
                print("Deleted the task:", sys.argv[2])
        if not found:
            print("ID", sys.argv[2], "not found")
        
        with open("tasks.json", "w") as f:
            json.dump(tasks, f)

elif sys.argv[1] == "mark-done" or sys.argv[1] == "mark-in-progress":
    tasks = load_tasks()
    found = False
    if sys.argv[1] == "mark-done":
        new_status = "done"
    elif sys.argv[1] == "mark-in-progress":
        new_status = "in-progress"
    
    for task in tasks:
        if int(sys.argv[2]) == task["id"]:
            found = True
            task["status"] = new_status
            print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")
    if not found:
        print("ID", sys.argv[2], "not found")
    with open("tasks.json", "w") as f:
            json.dump(tasks, f)