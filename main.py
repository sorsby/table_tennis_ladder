from ladder import Ladder
from player import Player
import click


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


@click.command()
@click.option('/test;/no-test')
@click.option('--add', '-a')
@click.option('--update', '-u', nargs=2)
def main(test, add, update):
    ladder = Ladder()
    players = ladder.get_players()

    if test:
        run_tests(players, ladder)
        return

    if add:
        ladder.add_player(Player(add))

    if update:
        winner = ladder.get_player(update[0])
        loser = ladder.get_player(update[1])

        if not winner:
            winner = Player(update[0])
        if not loser:
            loser = Player(update[1])

        ladder.update(winner, loser)

    print ladder


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
