players = []


def add_player(name):
    players.append(name)


def get_player_pos(name):
    return players.index(name)


#use score as input to determine the winner
def update_ladder(winner, loser):
    global players
    if winner in players:
        if loser in players:
            # both in ladder
            winner_pos = get_player_pos(winner)
            loser_pos = get_player_pos(loser)
            del players[winner_pos]
            players.insert(loser_pos, winner)
        else:
            # loser not in ladder
            players.append(loser)
    else:
        if loser in players:
            # winner not in ladder, loser in ladder
            loser_pos = get_player_pos(loser)
            players.insert(loser_pos, winner)
        else:
            # winner not in ladder, loser not in ladder
            players.append(winner)
            players.append(loser)


def init_players():
    add_player('Matt')
    add_player('Dan')
    add_player('Ash')
    add_player('James')
    add_player('Doge')


def main():
    init_players()
    print players

# both in ladder already
    update_ladder('Ash', 'Matt')
    print players

# new winner to ladder
    update_ladder('Mike', 'Ash')
    print players

#both not in ladder
    update_ladder('Lee', 'Andy')
    print players

# loser not in ladder already
    update_ladder('Matt', 'Emily')
    print players


if __name__ == '__main__':
    main()
