#!/usr/bin/env python3

import logging

from .constants import REPL_BANNER, REPL_COMMANDS
from .tasks import add_task, remove_task, list_tasks, mark_done

logger = logging.getLogger(__name__)


def repl(file):
    """
    Enter REPL mode for the to-do list application.

    :param file: The file where the to-do list is stored.
    :type file: str
    """
    print(REPL_BANNER)
    print("Entering REPL mode. Type 'help' for a list of commands.")

    while True:
        try:
            # Get user input and split it into a command and arguments
            command = input("> ").strip().split()

            # Skip empty commands
            if not command:
                continue

            # Extract the command and arguments
            cmd, *args = command

            # Process the command
            if cmd == "add":
                if args:
                    add_task(" ".join(args), file)
                else:
                    print("Usage: add <task>")
            elif cmd == "remove":
                if args and args[0].isdigit():
                    remove_task(int(args[0]), file)
                else:
                    print("Usage: remove <index>")
            elif cmd == "list":
                list_tasks(file)
            elif cmd == "done":
                if args and args[0].isdigit():
                    mark_done(int(args[0]), file)
                else:
                    print("Usage: done <index>")
            elif cmd == "exit":
                break
            elif cmd == "help":
                print(REPL_COMMANDS)
            else:
                print(f"Unknown command: {cmd}")
        except (EOFError, KeyboardInterrupt):
            break

    print("Exiting REPL mode. Goodbye.")
