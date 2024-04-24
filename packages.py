# packages - third party modules
# PYPI.org - download and install

# cowsay

# PIP - package manager - allows you to install libraries

# pip install cowsay - entered in the command line

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])
