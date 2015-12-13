from vendors.faker import Faker
from lib.models import Player
import random


class RandomFiller(object):
    faker = None

    def __init__(self, locale='it_IT'):
        self.faker = Faker(locale)

    def get_player(self):
        pl = Player()
        pl.name = self.faker.name()
        pl.surname = self.faker.surname()
        #pl.role =
        return pl
