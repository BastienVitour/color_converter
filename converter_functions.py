from cleaners_and_checkers import *

hex_tab = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]


def rgb_to_hex(value):
    """
    Fonction pour passer d'une couleur au format rgb à une couleur au format hexadécimal
    :param value: la valeur rgb sous forme d'un string, qui sera nettoyée par la fonction clean_rgb_value
    :return: les valeurs au format hexadécimal
    """

    vals = clean_rgb_value(value)

    r = int(vals[0])
    g = int(vals[1])
    b = int(vals[2])

    if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
        exit("Invalid value(s)")

    hex_red = hex_tab[r // 16]+hex_tab[r % 16]

    hex_green = hex_tab[g // 16]+hex_tab[g % 16]

    hex_blue = hex_tab[b // 16] + hex_tab[b % 16]

    return [hex_red, hex_green, hex_blue]


def rgb_to_hsl(value):
    """
    Fonction pour passer d'une couleur au format rgb à une couleur au format hsl
    :param value: la valeur rgb sous forme d'un string, qui sera nettoyée par la fonction clean_rgb_value
    :return: les valeurs au format hsl
    """

    vals = clean_rgb_value(value)

    r = int(vals[0])
    g = int(vals[1])
    b = int(vals[2])

    if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
        exit("Invalid value(s)")

    red = r / 255
    green = g / 255
    blue = b / 255
    max_val = max(red, green, blue)
    min_val = min(red, green, blue)
    d = max_val - min_val

    lightness = (max_val + min_val) / 2

    saturation = d / (1 - abs(2 * lightness - 1)) if lightness != 0 else 0

    hue = 0

    if d == 0:
        hue = 0
    elif max_val == red:
        segment = (green - blue) / d
        shift = 0 / 60
        if segment < 0:
            shift = 360 / 60
        hue = segment + shift
    elif max_val == green:
        segment = (blue - red) / d
        shift = 120 / 60
        hue = segment + shift
    elif max_val == blue:
        segment = (red - green) / d
        shift = 240 / 60
        hue = segment + shift

    hue = round(hue * 60, 1)

    saturation = round(saturation * 100, 1)
    lightness = round(lightness * 100, 1)

    return [str(hue), str(saturation), str(lightness)]


def hex_to_rgb(value):
    """
    Fonction pour passer d'une couleur au format hexadécimal à une couleur au format rgb
    :param value: la valeur hex sous forme d'un string, qui sera nettoyée par la fonction clean_hex_value
    :return: les valeurs au format rgb
    """

    vals = clean_hex_value(value)

    r = vals[0]
    g = vals[1]
    b = vals[2]

    red = list(r.upper())
    rgb_red = hex_tab.index(red[0]) * 16 + hex_tab.index(red[1])
    green = list(g.upper())
    rgb_green = hex_tab.index(green[0]) * 16 + hex_tab.index(green[1])
    blue = list(b.upper())
    rgb_blue = hex_tab.index(blue[0]) * 16 + hex_tab.index(blue[1])

    return [rgb_red, rgb_green, rgb_blue]


def hex_to_hsl(value):
    """
    Fonction pour passer d'une couleur au format hexadécimal à une couleur au format hsl
    :param value: la valeur hex sous forme d'un string, qui sera nettoyée par la fonction clean_hex_value
    :return: les valeurs au format hsl
    """

    rgb_vals = hex_to_rgb(value)

    return rgb_to_hsl(f'rgb({rgb_vals[0]}, {rgb_vals[1]}, {rgb_vals[2]})')


def hsl_to_rgb(value):
    """
    Fonction pour passer d'une couleur au format hsl à une couleur au format rgb
    :param value: la valeur hsl sous forme d'un string, qui sera nettoyée par la fonction clean_hsl_value
    :return: les valeurs au format rgb
    """

    vals = clean_hsl_value(value)

    h = vals[0]
    s = vals[1]
    li = vals[2]

    d = (s / 100) * (1 - abs(2 * (li / 100) - 1))

    x = d * (1 - abs((h / 60) % 2 - 1))

    m = (li / 100) - d / 2

    # r = g = b = 0

    if 0 <= h < 60:
        r, g, b = d, x, 0
    if 60 <= h < 120:
        r, g, b = x, d, 0
    if 120 <= h < 180:
        r, g, b = 0, d, x
    if 180 <= h < 240:
        r, g, b = 0, x, d
    if 240 <= h < 300:
        r, g, b = x, 0, d
    if 300 <= h < 360:
        r, g, b = d, 0, x

    red = (r + m) * 255
    green = (g + m) * 255
    blue = (b + m) * 255

    return [int(round(red)), int(round(green)), int(round(blue))]


def hsl_to_hex(value):
    """
    Fonction pour passer d'une couleur au format hsl à une couleur au format hexadécimal
    :param value: la valeur hsl sous forme d'un string, qui sera nettoyée par la fonction clean_hsl_value
    :return: les valeurs au format hexadécimal
    """

    rgb_vals = hsl_to_rgb(value)

    return rgb_to_hex(f'rgb({rgb_vals[0]}, {rgb_vals[1]}, {rgb_vals[2]})')
