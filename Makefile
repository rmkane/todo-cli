# Makefile for todo-cli

.PHONY: all test install uninstall build wheel clean rebuild format remove_venv full_clean help

# Variables for Python and pip executables in the virtual environment
VENV_DIR = .venv
PYTHON = $(VENV_DIR)/bin/python
PIP = $(VENV_DIR)/bin/pip

# Python package name
PACKAGE_NAME = todo-cli
TEST_DIR = tests

# Default target
all: install

# Create the virtual environment if it doesn't exist
$(VENV_DIR):
	python3 -m venv $(VENV_DIR)

# Run tests
test: $(VENV_DIR) ## Run tests
	$(PYTHON) -m unittest discover -s $(TEST_DIR)

# Install the package using pip within the virtual environment
install: $(VENV_DIR) ## Install the package
	$(PIP) install .

# Uninstall the package using pip within the virtual environment
uninstall: $(VENV_DIR) ## Uninstall the package
	$(PIP) uninstall -y $(PACKAGE_NAME)

# Ensure wheel is installed within the virtual environment
wheel_dep: $(VENV_DIR) ## Ensure wheel is installed
	$(PIP) install wheel

# Build the package within the virtual environment
build: wheel_dep ## Build the package
	$(PYTHON) setup.py sdist bdist_wheel

# Create a wheel within the virtual environment
wheel: wheel_dep ## Create a wheel
	$(PYTHON) setup.py bdist_wheel

# Ensure black is installed and run the formatter
format: $(VENV_DIR) ## Ensure black is installed and run the formatter
	$(PIP) install black
	$(VENV_DIR)/bin/black .

# Clean up build directories and files
clean: ## Clean up build directories and files
	rm -rf build dist *.egg-info
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -rf {} +

# Clean up and build the package
rebuild: clean build ## Clean up and rebuild the package

# Remove the virtual environment
remove_venv: ## Remove the virtual environment
	rm -rf $(VENV_DIR)

# Full clean including logs
full_clean: clean remove_venv ## Clean build directories, remove virtual environment, and logs
	rm -rf log/
	rm -rf *.log

# Display help
help: ## Display this help message
	@echo "Available targets:"
	@awk 'BEGIN {FS = ":.*##"} /^[a-zA-Z_-]+:.*?##/ { printf "  %-15s %s\n", $$1, $$2 }' $(MAKEFILE_LIST)
