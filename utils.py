from gameconfig import config
from lib.lazyassconsole import Utils
from lib.lazyassconsole import Console
from lib.generator import RandomFiller
from pydsmanager import teams, free_players, match_results


def print_banner():
    print(config['banner'])


def generate_player():
    rnd = RandomFiller()
    player = rnd.get_player(rnd.get_locale())
    print("Player generated {}".format(player))
    free_players.append(player)


def show_free_players():
    if len(free_players) > 0:
        for i, player in enumerate(free_players):
            print("{} . {}".format(i + 1, player))
    else:
        Console.print('No free players available', 'r')


def add_player_to_team():
    if len(free_players) < 1 or len(teams) < 1:
        Console.print("Not enough players or teams generated")
    else:
        show_free_players()
        player = Utils.choose_one_from_list(free_players)
        show_teams()
        team = Utils.choose_one_from_list(teams)
        team.add_player(player)
        free_players.remove(player)


def generate_team():
    rnd = RandomFiller()
    team = rnd.get_team(rnd.get_locale())
    print("team: {} ({}) generated".format(team.name, team.nationality))
    teams.append(team)


def show_teams():
    if len(teams) > 0:
        print("Team List:")
        for i, team in enumerate(teams):
            print("{}. {} ({})".format(i + 1, team.name, team.nationality))
        team = Utils.choose_one_from_list(teams)
        print(team)
        print("Players:")
        for player in team.players:
            print("{}".format(player))
    else:
        Console.print('No teams available', 'r')


def generate_match():
    pass
