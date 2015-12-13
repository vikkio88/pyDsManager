from vendors.faker import Faker
from lib.models import Player


class RandomFiller(object):
    faker = None

    def __init__(self, locale='it_IT'):
        self.faker = Faker(locale)

    def get_player(self):
        pl = Player()
        pl.name = self.faker.name()
        return pl
