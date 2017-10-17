#!/usr/bin/env python3

import sys


def newdeck(suits=4, cards=13):
    # cards = cards per suit
    alph = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    deck = [(c,n) for c in alph[:suits] for n in range(1, cards+1)]
    return deck


def printdeck(deck, stacks=1):
    decklength = len(deck)
    if stacks == 1:
        for n in range(decklength):
            print('%c %i' % (deck[n][0], deck[n][1]))
    elif stacks == 2:
        for n in range(decklength//2): # Der er 52 kort i et deck
            print('%c %i\t%c %i' % 
                   (deck[n][0], deck[n][1], deck[n + decklength//2][0], deck[n + decklength//2][1]))
    else:
        print('Error: printdeck(): Invalid stacks number.')


def shuffle(deck):
    decklength = len(deck)

    #split deck in to equal parts
    part1 = deck[:decklength//2]
    part2 = deck[decklength//2:]

    shuffled_deck = []
    for n in range(decklength//2):
        shuffled_deck.append(part1[n])
        shuffled_deck.append(part2[n])

    return shuffled_deck


def find_period(deck, ceiling=1000):
    initial = deck
    for i in range(ceiling):
        deck = shuffle(deck)
        
        # check for match
        if deck == initial:
            return i + 1

    # if no match was found, return 0
    return 0


def printhelp():
    print('Usage: cshuffle2.py s_min s_max n_min n_max ceiling')
    print('all args must be integers')


def main(s_min, s_max, n_min, n_max, ceiling):
    try:
        for s in range(s_min, s_max+1): # +1 fordi range er ekskl.
            for n in range(n_min, n_max+1): # +1 fordi range er ekskl.
                if (s*n) % 2 != 0: # Vi gider ikke ulige produkter
                    continue

                d = newdeck(s, n)
                p = find_period(d, ceiling)
                print('[%i, %i, %i, %i]' % (s, n, (s*n), p))
    except KeyboardInterrupt:
        print()


if __name__ == '__main__':
    args = sys.argv[1:] # read arguments
    if not args or args[0] == '--help' or len(args) != 5:
        printhelp()
        pass
    else:
        try:
            s_min = int(args[0]) # s er antal kulører
            s_max = int(args[1])
            n_min = int(args[2]) # n er antal kort i hver kulør
            n_max = int(args[3])
            ceiling = int(args[4]) # loftet for find_period()
        except ValueError:
            print('Error: must be integers.')
            printhelp()

        main(s_min, s_max, n_min, n_max, ceiling)
