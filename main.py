from functions import *

print("Choose a color type")
print("1 : rgb")
print("2 : hex")
print("3 : hsl")

color_type = int(input())

match color_type:
    case 1:
        print("You chose rgb")
        red = int(input("Red value : "))
        green = int(input("Green value : "))
        blue = int(input("Blue value : "))
        hex_val = rgb_to_hex(red, green, blue)
        hsl_val = rgb_to_hsl(red, green, blue)

        print(f'rgb({red}, {green}, {blue}) => {hex_val}')
        print(f'rgb({red}, {green}, {blue}) => {hsl_val}')
        # rgb_to_hsl(red, green, blue)
    case 2:
        print("You chose hex")
        red = input("Red value : ")
        green = input("Green value : ")
        blue = input("Blue value : ")
        rgb_val = hex_to_rgb(red, green, blue)

        print(f'#{red.upper()}{green.upper()}{blue.upper()} => {rgb_val}')
        # hex_to_hsl(red, green, blue)

    case 3:
        print("You chose hsl")
        hue = int(input("Hue value : "))
        saturation = int(input("Saturation value : "))
        lightness = int(input("Lightness value : "))
        hsl_to_rgb(hue, saturation, lightness)
        hsl_to_hex(hue, saturation, lightness)
