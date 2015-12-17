import random
from lib.generator import Randomizer


class Match(object):
    homeTeam = None
    awayTeam = None

    def __init__(self, home_team, away_team):
        self.homeTeam = home_team
        self.awayTeam = away_team

    def simulate(self):
        pass

    def malus_module(self, team, players_per_role):
        pass

    def bonus_home(self):
        return 1 if Randomizer.bool_on_percentage(66) else 0

    def chance(self):
        return random.randint(0, 3)
