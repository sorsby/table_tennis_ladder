import unittest
from player import Player
# from ladder import Ladder


class MockLadder:

    ladder = []
    players = {}

    def __init__(self, name):
        self.name = name

    def add_player(self, name):
        if not name in self.players.keys():
            player = Player(name)
            self.ladder.append(player)
            self.players[name] = player

    def get_player_pos(self, player):
        return self.ladder.index(player)

    def update(self, winner, loser):
        if winner not in self.ladder:
            self.add_player(winner.name)

        if loser not in self.ladder:
            self.add_player(loser.name)

        winner_pos = self.get_player_pos(winner)
        loser_pos = self.get_player_pos(loser)
        if winner_pos > loser_pos:
            del self.ladder[winner_pos]
            self.ladder.insert(loser_pos, winner)


class TestUpdateLadderStandings(unittest.TestCase):

    def test_both_players_in_ladder_winner_higher_rank(self):
        ladder = MockLadder('test_group')

        winner = Player('Icarus')
        loser = Player('Ben')

        ladder.ladder = [Player('Dan'), winner, loser]
        ladder.update(winner, loser)

        expected_ladder = [Player('Dan'), winner, loser]
        self.assertListEqual(ladder.ladder, expected_ladder)

    def test_both_players_in_ladder_winner_lower_rank(self):
        ladder = MockLadder('test_group')

        winner = Player('Icarus')
        loser = Player('Ben')

        ladder.ladder = [Player('Dan'), loser, winner]
        ladder.update(winner, loser)

        expected_ladder = [Player('Dan'), winner, loser]
        self.assertListEqual(ladder.ladder, expected_ladder)

    def test_winner_in_ladder_loser_not(self):
        ladder = MockLadder('test_group')

        ladder.add_player('Winner')
        ladder.update(ladder.players['Winner'], Player('Loser'))

        expected = [ladder.players['Winner'], ladder.players['Loser']]
        self.assertListEqual(expected, ladder.ladder)

    def test_loser_in_ladder_winner_not(self):
        ladder = MockLadder('test_group')

        ladder.add_player('Loser')
        ladder.update(Player('Winner'), ladder.players['Loser'])

        expected = [ladder.players['Winner'], ladder.players['Loser']]
        self.assertListEqual(expected, ladder.ladder)

    def test_both_not_in_ladder(self):
        ladder = MockLadder('test_group')

        ladder.update(Player('Winner'), Player('Loser'))

        expected = [ladder.players['Winner'], ladder.players['Loser']]
        self.assertListEqual(expected, ladder.ladder)


if __name__ == '__main__':
    unittest.main()
