
# Task Tracker

A simple command-line task tracker that stores tasks in a JSON file and reads it.

## Requirements
- python3, no external dependencies

## Usage
Upon using the .py file, it will create a new file "tasks.json" in the directory and saves the tasks inside.

Here are a few command lines that can be used:
```bash
python3 task.py list (filter)
```
Lists all tasks. Filters are "todo", "in-progress" and "done"

```bash
python3 task.py add <description>
```
Adds a new task with description.

```bash
python3 task.py update <task ID> <description>
```
Edits and updates a description of a task

```bash
python3 task.py delete <task ID>
```
Deletes a task.

```bash
python3 task.py mark-done <task ID>
```
Marks a task as "done".

```bash
python3 task.py mark-in-progress <task ID>
```
Marks a task as "in-progress"

## Example
```bash
python3 task.py add "Buy groceries"
python3 task.py mark-done 1
python3 task.py list done
```