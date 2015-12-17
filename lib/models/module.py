from lib.config.modules import modules


class Module:
    name = None
    configurations = None

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
