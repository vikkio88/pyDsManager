from lib.config.modules import modules
from lib.config.roles import roles


class Module:
    name = None
    configurations = None
    roles_needed = None

    def __init__(self, module_string):
        if module_string in modules:
            self.name = module_string
            self.configurations = modules[module_string]

    def is_offensive(self):
        return self.configurations['character'] == 1

    def is_balanced(self):
        return self.configurations['character'] == 2

    def is_defensive(self):
        return self.configurations['character'] == 4

    def get_roles_needed(self):
        if self.roles_needed is None:
            self.roles_needed = {}
            i = 0
            for role in roles:
                self.roles_needed[role['name']] = self.configurations['roles'][i]
                i += 1
        return self.roles_needed

    def is_applicable_to_team(self, team):
        return self.is_applicable_to_list(team.get_players_per_role())

    def is_applicable_to_list(self, player_list):
        needed = self.get_roles_needed()
        for role in needed:
            if needed[role] > 0 and role not in player_list or needed[role] > player_list[role]:
                return False
        return True

    def roles_missing_team(self, team):
        return self.roles_missing_from_list(team.get_players_per_role())

    def roles_missing_from_list(self, player_list):
        result = {}
        needed = self.get_roles_needed()
        for role in needed:
            if needed[role] > 0 and role not in player_list or needed[role] > player_list[role]:
                n = player_list.get(role, 0)
                result[role] = needed[role] - n
        return result
