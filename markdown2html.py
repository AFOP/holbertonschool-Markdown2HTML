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
def md5_lowercase(content):
    md5 = hashlib.md5(content.encode('utf-8')).hexdigest()
    return md5.lower()

def quit_c(content):
    return content.replace('c', '').replace('C', '')

def markdown_to_html(markdown_str):
    html_str = ""
    in_list = False
    in_olist = False
    is_text = False
    for line in markdown_str.split("\n"):
        if "**" in line:
            line_aux = ""
            while "**" in line:
                line_aux += line[:line.index("**")] + "<b>"
                line = line[line.index("**")+2:]
                line_aux += line[:line.index("**")] + "</b>"
                line = line[line.index("**")+2:]
            line_aux += line + ""
            line = line_aux
        if "__" in line:
                line_aux = ""
                while "__" in line:
                    line_aux += line[:line.index("__")] + "<em>"
                    line = line[line.index("__")+2:]
                    line_aux += line[:line.index("__")] + "</em>"
                    line = line[line.index("__")+2:]
                line_aux += line + ""
                line = line_aux
        if "[[" and "]]" in line:
                word_encript = ""
                word_encript = re.sub(r'\[\[(.*?)\]\]', lambda m: md5_lowercase(m.group(1)), line)
                line = word_encript
        if "((" and "))" in line:
            word_encript = ""
            word_encript = re.sub(r'\(\((.*?)\)\)', lambda m: quit_c(m.group(1)), line)
            line = word_encript
        if line.startswith("-"):
            if not in_list:
                html_str += "<ul>\n"
                in_list = True
            li_content = line[2:].strip()
            html_str += f"\t<li>{li_content}</li>\n"
        elif line.startswith("*"):
            if not in_olist:
                html_str += "<ol>\n"
                in_olist = True
            li_content = line[2:].strip()
            html_str += f"\t<li>{li_content}</li>\n"
        elif line.startswith("#"):
            level = min(line.count("#"), 6)
            html_str += f"<h{level}>{line[level+1:].strip()}</h{level}>\n"
        elif line.strip():
            if not is_text:
                html_str += f"<p>\n\t{line}\n"
                is_text = True
            else:
                html_str += f"\t\t<br>\n\t{line}\n"
        else:
            if in_list:
                html_str += "</ul>\n"
                in_list = False
            elif in_olist:
                html_str += "</ol>\n"
                in_olist = False
            elif is_text:
                html_str += "</p>\n"
                is_text = False
            html_str += line
    return html_str

if __name__ == "__main__":
    import sys
    import os.path
    import hashlib
    import re

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
        html = markdown_to_html(md)
        with open(html_file, 'w') as g:
            g.write(html)
    sys.exit(0)
