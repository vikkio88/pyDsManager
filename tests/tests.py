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

    def test_team_generator(self):
        team = self.randomFiller.get_team()
        self.assertIsNot(len(team.players), 0)
        self.assertIsNotNone(team.coach)
        self.assertIsNotNone(team.get_avg_age())
        self.assertIsNotNone(team.get_avg_skill())


if __name__ == '__main__':
    unittest.main()
