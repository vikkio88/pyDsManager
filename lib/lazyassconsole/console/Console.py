from lib.lazyassconsole.console.style.style import Style as St
from lib.lazyassconsole.console.style.styleutils import StyleUtils as Su
from lib.lazyassconsole.console.style.colours import Colours as Co


class Console:
    @staticmethod
    def print_yellow(message):
        print((Co.YELLOW + message + Su.ENDC))

    @staticmethod
    def print_blue(message):
        print((Co.BLUE + message + Su.ENDC))

    @staticmethod
    def print_red(message):
        print((Co.RED + message + Su.ENDC))

    @staticmethod
    def print_green(message):
        print((Co.GREEN + message + Su.ENDC))

    @staticmethod
    def print_pink(message):
        print((Co.PINK + message + Su.ENDC))

    @staticmethod
    def format_colour(message, colour='GREEN'):
        return "{}{}{}".format(Co.GREEN, message, Su.ENDC)

    @staticmethod
    def print(message):
        print(Console.format_colour(message))
