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
                print(role['name'], self.configurations['roles'][i])
                self.roles_needed[role['name']] = self.configurations['roles'][i]
                i += 1
        return self.roles_needed
