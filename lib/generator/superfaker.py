from faker import Factory
from lib.config.roles import roles
import random


class SuperFaker(object):
    faker = None
    locale = 'it_IT'

    def __init__(self, locale='it_IT'):
        self.faker = Factory.create(locale)
        self.locale = locale

    def name(self):
        return self.faker.name()

    def surname(self):
        return self.faker.last_name()

    def age(self, mn=16, mx=38):
        return random.randint(mn, mx)

    def player_role(self):
        return random.choice(roles)['name']

    def team_name(self):
        return self.faker.city()
