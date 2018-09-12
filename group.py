class Group:
"""
Represents a group ladder/leaderboard.

Arguments:
name - name of the group leaderboard.
ladder - instance of Ladder which stores leaderboard information for group.
"""
    
    def __init__(self, name, ladder):
        self.name = name
        self.ladder = ladder
