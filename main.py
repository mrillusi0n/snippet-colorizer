###########

import json
from itertools import starmap

def load_colors(cs_name):
    with open(cs_name) as scheme:
        return json.load(scheme)

def make_css(json_scheme):
    return '''\
:root {{
{}
}}
'''.format('\n'.join(starmap('\t--{}: {}'.format, json_scheme.items())))

print(make_css(load_colors('colors/everforest.json')))

