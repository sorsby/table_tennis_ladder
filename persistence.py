import os

class Persistence:

    def __init__(self, ladder_folder, group_name, ladder):
        self.ladder = ladder
        self.group_name = group_name
        self.ladder_folder = ladder_folder
        self.ladder_filepath = ladder_folder + '/' + self.group_name

    def read(self):
        try:
            with open(self.ladder_filepath, 'r') as f:
                lines = f.readlines()
                return [line.rstrip('\n') for line in lines]
        except:
            self.save()

    def save(self):
        try:
            with open(self.ladder_filepath, 'w') as f:
                for player in self.ladder:
                    f.write(player.name + '\n')
        except IOError:
            os.mkdir(self.ladder_folder)
            self.save()