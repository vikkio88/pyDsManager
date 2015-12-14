import random


class Randomizer(object):
    @staticmethod
    def bool_on_percentage(percentage=0):
        return random.randint(0, 100) < percentage
