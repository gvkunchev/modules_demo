# Color print demo
from helpers.functions.output import color_print

color_print('This is white text')
color_print('This is red text', color='red')
color_print('This is green text', color='green')
color_print('This is blue text', color='blue')


# Indent print demo
from helpers.functions.output import indent_print

indent_print('This is indented with 4 spaces.')
indent_print('This is indented with 8 spaces.', indent=8)

