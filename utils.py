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
        elif cmd == 'sp':
            show_free_players()
        elif cmd == 'st':
            show_teams()
    else:
        Console.print("Invalid Command {}".format(cmd), 'r')


def generate_player():
    rnd = RandomFiller()
    player = rnd.get_player(rnd.get_locale())
    print("Player generated {}".format(player))
    free_players.append(player)


def show_free_players():
    for player in free_players:
        print(player)


def add_player_to_team():
    pass


def generate_team():
    rnd = RandomFiller()
    team = rnd.get_team(rnd.get_locale())
    print("team: {} ({}) generated".format(team.name, team.nationality))
    teams.append(team)


def show_teams():
    if len(teams) > 0:
        print("Which team? 1/{}".format(len(teams)))
        i = 1
        for team in teams:
            print("{}. {} ({})".format(i, team.name, team.nationality))
            i += 1
        index = int(input())
        index -= 1
        if len(teams) > index > -1:
            team = teams[index]
            print("{}".format(team.name))
            print("nation: {}".format(team.nationality))
            print("coach {}".format(team.coach))
            print("avgSkill: {}".format(team.get_avg_skill()))
            print("avgAge: {}".format(team.get_avg_age()))
            print("Players:")
            for player in team.players:
                print("{}".format(player))


def generate_match():
    pass
