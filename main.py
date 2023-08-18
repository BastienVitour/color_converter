from converter_functions import *
from cleaners_and_checkers import *

print("Choose a color type")
print("1 : rgb")
print("2 : hex")
print("3 : hsl")

color_type = int(input())

match color_type:
    case 1:
        print("You chose rgb")
        value = input("Value : ")
        if rgb_checker(value):
            hex_val = rgb_to_hex(value)
            hsl_val = rgb_to_hsl(value)

            print(f'{value} => #{hex_val[0]}{hex_val[1]}{hex_val[2]}')
            print(f'{value} => hsl({hsl_val[0]}°, {hsl_val[1]}%, {hsl_val[2]}%)')
        else:
            print('Valeur invalide')

    case 2:
        print("You chose hex")
        value = input("Value : ")
        if hex_checker(value):
            rgb_val = hex_to_rgb(value)
            hsl_val = hex_to_hsl(value)

            print(f'{value} => rgb({rgb_val[0]}, {rgb_val[1]}, {rgb_val[2]})')
            print(f'{value} => hsl({hsl_val[0]}, {hsl_val[1]}, {hsl_val[2]})')
        else:
            print('Valeur invalide')

    case 3:
        print("You chose hsl")
        value = input("Value : ")
        if hsl_checker(value):
            rgb_val = hsl_to_rgb(value)
            hex_val = hsl_to_hex(value)

            print(f'{value} => rgb({rgb_val[0]}, {rgb_val[1]}, {rgb_val[2]})')
            print(f'{value} => #{hex_val[0]}{hex_val[1]}{hex_val[2]}')
        else:
            print("Valeur invalide")
