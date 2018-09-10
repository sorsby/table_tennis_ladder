from player import Player


class Ladder:

    # dict of player name keys and associated player objects
    players = {}
    # list of Player objects where each player has a name attribute.
    ladder = []
    ladder_filename = "ladder_standings"

    def __init__(self):
        players = self.read()
        # file not found or empty load some default data for testing
        if not players:
            players = ['Ash', 'Matt', 'Mike', 'Dan', 'Emily']

        for player in players:
            player_object = Player(player)
            self.ladder.append(player_object)
            self.players[player] = player_object

    def __repr__(self):
        return str([player.name for player in self.ladder])

    def add_player(self, player):
        self.ladder.append(player)
        self.save()

    def get_player_pos(self, player):
        return self.ladder.index(player)

    def get_player(self, name):
        try:
            return self.players[name]
        except:
            return None

    def get_players(self):
        return self.players

    def get_rankings(self):
        return self.ladder

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

        self.save()

    def save(self):
        with open(self.ladder_filename, 'w') as f:
            for player in self.ladder:
                name = player.name
                f.write(name + '\n')

    def read(self):
        try:
            with open(self.ladder_filename, 'r') as f:
                lines = f.readlines()
                return [line.rstrip('\n') for line in lines]
        except:
            self.save()
