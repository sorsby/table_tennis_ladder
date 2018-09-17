import unittest
from ladder import Ladder
from player import Player



class TestAddPlayer(unittest.TestCase):

    ladder= Ladder("testing_group")

    def tearDown(self):
        self.ladder.clear()

    def test_add_player(self):
        self.ladder.add_player("Matt")
        expected_ladder = [self.ladder.get_player("Matt")]
        self.assertListEqual(expected_ladder, self.ladder.ladder)

    def test_add_multiple_players(self):
        self.ladder.add_player("player 1")
        self.ladder.add_player("player 2")
        player_1 = self.ladder.get_player("player 1")
        player_2 = self.ladder.get_player("player 2")
        new_ladder = [player_1, player_2]
        self.assertListEqual(new_ladder, self.ladder.ladder)


if __name__ == "__main__":
    unittest.main()