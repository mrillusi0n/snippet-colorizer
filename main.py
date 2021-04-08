##############################################################

import os
import json
import sys

from itertools import starmap
from color_transformer import darken

def load_colors(colorscheme_file):
    with open(colorscheme_file) as scheme:
        return json.load(scheme)

def make_root(json_scheme):
    return ':root {{{}}}'.format(
        ';'.join(starmap('--{}:{}'.format, json_scheme.items()))
    )

def export_css(json_scheme):
    with open(os.path.join(EXPORT_PATH, 'css/scheme.css'), 'w') as export_file:
        export_file.write(make_root(json_scheme))

def render(scheme, snippet):
    colors = load_colors(scheme)
    export_css(colors)

    with open(TEMPLATE) as template:
        html = template.read().format(snippet=snippet, bg_color=darken(colors['bg'], 20))

    with open(os.path.join(EXPORT_PATH, 'index.html'), 'w') as html_file:
        html_file.write(html)

EXPORT_PATH = 'render'
TEMPLATE = 'template.html'

try:
    SCHEME = sys.argv[1]
except:
    SCHEME = 'colors/ayu_mirage.json'

def main():
    with open('code.py') as snippet_file:
        render(SCHEME, snippet_file.read().strip())


if __name__ == '__main__':
    main()
