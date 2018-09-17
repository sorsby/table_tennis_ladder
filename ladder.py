from player import Player
from htmlify import Htmlify
from prettytable import PrettyTable
from persistence import Persistence
from mocks.printer import Printer


class Ladder:

    ladder = []
    ladder_folder = "group_ladders"
    printer = Printer()

    def __init__(self, group_name):
        self.players = {}
        self.ladder_filename = group_name

        # init the persistence object for reading and saving the ladder
        self.file = Persistence(
            self.ladder_folder, self.ladder_filename, self.ladder)
        players = self.file.read()

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
            self.printer.set_string("Player '%s' successfully removed from group '%s'." % (
                name, self.ladder_filename))
            self.printer.prnt()
        else:
            self.printer.set_string("ERROR: %s is not in the ladder, skipping." % name)
            self.printer.prnt()

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

        self.printer.set_string("Leaderboard updated: '%s' beat '%s'." % (
            winner.name, loser.name))
        self.printer.prnt()
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

    def clear(self):
        self.ladder = []
        self.players.clear()
        self.file.delete()
