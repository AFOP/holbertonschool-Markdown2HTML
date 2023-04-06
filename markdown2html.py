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
def markdown_to_html(markdown_str):
    html_str = ""
    in_list = False
    in_olist = False
    is_text = False
    for line in markdown_str.split("\n"):
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
