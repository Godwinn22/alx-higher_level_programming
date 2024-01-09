# This is a readme file for my ALX 0x03-python-data_structures project.

For python scripts "#!/usr/bin/python3"
for shell scripts "#!/bin/bash"

## To use the pycodestyle
pip install pycodestyle
pip install --upgrade pycodestyle
pip uninstall pycodestyle
pycodestyle --first optparse.py

You can also make pycodestyle.py show the source code for each error, and even the relevant text from PEP 8:
pycodestyle --show-source --show-pep8 testing/data/E40.py

Or you can display how often each error was found:
pycodestyle --statistics -qq Python-2.5/Lib