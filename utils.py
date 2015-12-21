from gameconfig import config
from lib.lazyassconsole import Utils
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
    for i, player in enumerate(free_players):
        print("{} . {}".format(i + 1, player))


def add_player_to_team():
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
