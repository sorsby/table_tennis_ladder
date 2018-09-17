import unittest
from ladder import Ladder
from player import Player
from mocks.printer import Printer

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

    def test_remove_player_not_in_ladder_success_msg(self):
        self.ladder.add_player('p1')
        self.ladder.remove_player('p1')

        expected = "Player 'p1' successfully removed from group 'test_group'."
        self.assertEqual(expected, self.ladder.printer.string)

    def test_remove_player_not_in_ladder(self):
        self.ladder.add_player('p1')
        self.ladder.remove_player('not_in_ladder')

        expected = [self.ladder.get_player('p1')]
        self.assertListEqual(expected, self.ladder.ladder)

    def test_remove_player_not_in_ladder_error_msg(self):
        self.ladder.add_player('p1')
        self.ladder.remove_player('not_in_ladder')

        expected = "ERROR: not_in_ladder is not in the ladder, skipping."
        self.assertEqual(expected, self.ladder.printer.string)

if __name__ == '__main__':
    unittest.main()
