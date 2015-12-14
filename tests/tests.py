import unittest
from lib.models import *
from lib.generator import RandomFiller


class TestGameModels(unittest.TestCase):
    randomFiller = RandomFiller()

    def test_player_generator(self):
        pl = self.randomFiller.get_player()
        self.assertIsInstance(pl, Player)
        self.assertIsNotNone(pl.name)
        self.assertIsNotNone(pl.role)


if __name__ == '__main__':
    unittest.main()
