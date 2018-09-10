from ladder import Ladder
from player import Player


def add_test_player(players, name):
    players[name] = Player(name)


def run_tests(test_players, ladder):
    ladder.add_player(Player('Malik'))
    print ladder

    ladder.update(test_players['Matt'], test_players['Ash'])
    print ladder

    ladder.update(test_players['Dan'], test_players['Matt'])
    print ladder

    add_test_player(test_players, 'James')
    ladder.update(test_players['Dan'], test_players['James'])
    print ladder

    add_test_player(test_players, 'Sandeep')
    ladder.update(test_players['Sandeep'], test_players['James'])
    print ladder

    add_test_player(test_players, 'Sam')
    add_test_player(test_players, 'Pam')
    ladder.update(test_players['Sam'], test_players['Pam'])
    print ladder


def main():
    ladder = Ladder()
    test_players = ladder.get_players()
    print ladder

    run_tests(test_players, ladder)


'''
Earlier test code.
def main():
    test_players = ['Ash', 'Matt', 'Mike', 'Dan', 'Emily']
    ladder = Ladder(test_players)
    print ladder

    ladder.add_player('Malik')
    print ladder

    ladder.update('Matt', 'Ash')
    print ladder

    ladder.update('Dan', 'Matt')
    print ladder

    ladder.update('Dan', 'James')
    print ladder

    ladder.update('Sandeep', 'James')
    print ladder

    ladder.update('Sam', 'Pam')
    print ladder
'''


if __name__ == '__main__':
    main()
