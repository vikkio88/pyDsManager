from gameconfig import config
from lib.lazyassconsole import Console
from lib.generator import RandomFiller
from pydsmanager import teams, free_players, match_results


def print_banner():
    print(config['banner'])


def print_menu():
    for menu_entry in config['menu_choice']:
        print("{} . {}".format(menu_entry, config['menu_choice'][menu_entry]))


def check_cmd(cmd):
    if cmd in config['menu_choice']:
        print(config['menu_choice'][cmd])
        if cmd == 'gp':
            generate_player()
        elif cmd == 'ap':
            add_player_to_team()
        elif cmd == 'gt':
            generate_team()
        elif cmd == 'gm':
            generate_match()
    else:
        Console.print("Invalid Command {}".format(cmd), 'r')


def generate_player():
    rnd = RandomFiller()
    player = rnd.get_player(rnd.get_locale())
    print("Player generated {}".format(player))
    free_players.append(player)


def add_player_to_team():
    for player in free_players:
        print(player)


def generate_team():
    pass


def generate_match():
    pass
