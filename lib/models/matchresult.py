class MatchResult(object):
    goalHome = 0
    goalAway = 0
    homeTeam = None
    awayTeam = None

    def __init__(self, goal_home, goal_away, team_home, team_away):
        self.goalHome = goal_home
        self.goalAway = goal_away
        self.homeTeam = team_home
        self.awayTeam = team_away

    def __str__(self):
        return "{} - {}  {}-{}".format(self.homeTeam.name, self.awayTeam.name, self.goalHome, self.goalAway)
