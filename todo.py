"""Simple command-line to-do list manager.

Usage:
    python todo.py add "Buy milk"
    python todo.py list
    python todo.py done 1
    python todo.py delete 1
    python todo.py clear
"""
import argparse
import json
from pathlib import Path

DATA_FILE = Path("tasks.json")


def load_tasks(path=DATA_FILE):
    """Load tasks from a JSON file. Returns an empty list if none exists."""
    if not Path(path).exists():
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks, path=DATA_FILE):
    """Save tasks to a JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def add_task(tasks, title):
    """Add a new task and return it."""
    task = {"id": max((t["id"] for t in tasks), default=0) + 1,
            "title": title, "done": False}
    tasks.append(task)
    return task


def mark_done(tasks, task_id):
    """Mark a task as done. Returns True if found."""
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            return True
    return False


def delete_task(tasks, task_id):
    """Delete a task by id. Returns True if something was removed."""
    before = len(tasks)
    tasks[:] = [t for t in tasks if t["id"] != task_id]
    return len(tasks) < before


def format_tasks(tasks):
    """Return a printable string of all tasks."""
    if not tasks:
        return "No tasks yet. Add one with: python todo.py add \"Your task\""
    return "\n".join(
        f"[{'x' if t['done'] else ' '}] {t['id']}. {t['title']}" for t in tasks
    )


def main():
    parser = argparse.ArgumentParser(description="Simple CLI to-do list")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="Add a task")
    p_add.add_argument("title", help="Task description")
    sub.add_parser("list", help="Show all tasks")
    p_done = sub.add_parser("done", help="Mark a task as done")
    p_done.add_argument("id", type=int)
    p_del = sub.add_parser("delete", help="Delete a task")
    p_del.add_argument("id", type=int)
    sub.add_parser("clear", help="Delete all tasks")

    args = parser.parse_args()
    tasks = load_tasks()

    if args.command == "add":
        task = add_task(tasks, args.title)
        print(f"Added task {task['id']}: {task['title']}")
    elif args.command == "list":
        print(format_tasks(tasks))
    elif args.command == "done":
        print("Marked as done." if mark_done(tasks, args.id) else "Task not found.")
    elif args.command == "delete":
        print("Deleted." if delete_task(tasks, args.id) else "Task not found.")
    elif args.command == "clear":
        tasks.clear()
        print("All tasks cleared.")

    save_tasks(tasks)


if __name__ == "__main__":
    main()
