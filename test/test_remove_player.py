import unittest
from ladder import Ladder
from player import Player

class TestRemovePlayer(unittest.TestCase):

    ladder = Ladder('test_group')

    def tearDown(self):
        self.ladder.clear()

    def test_remove_player_in_ladder(self):
        self.ladder.add_player('p1')
        self.ladder.add_player('p2')
        self.ladder.remove_player('p1')

        expected = [self.ladder.get_player('p2')]
        self.assertListEqual(expected, self.ladder.ladder)

    def test_remove_player_not_in_ladder(self):
        self.ladder.add_player('p1')
        self.ladder.remove_player('not_in_ladder')

        expected = [self.ladder.get_player('p1')]
        self.assertListEqual(expected, self.ladder.ladder)

    def test_remove_player_not_in_ladder_error_msg(self):
        self.ladder.add_player('p1')
        self.ladder.remove_player('not_in_ladder')

if __name__ == '__main__':
    unittest.main()
