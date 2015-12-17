from .providers import providers
from lib.config.roles import roles
import random


class SuperFaker(object):
    providers = None
    locale = 'it_IT'

    def __init__(self, locale='it_IT'):
        self.providers = providers
        self.locale = locale

    def name(self):
        return random.choice(self.providers[self.locale]['names'])

    def surname(self):
        return random.choice(self.providers[self.locale]['surnames'])

    def age(self, mn=16, mx=38):
        return random.randint(mn, mx)

    def player_role(self):
        return random.choice(roles)['name']

    def team_name(self):
        return random.choice(self.providers[self.locale]['cities'])
