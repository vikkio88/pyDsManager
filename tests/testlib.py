import unittest
from lib.generator import *


class TestGameLibs(unittest.TestCase):
    def test_randomizer(self):
        self.assertFalse(Randomizer.bool_on_percentage())
        self.assertTrue(Randomizer.bool_on_percentage(100))


if __name__ == '__main__':
    unittest.main()
