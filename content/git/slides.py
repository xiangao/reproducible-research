#!/usr/bin/env python
import sys
from tempfile import NamedTemporaryFile
import subprocess

# if __name__ == '__main__':
path = sys.argv[1]

temp = NamedTemporaryFile(mode='w')

with open(path) as f:
    for line in f:
        if line.startswith('#'):
            line = line[1:]
        temp.write(line)
    # 1. need to demote

command = f'/usr/local/bin/pandoc -t revealjs -s -o slides {temp.name} -V revealjs-url=https://revealjs.com --slide-level=2 -V transition=none'

subprocess.call(command, shell=True)
