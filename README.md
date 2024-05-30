# todo-cli

## Simple To-Do List Manager

A simple command-line interface (CLI) application to manage your to-do list.

## Features

- Add a new task
- Remove a task by index
- List all tasks
- Clear all tasks
- Mark a task as done by index
- Optionally specify the to-do list file
- Enter REPL mode

## Requirements

- Python 3.7+
- `make` utility

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/rmkane/todo-cli.git
   cd todo-cli
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   ./install.sh
   ```

## Usage

The CLI supports the following commands:

```bash
todo-cli {add,remove,list,clear,done} [--file FILE] [--repl]
```

### Commands

- **add**: Add a new task
   ```bash
   todo-cli add "Your new task"
   ```

- **remove**: Remove a task by index
   ```bash
   todo-cli remove 1
   ```

- **list**: List all tasks
   ```bash
   todo-cli list
   ```

- **clear**: Clear all tasks
   ```bash
   todo-cli clear
   ```

- **done**: Mark a task as done by index
   ```bash
   todo-cli done 1
   ```

### Optional Arguments

- **--file FILE**: Specify the to-do list file
   ```bash
   todo-cli list --file mytasks.txt
   ```

- **--repl**: Enter REPL (Read-Eval-Print Loop) mode
   ```bash
   todo-cli --repl
   ```

## Development

### Makefile Targets

- **all**: Install the package (default target)
  ```bash
  make all
  ```

- **test**: Run tests
  ```bash
  make test
  ```

- **install**: Install the package
  ```bash
  make install
  ```

- **uninstall**: Uninstall the package
  ```bash
  make uninstall
  ```

- **wheel_dep**: Ensure wheel is installed
  ```bash
  make wheel_dep
  ```

- **build**: Build the package
  ```bash
  make build
  ```

- **wheel**: Create a wheel
  ```bash
  make wheel
  ```

- **format**: Ensure black is installed and run the formatter
  ```bash
  make format
  ```

- **clean**: Clean up build directories and files
  ```bash
  make clean
  ```

- **rebuild**: Clean up and build the package
  ```bash
  make rebuild
  ```

- **remove_venv**: Remove the virtual environment
  ```bash
  make remove_venv
  ```

- **full_clean**: Clean build directories, remove the virtual environment, and logs
  ```bash
  make full_clean
  ```

- **help**: Display help message
  ```bash
  make help
  ```

## License

This project is licensed under the GNU General Public License - see
the [LICENSE](https://www.gnu.org/licenses/gpl-3.0.en.html) file for details.
