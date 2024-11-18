COLORS = {
    'white': '\33[37m',
    'green': '\33[92m',
    'red': '\33[91m',
    'blue': '\33[34m'
}
END = '\033[0m'


def color_print(text, color='white'):
    print(f"{COLORS[color]}{text}{END}")


def indent_print(text, indent=4):
    print(f"{' ' * indent}{text}")
