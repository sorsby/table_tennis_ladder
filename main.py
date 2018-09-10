from ladder import Ladder

def main():

    test_players = ['Ash', 'Matt', 'Mike', 'Dan', 'Emily']
    # init_players()
    print "Main func."
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


if __name__ == '__main__':
    main()