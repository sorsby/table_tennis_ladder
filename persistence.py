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
        except:
            self.save()

    def save(self):
        with open(self.ladder_filepath, 'w') as f:
            for player in self.ladder:
                f.write(player.name + '\n')

    def delete(self):
        os.remove(self.ladder_filepath)