from utils import *

teams = []
free_players = []
match_results = []


def main():
    print_banner()

    cmd = ''
    while cmd != 'q':
        print_menu()
        cmd = input()
        check_cmd(cmd)


if __name__ == '__main__':
    main()
