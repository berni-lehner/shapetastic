import re
import matplotlib.colors as mcolors

def is_hex_color(color):
    # Regular expression pattern for hexadecimal color value
    hex_color_pattern = r'^#(?:[0-9a-fA-F]{3}){1,2}$'

    # Check if the color string matches the pattern
    return re.match(hex_color_pattern, color) is not None


def hex_to_rgba(hex_color):
    # Remove "#" if present and extract RGB and alpha components
    hex_color = hex_color.lstrip('#')

    rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    # Check if alpha value is present, default to 255 if not
    alpha = int(hex_color[6:8], 16) if len(hex_color)==8 else 255

    # Normalize values to the range [0, 1]
    r, g, b = [val/255 for val in rgb]
    # TODO: merge alpah with rgb
    alpha = alpha/255

    return r, g, b, alpha


def unify_color(color):
    if isinstance(color, str) and is_hex_color(color):
        color = hex_to_rgba(color)
    elif isinstance(color, str):
        color = mcolors.to_rgba(color)

    return color


def interpolate_color(color1, color2):
    color1 = unify_color(color1)
    color2 = unify_color(color2)

    result = [(c1+c2)/2 for c1, c2 in zip(color1, color2)]

    return result