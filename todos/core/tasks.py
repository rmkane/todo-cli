#!/usr/bin/env python3

import logging

from .helpers import format_todo, index_in_range, load_todos, save_todos

logger = logging.getLogger(__name__)


def add_task(task, file):
    todos = load_todos(file)
    todos.append({"task": task, "done": False})
    save_todos(todos, file)
    print(f"Added task: {task}")


def clear_tasks(file):
    save_todos([], file)
    print("Cleared all tasks.")


def list_tasks(file):
    todos = load_todos(file)

    if not todos:
        print("No tasks in the list.")
        return

    padding = len(str(len(todos)))

    for i, todo in enumerate(todos):
        print(format_todo(todo, i, padding))


def mark_done(index, file):
    todos = load_todos(file)

    if not index_in_range(index, todos):
        return

    todos[index]["done"] = True
    save_todos(todos, file)
    print(f"Marked task as done: {todos[index]['task']}")


def remove_task(index, file):
    todos = load_todos(file)

    if not index_in_range(index, todos):
        return

    removed_task = todos.pop(index)
    save_todos(todos, file)
    print(f"Removed task: {removed_task['task']}")
