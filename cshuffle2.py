#!/usr/bin/env python3

# Alle functions skal skrives om til at tilpasses decks på størrelse n og ikke 52.

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
        
        if deck == initial:
            return i + 1

    return 0
    

if __name__ == '__main__':
    # s er antal kulører, n er antal kort i hver kulør.
    for s in range(10):
        for n in range(40):
            if (s*n) % 2 != 0: # Vi gider ikke ulige produkter
                continue

            d = newdeck(s, n)
            p = find_period(d)
            #print('s: %i, n: %i, product: %i, period: %i' % (s, n, (s * n), p))
            print('[%i, %i, %i, %i]' % (s, n, (s * n), p))

    #print('-------------------- Initial deck')
    #printdeck(d,2)
    #for n in range(9):
    #    print('-------------------- Shuffle number %i' % (n+1))
    #    d = shuffle(d)
    #    printdeck(d,2)
