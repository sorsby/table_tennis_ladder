from player import Player
from htmlify import Htmlify


class Ladder:

    # list of Player objects where each player has a name attribute.
    ladder = []
    ladder_folder = "group_ladders/%s"

    def __init__(self, name, new=True):
        self.players = {}
        self.ladder_filename = name
        players = self.read()

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
        return str([player.name for player in self.ladder])

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

    def update(self, winner, loser):
        players = self.ladder
        if winner in players and loser in players:
            winner_pos = self.get_player_pos(winner)
            loser_pos = self.get_player_pos(loser)
            if winner_pos > loser_pos:
                del players[winner_pos]
                players.insert(loser_pos, winner)
        elif winner in players and loser not in players:
            self.add_player(loser.name)
        elif winner not in players and loser in players:
            loser_pos = self.get_player_pos(loser)
            players.insert(loser_pos, winner)
        else:
            self.add_player(winner.name)
            self.add_player(loser.name)

        print "Leaderboard updated: '%s' beat '%s'." % (
            winner.name, loser.name)
        self.save()

    def save(self):
        filename = self.ladder_folder % self.ladder_filename
        with open(filename, 'w') as f:
            for player in self.ladder:
                f.write(player.name + '\n')

        # put data in format ready for html templating
        html_players = []
        i = 0
        for player in self.ladder:
            i += 1
            html_players.append({'name': player.name, 'rank': i})
        
        Htmlify(html_players, self.ladder_filename).gen_html()

    def read(self):
        filename = self.ladder_folder % self.ladder_filename
        try:
            with open(filename, 'r') as f:
                lines = f.readlines()
                return [line.rstrip('\n') for line in lines]
        except:
            self.save()
