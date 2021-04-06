##############################################################

import json
from itertools import starmap

def load_colors(colorscheme_file):
    with open(colorscheme_file) as scheme:
        return json.load(scheme)

def make_root(json_scheme):
    return ':root {{{}}}'.format(
        ';'.join(starmap('--{}:{}'.format, json_scheme.items()))
    )

def export_css(dest, json_scheme):
    with open(dest, 'w') as export_file:
        export_file.write(make_root(json_scheme))

def render(dest, template, snippet):
    with open(template) as template:
        html = template.read().format(snippet)

    with open(dest, 'w') as html_file:
        html_file.write(html)

def main():
	print(make_root(load_colors('colors/everforest.json')))
	export_css('css/scheme.css', load_colors('colors/everforest.json'))

	with open('code.py') as snippet_file:
		render('index.html', 'template.html', snippet_file.read().strip())


if __name__ == '__main__':
	main()