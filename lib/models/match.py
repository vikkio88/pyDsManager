import random
from lib.generator.randomizer import Randomizer
from .module import Module
from .matchresult import MatchResult


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
                goal_away += ((away_point - home_point) % 6) + self.chance()
                goal_home += self.chance() + self.bonus_home()
            else:
                goal_home += ((home_point - away_point) % 6) + self.chance() + self.bonus_home()
                goal_away += self.chance()
        else:
            goal_home += self.chance() + self.bonus_home()
            goal_away += self.chance()

        goal_home += self.bonus_age(self.homeTeam)
        goal_away += self.bonus_age(self.awayTeam)

        goal_away -= self.bonus_goalkeeper(self.homeTeam)
        goal_home -= self.bonus_goalkeeper(self.awayTeam)

        if Module(self.homeTeam.coach.module).is_offensive():
            goal_home += random.randint(1, 2) if Randomizer.bool_on_percentage(50) else 0
            goal_away += 1 if Randomizer.bool_on_percentage(20) else 0
        if Module(self.awayTeam.coach.module).is_offensive():
            goal_away += random.randint(1, 2) if Randomizer.bool_on_percentage(50) else 0
            goal_home += 1 if Randomizer.bool_on_percentage(20) else 0
        if Module(self.homeTeam.coach.module).is_defensive():
            goal_away -= 1 if Randomizer.bool_on_percentage(30) else 0
        if Module(self.awayTeam.coach.module).is_defensive():
            goal_home -= 1 if Randomizer.bool_on_percentage(30) else 0

        goal_home = int(goal_home)
        goal_away = int(goal_away)
        goal_home = goal_home if goal_home > 0 else 0
        goal_away = goal_away if goal_away > 0 else 0

        return MatchResult(goal_home, goal_away, self.homeTeam, self.awayTeam)

    def bonus_goalkeeper(self, team):
        goalie = team.get_best_player_by_role('GK')
        if goalie is not None:
            return 1 if Randomizer.bool_on_percentage(goalie.skill) else 0
        else:
            return 1 if Randomizer.bool_on_percentage(1) else 0

    def bonus_age(self, team):
        if team.get_avg_age() > 29 or team.get_avg_age() < 24:
            return self.chance()
        return 0

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
