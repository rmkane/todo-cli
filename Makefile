# Makefile for todo-cli

.PHONY: all install uninstall build wheel clean rebuild help

# Variables for Python and pip executables
PYTHON = python3
PIP = pip3

# Python package name
PACKAGE_NAME = todo-cli

# Default target
all: install

# Install the package using pip
install: ## Install the package using pip
	$(PIP) install .

# Uninstall the package using pip
uninstall: ## Uninstall the package using pip
	$(PIP) uninstall -y $(PACKAGE_NAME)

# Ensure wheel is installed
wheel_dep: ## Ensure wheel is installed
	$(PIP) install wheel

# Build the package
build: wheel_dep ## Build the package
	$(PYTHON) setup.py sdist bdist_wheel

# Create a wheel
wheel: wheel_dep ## Create a wheel
	$(PYTHON) setup.py bdist_wheel

# Clean up build directories
clean: ## Clean up build directories
	rm -rf build dist *.egg-info
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -rf {} +

# Clean up and build the package
rebuild: clean build ## Clean up and build the package

# Display help
help: ## Display this help
	@echo "Available targets:"
	@awk 'BEGIN {FS = ":.*##"} /^[a-zA-Z_-]+:.*?##/ { printf "  %-15s %s\n", $$1, $$2 }' $(MAKEFILE_LIST)
