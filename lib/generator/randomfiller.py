from lib.models import Person
from lib.models import Player
from lib.models import Coach
from lib.models import Team
from lib.config.locales import locales
from lib.generator.superfaker import SuperFaker
import random


class RandomFiller(object):
    faker = None
    locale = None
    locales = None

    def __init__(self, locale='it_IT'):
        self.locales = locales
        self.change_locale(locale)

    def get_person(self):
        person = Person()
        person.name = self.faker.name()
        person.surname = self.faker.surname()
        person.skill = random.randint(40, 100)
        return person

    def get_player(self, locale=None):
        self.change_locale(locale)
        pl = Player(self.get_person())
        pl.role = self.faker.player_role()
        pl.age = self.faker.age()
        pl.nationality = self.locale
        return pl

    def get_coach(self, locale=None):
        self.change_locale(locale)
        co = Coach(self.get_person())
        co.age = self.faker.age(38, 70)
        co.nationality = self.locale
        return co

    def get_team(self, locale=None):
        self.change_locale(locale)
        players = []
        for _ in range(15):
            players.append(self.get_player())
        te = Team(self.get_coach(), players)
        te.name = self.faker.team_name()
        te.nationality = self.locale
        return te

    def change_locale(self, locale=None):
        if self.locale != locale and locale is not None:
            self.faker = SuperFaker(locale)
            self.locale = locale

    def get_locale(self):
        return self.locales[random.choice(list(self.locales.keys()))]['locale']
