#!/bin/bash

echo "Check if virtualenv is installed"
if ! python3 -m virtualenv --version &> /dev/null
then
    echo "Installing virtualenv"
    python3 -m pip install virtualenv
fi

echo "Create Virtual Environment"
python3 -m virtualenv .venv

echo "Activate Virtual Environment"
source .venv/bin/activate

echo "Install the required packages"
python3 -m pip install -r requirements.txt