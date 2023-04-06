#!/usr/bin/python3
""" Prueba """

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
