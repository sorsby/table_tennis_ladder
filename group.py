from ladder import Ladder


class Group:

    '''
    Represents a group ladder/leaderboard.

    Arguments:
    name - name of the group leaderboard.
    ladder - instance of Ladder which stores leaderboard information for group.
    '''

    def __init__(self, name, test):
        self.name = name
        self.ladder = Ladder(name, not test)

    def get_ladder(self):
        return self.ladder

    def get_name(self):
        return self.name
