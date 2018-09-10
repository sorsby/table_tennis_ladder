class Ladder:

    ladder = []

    def __init__(self, players):
        self.add(players)

    def add(self, players):
        self.ladder.append(players)

    def get_player_pos(self, player):
        return self.ladder.index(player)

    def update_ladder(self, winner, loser):
        players = self.ladder
        pass
