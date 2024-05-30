#!/usr/bin/env bash

# Check if make is installed
if ! command -v make &> /dev/null
then
    echo "make could not be found. Please install make and try again."
    exit 1
fi

# Run make install
make install

# Check if the installation was successful
if [ $? -eq 0 ]; then
    echo "Installation successful!"
else
    echo "Installation failed. Please check the error messages above."
    exit 1
fi
