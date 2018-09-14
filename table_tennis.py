import click

from group import Group
from ladder import Ladder
from player import Player
import validation

welcome = r"""
          ,;;;!!!!!;;.
        :!!!!!!!!!!!!!!;    Infinity Works Graduate Scheme 2018
      :!!!!!!!!!!!!!!!!!;       Ash & Matt's Ping Pong Ladder Extravaganza
     ;!!!!!!!!!!!!!!!!!!!;          All Rights Reserved (c) 2018
    ;!!!!!!!!!!!!!!!!!!!!!
    ;!!!!!!!!!!!!!!!!!!!!'
    ;!!!!!!!!!!!!!!!!!!!'       o      .  _______ _______
     :!!!!!!!!!!!!!!!!'         \_ 0     /______//______/|   @_o
      ,!!!!!!!!!!!!!''            /\_,  /______//______/     /\
   ,;!!!''''''''''               | \    |      ||      |     / |
 .!!!!'
!!!!
"""

champ = r"""
  ___________
 '._==_==_=_.'
 .-\:      /-.
| (|:.     |) |
 '-|:.     |-'     Current Champ: %s !!!
   \::.    /
    '::. .'          %s is overwhelmed with a feeling of pride and accomplishment.
      ) (            %s has truly earned the adoration of his/her peers.
    _.' '._
   `-------`
"""


@click.command()
@click.argument('group')
@click.option('--new', '-n', is_flag=True, help='Flag to create new group ladders.')
@click.option('--add', '-a', multiple=True, help='Add player(s) to the ladder (multiple players require multiple --add flags).')
@click.option('--update', '-u', nargs=2, help='Update ladder with results of a game e.g. --update WINNER LOSER.')
@click.option('--view', '-v', is_flag=True, help='View the current ladder positions.')
@click.option('--remove', '-r', multiple=True, help='Remove player(s) from the ladder (multiple players require multiple --remove flags).')
@click.option('--champion', '-c', is_flag=True, help="Show the current champion and their pending title trophy.")
def main(group,
         new, add, update, view, remove, champion):
    """A simple program to view and administrate the IW Table Tennis ladder.

        Provide a GROUP name and use the options listed below to interact with the system."""

    print welcome

    if new and not update:
        create_group(group)
        return

    # read group namme argument from command line and get group
    cur_group = get_group(group)
    if not cur_group:
        return

    group_ladder = cur_group.get_ladder()
    print_ladder = True

    if add and validation.data_validation(add):
        for name in add:
            group_ladder.add_player(name)
    if remove:
        for name in remove:
            group_ladder.remove_player(name)
    if champion:
        name = group_ladder.get_champion().name
        print champ % (name, name, name)
        print_ladder = False
    if update and (validation.data_validation(update[0]) and validation.data_validation(update[1])):
        winner_name = update[0]
        loser_name = update[1]
        input_game(group_ladder, winner_name, loser_name)

    if print_ladder or view:
        print group_ladder


def input_game(ladder, winner_name, loser_name):
    winner = ladder.get_player(winner_name)
    loser = ladder.get_player(loser_name)
    if not winner:
        winner = Player(winner_name)
    if not loser:
        loser = Player(loser_name)
    ladder.update(winner, loser)


# TODO: Check that group doesn't already exist
def create_group(name):
    new_group = Group(name)
    new_group.ladder.save()
    print "Successfully added new group ladder: '%s'." % name


def get_group(name):
    try:
        return Group(name)
    except:
        print "ERROR: Group with name '%s' does not exist! Check spelling and try again." % name
        return None


if __name__ == '__main__':
    main()
