#!/usr/bin/env python3

import logging
from argparse import ArgumentParser

from todos.core.constants import DEFAULT_TODO_FILE
from todos.core.logging_config import setup_logging
from todos.core.repl import repl
from todos.core.tasks import add_task, clear_tasks, list_tasks, mark_done, remove_task

logger = logging.getLogger(__name__)


def parse_args():
    parser = ArgumentParser(description="Simple To-Do List Manager")
    parser.add_argument(
        "--file", type=str, default=DEFAULT_TODO_FILE, help="The to-do list file"
    )
    subparsers = parser.add_subparsers(dest="command", required=False)

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("task", type=str, help="The task to add")

    remove_parser = subparsers.add_parser("remove", help="Remove a task by index")
    remove_parser.add_argument(
        "index", type=int, help="The index of the task to remove"
    )

    subparsers.add_parser("list", help="List all tasks")

    subparsers.add_parser("clear", help="Clear all tasks")

    done_parser = subparsers.add_parser("done", help="Mark a task as done by index")
    done_parser.add_argument(
        "index", type=int, help="The index of the task to mark as done"
    )

    parser.add_argument("--repl", action="store_true", help="Enter REPL mode")

    return parser, parser.parse_args()


def run():
    setup_logging(default_level=logging.DEBUG)
    parser, args = parse_args()

    if args.repl:
        repl(args.file)
    elif args.command == "add":
        add_task(args.task, args.file)
    elif args.command == "remove":
        remove_task(args.index, args.file)
    elif args.command == "list":
        list_tasks(args.file)
    elif args.command == "clear":
        clear_tasks(args.clear)
    elif args.command == "done":
        mark_done(args.index, args.file)
    else:
        parser.print_help()


if __name__ == "__main__":
    run()
