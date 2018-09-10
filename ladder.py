from player import Player

class Ladder:

    ladder = []

    def __init__(self, players):
        self.ladder = players

    def __repr__(self):
        return str([player.name for player in self.ladder])

    def add_player(self, player):
        self.ladder.append(player)

    def get_player_pos(self, player):
        return self.ladder.index(player)

    def update(self, winner, loser):
        players = self.ladder
        if winner in players and loser in players:
            winner_pos = self.get_player_pos(winner)
            loser_pos = self.get_player_pos(loser)
            del players[winner_pos]
            players.insert(loser_pos, winner)
        elif winner in players and loser not in players:
            self.add_player(loser)
        elif winner not in players and loser in players:
            loser_pos = self.get_player_pos(loser)
            players.insert(loser_pos, winner)
        else:
            self.add_player(winner)
            self.add_player(loser)
