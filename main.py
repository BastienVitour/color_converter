from functions import *

print("Choose a color type")
print("1 : rgb")
print("2 : hex")
print("3 : hsl")

color_type = int(input())

match color_type:
    case 1:
        print("You chose rgb")
        #red = int(input("Red value : "))
        #green = int(input("Green value : "))
        #blue = int(input("Blue value : "))
        value = input("Value : ")
        hex_val = rgb_to_hex(value)
        hsl_val = rgb_to_hsl(value)

        print(f'{value} => #{hex_val[0]}{hex_val[1]}{hex_val[2]}')
        print(f'{value} => hsl({hsl_val[0]}°, {hsl_val[1]}%, {hsl_val[2]}%)')

    case 2:
        print("You chose hex")
        #red = input("Red value : ")
        #green = input("Green value : ")
        #blue = input("Blue value : ")
        value = input("Value : ")
        rgb_val = hex_to_rgb(value)
        hsl_val = hex_to_hsl(value)

        print(f'{value} => rgb({rgb_val[0]}, {rgb_val[1]}, {rgb_val[2]})')
        print(f'{value} => hsl({hsl_val[0]}, {hsl_val[1]}, {hsl_val[2]})')

    case 3:
        print("You chose hsl")
        hue = float(input("Hue value : "))
        saturation = float(input("Saturation value : "))
        lightness = float(input("Lightness value : "))
        rgb_val = hsl_to_rgb(hue, saturation, lightness)
        hex_val = hsl_to_hex(hue, saturation, lightness)

        print(f'hsl({hue}, {saturation}, {lightness}) => rgb({rgb_val[0]}, {rgb_val[1]}, {rgb_val[2]})')
        print(f'hsl({hue}, {saturation}, {lightness}) => #{hex_val[0]}{hex_val[1]}{hex_val[2]}')
