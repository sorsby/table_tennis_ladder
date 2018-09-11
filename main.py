from ladder import Ladder
from player import Player
import click
from prettytable import PrettyTable


def print_ladder(ladder):
    t = PrettyTable(['Name', 'Position'])
    i = 0
    for player in ladder.get_rankings():
        i += 1
        t.add_row([player.name, i])
    print t
    print '\n'
    t.clear()


def add_test_player(players, name):
    players[name] = Player(name)


def run_tests(test_players, ladder):
    ladder.add_player(Player('Malik'))
    print_ladder(ladder)

    ladder.update(test_players['Matt'], test_players['Ash'])
    print_ladder(ladder)

    ladder.update(test_players['Dan'], test_players['Matt'])
    print_ladder(ladder)

    add_test_player(test_players, 'James')
    ladder.update(test_players['Dan'], test_players['James'])
    print_ladder(ladder)

    add_test_player(test_players, 'Sandeep')
    ladder.update(test_players['Sandeep'], test_players['James'])
    print_ladder(ladder)

    add_test_player(test_players, 'Sam')
    add_test_player(test_players, 'Pam')
    ladder.update(test_players['Sam'], test_players['Pam'])
    print_ladder(ladder)

    add_test_player(test_players, 'Spam')
    ladder.update(test_players['Dan'], test_players['Spam'])
    print_ladder(ladder)


@click.command()
@click.option('--test', '-t', is_flag=True, help='Run a suite of tests.')
@click.option('--add', '-a', multiple=True, help='Add player(s) to the ladder (multiple players require multiple --add flags).')
@click.option('--update', '-u', nargs=2, help='Update ladder with results of a game e.g. --update WINNER LOSER.')
@click.option('--view', '-v', is_flag=True, help='View the current ladder positions.')
@click.option('--search', '-s', help='Search for a player in the ladder. e.g. --search Ash')
def main(test, add, update, view, search):
    """A simple program to view and administrate the IW Table Tennis ladder."""
    ladder = Ladder()
    players = ladder.get_players()

    if test:
        run_tests(players, ladder)
        return

# TODO: Bug present when adding a new player and updating the ladder in the same command.
    if add and not update:
        for name in add:
            ladder.add_player(Player(name))

    if update:
        input_game(ladder, update[0], update[1])

    if view:
        print_ladder(ladder)

    if search:
        player = ladder.get_player(search)
        if player:
            print(player.name + " is rank: " +
                  str(ladder.get_player_pos(player) + 1))


def input_game(ladder, arg0, arg1):
    winner = ladder.get_player(arg0)
    loser = ladder.get_player(arg1)
    if not winner:
        winner = Player(arg0)
    if not loser:
        loser = Player(arg1)
    ladder.update(winner, loser)


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
