
import os
from pathlib import Path

# `username` of the operating system
# default is the current user `username`
# USERNAME=''
USERNAME = os.getenv('USERNAME')

# `project` or `repository` directory path
# default is `bookless` repository clone
# PROJECTDIR=''
PROJECTDIR = Path(__file__).resolve().parent.parent

# `virtual environment` directory path
# default is one level inside `bookless` repository clone
# VENVDIR=''
VENVDIR = Path(__file__).resolve().parent.parent / '.venv'

# number of `workers` or `instances` that run `bookless`
# default is `2`
WORKERS=2

