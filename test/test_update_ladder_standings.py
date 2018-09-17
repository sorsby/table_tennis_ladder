import unittest
from ladder import Ladder
from player import Player


class TestUpdateLadderStandings(unittest.TestCase):

    ladder = Ladder('test_group')

    def test_both_players_in_ladder_winner_higher_rank(self):
        self.ladder.clear()

        winner = Player('Icarus')
        loser = Player('Ben')

        self.ladder.ladder = [winner, loser]
        self.ladder.update(winner, loser)

        expected_ladder = [winner, loser]
        self.assertListEqual(self.ladder.ladder, expected_ladder)

    def test_both_players_in_ladder_winner_lower_rank(self):
        self.ladder.clear()

        winner = Player('Icarus')
        loser = Player('Ben')

        self.ladder.ladder = [loser, winner]
        self.ladder.update(winner, loser)

        expected_ladder = [winner, loser]
        self.assertListEqual(self.ladder.ladder, expected_ladder)

    def test_winner_in_ladder_loser_not(self):
        self.ladder.clear()
        winner = Player('Icarus')
        loser = Player('Ben')

        self.ladder.ladder = [winner]
        self.ladder.update(winner, loser)

        expected = [winner, loser]
        self.assertListEqual(self.ladder.ladder, expected)

    def test_loser_in_ladder_winner_not(self):
        self.ladder.clear()
        winner = Player('Icarus')
        loser = Player('Ben')

        self.ladder.ladder = [loser]
        self.ladder.update(winner, loser)

        expected = [winner, loser]
        self.assertListEqual(self.ladder.ladder, expected)

    def test_both_not_in_ladder(self):
        self.ladder.clear()
        winner = Player('Icarus')
        loser = Player('Ben')

        self.ladder.ladder = []
        self.ladder.update(winner, loser)

        expected = [winner, loser]
        self.assertListEqual(self.ladder.ladder, expected)


if __name__ == '__main__':
    unittest.main()
