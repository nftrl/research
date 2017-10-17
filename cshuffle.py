#!/usr/bin/env python3

# Alle functions skal skrives om til at tilpasses decks på størrelse n og ikke 52.

def newdeck():
    deck = [(c,n) for c in ('a','b','c','d') for n in range(1,14)]
    return deck


def printdeck(deck, stacks=1):
    if stacks == 1:
        for n in range(52):
            print('%c %i' % (deck[n][0], deck[n][1]))
    elif stacks == 2:
        for n in range(26): # Der er 52 kort i et deck
            print('%c %i\t%c %i' % 
                   (deck[n][0], deck[n][1], deck[n + 26][0], deck[n + 26][1]))
    else:
        print('Error: printdeck(): Invalid stacks number.')


def shuffle(deck):
    #split deck in to equal decks
    d1 = deck[:26]
    d2 = deck[26:]

    newdeck = []
    for n in range(26):
        newdeck.append(d1[n])
        newdeck.append(d2[n])

    return newdeck


if __name__ == '__main__':
    d = newdeck(4,15)

    print('-------------------- Initial deck')
    printdeck(d,2)

    for n in range(9):
        print('-------------------- Shuffle number %i' % (n+1))
        d = shuffle(d)
        printdeck(d,2)
