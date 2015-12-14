from lib.lazyassconsole.console.style.style import Style as St
from lib.lazyassconsole.console.style.styleutils import StyleUtils as Su
from lib.lazyassconsole.console.style.colours import Colours as Co


class Console:
    @staticmethod
    def print(message, color=None):
        if not color:
            print(message)
        else:
            print(Co.BLUE + message + Su.ENDC)
