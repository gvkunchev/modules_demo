# Color print demo
from helpers.functions.outputs import color_print

color_print('This is white text')
color_print('This is red text', color='red')
color_print('This is green text', color='green')
color_print('This is blue text', color='blue')


# Indent print demo
from helpers.functions.outputs import indent_print

indent_print('This is indented with 4 spaces.')
indent_print('This is indented with 8 spaces.', indent=8)


# Integer input demo (Using a short import statement)
import helpers
helpers.functions.inputs.int_input('Please enter a whole number.')


# Confirmation input demo (Using a renamed import statement)
import helpers.functions.inputs as input_fun_helpers
result = input_fun_helpers.auto_input('Please confirm or reject Y/n.')
print(f'You said "{result}"')


# Only truthy input arguments demo
from helpers.decorators.filters import truthy_input

@truthy_input
def print_something(*args, **kwargs):
    print(args)
    print(kwargs)

print_something(0, '', 1, {}, name1=1, name2=0.0, name3=False)


# Only string output demo
from helpers import decorators

@decorators.filters.string_output
def print_something(to_print):
    return to_print

print(print_something('String'))
print(print_something({'Not': 'String'}))

# Log input arguments
from helpers.decorators.loggers import logged_input

@logged_input
def do_something(*args, **kwargs):
    pass

do_something(1, 2, name=3)


# Log output result
import helpers

@helpers.decorators.loggers.logged_output
def do_something():
    return 3.14

do_something()


# Color class demo
from helpers.classes.inherit import Color

class Test(Color, int):
    pass

test = Test(42)
test.red()
test.green()
test.blue()


# Logged class demo
from helpers import classes as class_helpers

class Test(class_helpers.inherit.Logged):

    def __init__(self):
        self.name = 'Logged class'

test = Test()
test.name


# Generator class demo
from helpers.classes import generators as gen

class Class1:
    pass

class Class2:
    pass

generator = gen.InheritanceGenerator()
print(generator('StrangeClass', int, Class1, Class2))


# Dynamic Context Manager class demo
from helpers.classes.generators import DynamicContextManager as DynCM

cm = DynCM(enter=lambda *_: print('Start'), exit=lambda *_: print('End'))

with cm:
    print('Inside')
