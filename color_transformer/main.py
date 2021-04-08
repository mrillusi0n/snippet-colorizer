################################

import colorsys
from operator import mul

def hex_to_rgbf(hex_color):
    return tuple(int(x) / 255 for x in bytes.fromhex(hex_color[1:]))

def rgb_to_hex(rgb_values):
    return hex(int.from_bytes(bytes(rgb_values), byteorder='big'))[2:]

def rgbf_to_rgb(rgbf_values):
    return tuple(map(round, map(mul, rgbf_values, [255] * 3)))

def rgbf_to_hsv(rgbf_values):
    return colorsys.rgb_to_hsv(*rgbf_values)

def hsv_to_hex(hsv_values):
    return rgb_to_hex(rgbf_to_rgb(colorsys.hsv_to_rgb(*hsv_values)))

def _darken(hsv_values, amount):
    h, s, v = hsv_values
    v *= 1 - amount / 100

    return h, s, v

def darken(hex_color, amount):
    return hsv_to_hex(_darken(colorsys.rgb_to_hsv(*hex_to_rgbf(hex_color)), amount))

if __name__ == '__main__':
    rgbf_pink = hex_to_rgbf('ff88ee')
    hsv_pink = rgbf_to_hsv(rgbf_pink)
    rgb_pink = rgbf_to_rgb(rgbf_pink)
    hex_pink = rgb_to_hex(rgb_pink)

    # print(rgb_pink)
    # print(hsv_pink)
    # print(rgb_pink)
    # print(hex_pink)

    print(darken(darken(hex_pink, 10), 10))
