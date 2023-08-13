hex_tab = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]


def rgb_to_hex(r, g, b):
    if -1 < r < 256 and -1 < g < 256 and -1 < b < 256:

        hex_red = hex_tab[r // 16]+hex_tab[r % 16]

        hex_green = hex_tab[g // 16]+hex_tab[g % 16]

        hex_blue = hex_tab[b // 16] + hex_tab[b % 16]

        hex_value = "#"+hex_red+hex_green+hex_blue

        return hex_value

    else:
        print("Invalid values");
        return False


def rgb_to_hsl(r, g, b):
    print(r, g, b)


def hex_to_rgb(r, g, b):
    print(r, g, b)


def hex_to_hsl(r, g, b):
    print(r, g, b)


def hsl_to_rgb(h, s, l):
    print(h, s, l)


def hsl_to_hex(h, s, l):
    print(h, s, l)
