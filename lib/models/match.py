import random
from lib.generator import Randomizer
from . import Module


class Match(object):
    homeTeam = None
    awayTeam = None

    def __init__(self, home_team, away_team):
        self.homeTeam = home_team
        self.awayTeam = away_team

    def simulate(self):
        home_point = self.homeTeam.get_avg_skill()
        away_point = self.awayTeam.get_avg_skill()

        home_point += self.malus_module(self.homeTeam)
        away_point += self.malus_module(self.awayTeam)
        goal_home = 0
        goal_away = 0
        if Randomizer.bool_on_percentage(80):
            if home_point < away_point:
                goal_away += (away_point - home_point) % 6
                goal_home += self.chance()
                goal_away += self.chance()
                goal_home += self.bonus_home()
            else:
                goal_home += (home_point - away_point) % 6
                goal_away += self.chance()
                goal_home += self.chance()
                goal_home += self.bonus_home()
        else:
            goal_home += self.chance()
            goal_away += self.chance()
            goal_home += self.bonus_home()

        goal_home += self.bonus_age(self.homeTeam)
        goal_away += self.bonus_age(self.awayTeam)

    def bonus_age(self, team):
        if team.get_avg_age() > 29 or team.get_avg_age() < 24:
            return self.chance()

    def malus_module(self, team):
        m = Module(team.coach.module)
        if m.is_applicable_to_list(team.get_players_per_role()):
            return random.randint(1, 10)
        else:
            return -1 * random.randint(1, 10)

    def bonus_home(self):
        return 1 if Randomizer.bool_on_percentage(66) else 0

    def chance(self):
        return random.randint(0, 3)
