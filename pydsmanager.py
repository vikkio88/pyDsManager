from utils import *
from gamecmd import GameCmd

teams = []
free_players = []
match_results = []


def main():
    print_banner()
    GameCmd().cmdloop()


if __name__ == '__main__':
    main()
