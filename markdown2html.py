#!/usr/bin/python3
"""
Write a script markdown2html.py that takes an argument 2 strings:

First argument is the name of the Markdown file
Second argument is the output file name
Requirements:

If the number of arguments is less than 2: print in STDERR Usage:
./markdown2html.py README.md README.html and exit 1
If the Markdown file doesn’t exist:
print in STDER Missing <filename> and exit 1
Otherwise, print nothing and exit 0
"""

import sys
import os.path
import markdown

if len(sys.argv) < 3:
    sys.stderr.write("Usage: {} README.md README.html\n".format(sys.argv[0]))
    sys.exit(1)

md_file = sys.argv[1]
if not os.path.isfile(md_file):
    sys.stderr.write("Missing {}\n".format(md_file))
    sys.exit(1)

html_file = sys.argv[2]
with open(md_file, 'r') as f:
    md = f.read()
    html = markdown.markdown(md)
    with open(html_file, 'w') as g:
        g.write(html)
sys.exit(0)
