import os

class Persistence:

    def __init__(self, ladder_folder, group_name, ladder):
        self.ladder = ladder
        self.group_name = group_name
        self.ladder_filepath = ladder_folder + '/' + self.group_name

    def read(self):
        try:
            with open(self.ladder_filepath, 'r') as f:
                lines = f.readlines()
                return [line.rstrip('\n') for line in lines]
        except IOError:
            self.save()

    def save(self):
        with open(self.ladder_filepath, 'w') as f:
            for player in self.ladder:
                f.write(player.name + '\n')

    def delete(self):
        try:
            os.remove(self.ladder_filepath)
        except IOError:
            print "ERROR: Attempting to delete a file that doesn't exist: '%s'" % self.group_name
