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

print(make_root(load_colors('colors/everforest.json')))

