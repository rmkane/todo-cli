#!/usr/bin/env python3

"""
This module contains constants used throughout the todos application.
"""

DEFAULT_TODO_FILE = "todo.yaml"
"""
The default file name for the to-do list.

:rtype: str
"""

REPL_BANNER = """
 _____ ___________ _____   ______ ___________ _
|_   _|  _  |  _  \\  _  |  | ___ \\  ___| ___ \\ |
  | | | | | | | | | | | |  | |_/ / |__ | |_/ / |
  | | | | | | | | | | | |  |    /|  __||  __/| |
  | | \\ \\_/ / |/ /\\ \\_/ /  | |\\ \\| |___| |   | |____
  \\_/  \\___/|___/  \\___/   \\_| \\_\\____/\\_|   \\_____/
"""
"""
The banner displayed when entering REPL mode.

:rtype: str
"""

REPL_COMMANDS = """
Commands:
- add <task>
- remove <index>
- list
- done <index>
- exit
"""
"""
The list of commands available in REPL mode.

:rtype: str
"""
