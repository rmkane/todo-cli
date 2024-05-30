#!/usr/bin/env python3

import os
import sys
import unittest

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Now the relative import will work
from todos.core.helpers import index_in_range  # noqa: E402

# Define the base directory for resources
RESOURCE_DIR = os.path.join(os.path.dirname(__file__), "resources", "config")


class TestConfig(unittest.TestCase):
    def test_index_in_range(self):
        mock_todos = list(range(10))

        # In range
        self.assertTrue(index_in_range(1, mock_todos))
        self.assertTrue(index_in_range(9, mock_todos))

        # Out of range
        self.assertFalse(index_in_range(-1, mock_todos))
        self.assertFalse(index_in_range(10, mock_todos))


if __name__ == "__main__":
    unittest.main()
