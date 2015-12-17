from operator import attrgetter


class Team(object):
    name = ""
    nationality = ""
    coach = None
    players = []
    avg_age = None
    avg_skill = None

    def __init__(self, coach, players):
        self.coach = coach
        self.players = players

    def get_avg_age(self):
        if self.avg_age is None:
            tot = 0
            for player in self.players:
                tot += player.age
            self.avg_age = round(tot / len(self.players), 2)
        return self.avg_age

    def get_avg_skill(self):
        if self.avg_skill is None:
            tot = 0
            for player in self.players:
                tot += player.skill
            self.avg_skill = round(tot / len(self.players), 2)
        return self.avg_skill

    def get_players_with_role(self, role):
        result = []
        for player in self.players:
            if player.role == role:
                result.append(player)
        return result

    def get_players_per_role(self):
        result = {}
        for player in self.players:
            if player.role in result:
                result[player.role] += 1
            else:
                result[player.role] = 1
        return result

    def get_players_by_role(self, role):
        return [p for p in self.players if p.role == role]

    def get_best_player_by_role(self, role):
        players_by_role = self.get_players_by_role(role)
        # preferred this to the lambda version, apparently is faster
        return max(players_by_role, key=attrgetter('skill')) if len(players_by_role) > 0 else None
