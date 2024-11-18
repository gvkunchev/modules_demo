from ..functions.outputs import color_print
from helpers.decorators.loggers import logged_output


class Color:

    def red(self):
        color_print(repr(self), color='red')

    def green(self):
        color_print(repr(self), color='green')

    def blue(self):
        color_print(repr(self), color='blue')


class Logged:

    @logged_output
    def __getattribute__(self, name):
        return super().__getattribute__(name)
