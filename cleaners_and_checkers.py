import re


def hex_checker(value):
    """
    Fonction pour vérifier qu'un string est bien au format d'une couleur hexadécimale (#FFFFFF ou #FFF)
    :param value: le string qui sera analysé
    :return: vrai si le string est au bon format, faux sinon
    """
    reg = r"^#[0-9A-F]{6}$|^#[0-9A-F]{3}$"

    if re.match(reg, value):
        return True

    return False


def rgb_checker(value):
    """
    Fonction pour vérifier qu'un string est bien au format d'une couleur rgb (rgb(255, 255, 255))
    :param value: le string qui sera analysé
    :return: vrai si le string est au bon format, faux sinon
    """

    reg = r"^rgb\(\d{1,3}, ?\d{1,3}, ?\d{1,3}\)$"

    if re.match(reg, value):
        return True

    return False


def hsl_checker(value):
    """
    Fonction pour vérifier qu'un string est bien au format d'une couleur hsl (hsl(0, 100%, 50%))
    :param value: le string qui sera analysé
    :return: vrai si le string est au bon format, faux sinon
    """

    reg = r"^hsl\((?:\d{1,3}(?:\.\d{1})?), ?(?:\d{1,3}(?:\.\d{1})?)%, ?(?:\d{1,3}(?:\.\d{1})?)%\)$"

    if re.match(reg, value):
        return True

    return False


def clean_hex_value(value):
    """
    Fonction pour récupérer les valeurs d'un string au format d'une couleur hexadécimale
    :param value: le string à modifier
    :return: les valeurs r, g, b au format hexadécimal
    """

    string = value.replace('#', '')

    if len(string) == 3:
        red = string[0] + string[0]
        green = string[1] + string[1]
        blue = string[2] + string[2]
    else:
        red = string[0:2]
        green = string[2:4]
        blue = string[4:6]

    return [red, green, blue]


def clean_rgb_value(value):
    """
    Fonction pour récupérer les valeurs d'un string au format d'une couleur rgb
    :param value: le string à modifier
    :return: les valeurs r, g, b
    """

    values = value[4:].replace(')', '').split(', ')

    return [values[0], values[1], values[2]]


def clean_hsl_value(value):
    """
    Fonction pour récupérer les valeurs d'un string au format d'une couleur hsl
    :param value: le string à modifier
    :return: les valeurs h, s, l
    """

    values = value[4:].replace(')', '').replace('%', '').split(', ')

    return [float(values[0]), float(values[1]), float(values[2])]
