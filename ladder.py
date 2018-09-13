from player import Player
from htmlify import Htmlify
from prettytable import PrettyTable
from persistence import Persistence


class Ladder:

    # list of Player objects where each player has a name attribute.
    ladder = []
    ladder_folder = "group_ladders"

    def __init__(self, name, new=True):
        self.players = {}
        self.ladder_filename = name

        self.file = Persistence(
            self.ladder_folder, self.ladder_filename, self.ladder)
        players = self.file.read()

        # file not found or empty load some default data for testing
        if not players and not new:
            self.players['Ash'] = Player('Ash')
            self.players['Matt'] = Player('Matt')
            self.players['Mike'] = Player('Dan')
            self.players['Dan'] = Player('Dan')
            self.players['Emily'] = Player('Emily')
            players = ['Ash', 'Matt', 'Mike', 'Dan', 'Emily']
            self.save()

        if players:
            for player in players:
                player_object = Player(player)
                self.ladder.append(player_object)
                self.players[player] = player_object

    def __repr__(self):
        t = PrettyTable(['Name', 'Position'])
        i = 0
        for player in self.get_rankings():
            i += 1
            t.add_row([player.name, i])
        message = "Viewing ladder rankings for '%s' group." % self.ladder_filename
        return message + '\n' + t.get_string() + '\n'
        # return str([player.name for player in self.ladder])

    def add_player(self, name):
        if not name in self.players.keys():
            player = Player(name)
            self.ladder.append(player)
            self.players[name] = player
            self.save()
            print "Player '%s' successfully added to group '%s'." % (
                name, self.ladder_filename)
        else:
            print "ERROR: %s already in the ladder, skipping." % name

    def remove_player(self, name):
        if name in self.players.keys():
            player = self.get_player(name)
            self.ladder.remove(player)
            del self.players[name]

            self.save()
            print "Player '%s' successfully removed from group '%s'." % (
                name, self.ladder_filename)
        else:
            print "ERROR: %s is not in the ladder, skipping." % name

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

        print "Leaderboard updated: '%s' beat '%s'." % (
            winner.name, loser.name)
        self.save()

    def save(self):
        self.file.save()
        Htmlify(self.ladder_filename, self.ladder).gen_html()

    def read(self):
        self.file.read()

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

    def get_champion(self):
        return self.ladder[0]
