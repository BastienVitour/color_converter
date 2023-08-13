hex_tab = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]


def rgb_to_hex(r, g, b):
    if -1 < r < 256 and -1 < g < 256 and -1 < b < 256:

        hex_red = hex_tab[r // 16]+hex_tab[r % 16]

        hex_green = hex_tab[g // 16]+hex_tab[g % 16]

        hex_blue = hex_tab[b // 16] + hex_tab[b % 16]

        hex_value = "#" + hex_red+hex_green+hex_blue

        return hex_value

    else:
        print("Invalid values")
        return False


def rgb_to_hsl(r, g, b):
    print(r, g, b)


def hex_to_rgb(r, g, b):
    red = list(r.upper())
    rgb_red = hex_tab.index(red[0]) * 16 + hex_tab.index(red[1])
    green = list(g.upper())
    rgb_green = hex_tab.index(green[0]) * 16 + hex_tab.index(green[1])
    blue = list(b.upper())
    rgb_blue = hex_tab.index(blue[0]) * 16 + hex_tab.index(blue[1])

    rgb_val = "rgb(" + str(rgb_red) + ", " + str(rgb_green) + ", " + str(rgb_blue) + ")"

    return rgb_val


def hex_to_hsl(r, g, b):
    print(r, g, b)


def hsl_to_rgb(h, s, l):
    print(h, s, l)


def hsl_to_hex(h, s, l):
    print(h, s, l)
