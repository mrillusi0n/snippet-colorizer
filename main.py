##############################################################

import json
from itertools import starmap

def load_colors(cs_name):
    with open(cs_name) as scheme:
        return json.load(scheme)

def make_root(json_scheme):
    return ':root {{{}}}'.format(
        ';'.join(starmap('--{}:{}'.format, json_scheme.items()))
    )

def export_css(dest, json_scheme):
    with open(dest, 'w') as export_file:
        export_file.write(make_root(json_scheme))


print(make_root(load_colors('colors/everforest.json')))
export_css('css/scheme.css', load_colors('colors/everforest.json'))

