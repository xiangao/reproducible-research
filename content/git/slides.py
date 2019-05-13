#!/usr/bin/env python
import sys
from tempfile import NamedTemporaryFile
import subprocess

# if __name__ == '__main__':
path = sys.argv[1]
temp = NamedTemporaryFile(mode='w')

with open(path) as f:
    note = False
    for line in f:
        if line == '<!-- NOTES -->\n':
            note = True
        if line.startswith('#'):
            line = line[1:]
            note = False
        if not note:
            temp.write(line)

temp.write('''
<style type="text/css">
  .reveal .slides > section > section { text-align:left; }
</style>
''')
temp.flush()
command = f'/usr/local/bin/pandoc -t revealjs -s -o slides {temp.name} -V revealjs-url=https://revealjs.com --slide-level=2 -V transition=none -V width=1200 -V height=875 -V theme=white'

subprocess.call(command, shell=True)
