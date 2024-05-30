import setuptools

PACKAGE_NAME = "todo-cli"
MODULE_NAME = "todos"
MAIN_FILE = "cli"
MAIN_FUNCTION = "run"
VERSION = "0.0.1"
BINARY = "todo"

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author="Ryan Kane",
    author_email="rmkane@proto.me",
    description="A simple CLI to-do list manager",
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
