def rgb_to_hex(r, g, b):
    if -1 < r < 256 and -1 < g < 256 and -1 < b < 256:
        print(r, g, b)
        print("red")
        print(r / 16)
        print(r // 16)
        print(r % 16)
        print("green")
        print(g / 16)
        print(g // 16)
        print(g % 16)
        print("blue")
        print(b / 16)
        print(b // 16)
        print(b % 16)
    else:
        print("Invalid values")


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
