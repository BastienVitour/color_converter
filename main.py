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

        print(f'rgb({red}, {green}, {blue}) => #{hex_val[0]}{hex_val[1]}{hex_val[2]}')
        print(f'rgb({red}, {green}, {blue}) => hsl({hsl_val[0]}°, {hsl_val[1]}%, {hsl_val[2]}%)')

    case 2:
        print("You chose hex")
        red = input("Red value : ")
        green = input("Green value : ")
        blue = input("Blue value : ")
        rgb_val = hex_to_rgb(red, green, blue)
        hsl_val = hex_to_hsl(red, green, blue)

        print(f'#{red.upper()}{green.upper()}{blue.upper()} => rgb({rgb_val[0]}, {rgb_val[1]}, {rgb_val[2]})')
        print(f'#{red.upper()}{green.upper()}{blue.upper()} => hsl({hsl_val[0]}, {hsl_val[1]}, {hsl_val[2]})')

    case 3:
        print("You chose hsl")
        hue = float(input("Hue value : "))
        saturation = float(input("Saturation value : "))
        lightness = float(input("Lightness value : "))
        rgb_val = hsl_to_rgb(hue, saturation, lightness)
        hex_val = hsl_to_hex(hue, saturation, lightness)

        print(f'hsl({hue}, {saturation}, {lightness}) => rgb({rgb_val[0]}, {rgb_val[1]}, {rgb_val[2]})')
        print(f'hsl({hue}, {saturation}, {lightness}) => #{hex_val[0]}{hex_val[1]}{hex_val[2]}')
