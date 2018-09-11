from ladder import Ladder
from player import Player
import click
from prettytable import PrettyTable

welcome = """
          ,;;;!!!!!;;.
        :!!!!!!!!!!!!!!;    Infinity Works Graduate Scheme 2018
      :!!!!!!!!!!!!!!!!!;       Ash & Matt's Ping Pong Ladder Extravaganza
     ;!!!!!!!!!!!!!!!!!!!;          All Rights Reserved (c) 2018
    ;!!!!!!!!!!!!!!!!!!!!!
    ;!!!!!!!!!!!!!!!!!!!!'
    ;!!!!!!!!!!!!!!!!!!!'       o      .   _______ _______
     :!!!!!!!!!!!!!!!!'         \_ 0     /______//______/|   @_o
      ,!!!!!!!!!!!!!''            /\_,  /______//______/     /\\
   ,;!!!''''''''''               | \    |      ||      |     / |
 .!!!!'
!!!!
"""

champ = """
     ___________
    '._==_==_=_.'
    .-\:      /-.
   | (|:.     |) |
    '-|:.     |-'
      \::.    /     Current Champ: %s
       '::. .'          %s is overwhelmed with a feeling of pride and accomplishment.
         ) (            %s has truly earned the adoration of their peers.
       _.' '._
      `-------`
"""


def pretty_print(ladder):
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
    pretty_print(ladder)

    ladder.update(test_players['Matt'], test_players['Ash'])
    pretty_print(ladder)

    ladder.update(test_players['Dan'], test_players['Matt'])
    pretty_print(ladder)

    add_test_player(test_players, 'James')
    ladder.update(test_players['Dan'], test_players['James'])
    pretty_print(ladder)

    add_test_player(test_players, 'Sandeep')
    ladder.update(test_players['Sandeep'], test_players['James'])
    pretty_print(ladder)

    add_test_player(test_players, 'Sam')
    add_test_player(test_players, 'Pam')
    ladder.update(test_players['Sam'], test_players['Pam'])
    pretty_print(ladder)

    add_test_player(test_players, 'Spam')
    ladder.update(test_players['Dan'], test_players['Spam'])
    pretty_print(ladder)


@click.command()
@click.option('--test', '-t', is_flag=True, help='Run a suite of tests.')
@click.option('--add', '-a', multiple=True, help='Add player(s) to the ladder (multiple players require multiple --add flags).')
@click.option('--update', '-u', nargs=2, help='Update ladder with results of a game e.g. --update WINNER LOSER.')
@click.option('--view', '-v', is_flag=True, help='View the current ladder positions.')
@click.option('--search', '-s', help='Search for a player in the ladder. e.g. --search Ash')
@click.option('--remove', '-r', multiple=True, help='Remove player(s) from the ladder (multiple players require multiple --remove flags).')
@click.option('--champion', '-c', is_flag=True, help="Show the current champion and their pending title trophy.")
def main(test, add, update, view, search, remove, champion):
    """A simple program to view and administrate the IW Table Tennis ladder."""
    ladder = Ladder()
    players = ladder.get_players()

    print welcome

    if test:
        run_tests(players, ladder)
        return

# TODO: Bug present when adding a new player and updating the ladder in the same command.
# TODO: Change add function to create player instance instead of doing it here.
    if add and not update:
        for name in add:
            ladder.add_player(name)
        pretty_print(ladder)

    if update:
        input_game(ladder, update[0], update[1])
        pretty_print(ladder)

    if view:
        pretty_print(ladder)

    if search:
        player = ladder.get_player(search)
        if player:
            print(player.name + " is rank: " +
                  str(ladder.get_player_pos(player) + 1))
        else:
            print "Player not found. Check spelling and try again."

    if remove:
        for name in remove:
            ladder.remove_player(name)
        pretty_print(ladder)

    if champion:
        name = ladder.get_champion().name
        print champ % (name, name, name)


def input_game(ladder, arg0, arg1):
    winner = ladder.get_player(arg0)
    loser = ladder.get_player(arg1)
    if not winner:
        winner = Player(arg0)
    if not loser:
        loser = Player(arg1)
    ladder.update(winner, loser)


if __name__ == '__main__':
    main()
