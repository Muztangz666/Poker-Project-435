import math, random, pygame, time

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def __str__(self):
        return '(suit:' + str(self.suit) + ', rank: ' + str(self.rank) + ')'


class Deck():
    def __init__(self):
        self.deck_cards = []
        self.initializeDeck()

    def initializeDeck(self):
        self.deck_cards = []

        #create deck by creating 52 card object with each different ranks and suits.
        for i in range(0, 4):
            for j in range(0, 13):
                self.deck_cards.append(Card(i, j))

    def shuffleDeck(self):
        shuffled_cards = []

        #shuffle the deck by going through the deck and giving each card a random
        #number and then appending the to a new list effectively changing the order.
        for i in range(len(self.deck_cards)):
            if len(self.deck_cards) > 1:
                c = random.choice(self.deck_cards)
                shuffled_cards.append(c)
                self.deck_cards.remove(c)
            else:
                c = self.deck_cards.pop()
                shuffled_cards.append(c)
        self.deck_cards = shuffled_cards

    def popDeck(self):
        return self.deck_cards.pop(0)