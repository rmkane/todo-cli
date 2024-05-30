#!/usr/bin/env python3

import logging
import yaml

logger = logging.getLogger(__name__)


def format_todo(todo, index, padding=1):
    status = "x" if todo["done"] else " "
    return f"{index:>{padding}}: [{status}] {todo['task']}"


def index_in_range(index, todos):
    if index < 0 or index >= len(todos):
        print(f"Task index {index} is out of range.")
        return False
    return True


def load_todos(file):
    try:
        with open(file, 'r') as f:
            return yaml.safe_load(f) or []
    except FileNotFoundError:
        logger.info(f"The file {file} was not found. Starting with an empty list.")
        return []
    except Exception as e:
        logger.error(f"Failed to load file {file}: {e}")
        return []


def save_todos(todos, file):
    try:
        with open(file, 'w') as f:
            yaml.safe_dump(todos, f)
    except Exception as e:
        logger.error(f"Failed to save file {file}: {e}")
