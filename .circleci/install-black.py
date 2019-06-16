#!./venv/bin/python

import sys

if sys.version_info < (3, 6):
    print("Skipping python black install (python >=3.6 required.)")
    sys.exit(0)

import subprocess

subprocess.check_call(["./venv/bin/python", "-m", "pip", "install", "--progress-bar", "off", "black==19.3b0"])
