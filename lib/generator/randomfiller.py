from lib.models import Person
from lib.models import Player
from lib.models import Coach
from lib.generator.superfaker import SuperFaker
import random


class RandomFiller(object):
    faker = None

    def __init__(self, locale='it_IT'):
        self.faker = SuperFaker(locale)

    def get_person(self):
        person = Person()
        person.name = self.faker.name()
        person.surname = self.faker.surname()
        person.skill = random.randint(40, 100)
        return person

    def get_player(self):
        pl = Player(self.get_person())
        pl.role = self.faker.player_role()
        pl.age = self.faker.age()
        return pl

    def get_coach(self):
        co = Coach(self.get_person())
        co.age = self.faker.age(38, 70)
        return co
