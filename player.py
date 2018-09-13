class Player:

    def __init__(self, name):
        self.name = name

    def __eq__(self, player):
        if self.name == player.name:
            return True
        return False

    def __ne__(self, player):
        return not self.__eq__(player)