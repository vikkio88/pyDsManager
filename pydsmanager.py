from lib.generator.randomfiller import RandomFiller
from lib.lazyassconsole import Console
from lib.config.modules import modules
from lib.config.locales import locales
from lib.models import Module
from lib.models import Match

from utils import *

def main():
    print_banner()

    cmd = ''
    while cmd != 'q':
        print_menu()
        cmd = input()
        check_cmd(cmd)


if __name__ == '__main__':
    main()


