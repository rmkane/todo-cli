import setuptools

# PyPi package information
PACKAGE_NAME = "todo-cli"
VERSION = "0.0.1"

# CLI information
MODULE_NAME = "todos"  # The name of the module containing the CLI
MAIN_FILE = "cli"  # The name of the file containing the main function
MAIN_FUNCTION = "run"  # The name of the main function
BINARY = "todo"  # The name of the binary that will be created

# Read the long description from the README
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author="Ryan Kane",
    author_email="rmkane@proto.me",
    description="A simple CLI to-do list manager",
    license="GPLv3+",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPLv3",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [f"{BINARY}={MODULE_NAME}.{MAIN_FILE}:{MAIN_FUNCTION}"],
    },
    install_requires=[
        "PyYAML",
    ],
    python_requires=">=3.7",
)
