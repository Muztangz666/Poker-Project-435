import pickle, math, random, carddeckClass

class Player:
    def __init__(self, name, id, money=1500):
        self.name = name
        self.id = id
        self.money = money
        self.IsDead = False

        self.dealer = False
        self.smallBlind = False
        self.bigBlind = False
        self.hasFolded = False
        self.allIn = False

        self.IsChecked = False

        self.curr_bet_type = ""
        self.curr_bet_amount = 0
        self.card_list = []
        self.curr_raise_number = 0

        self.round_result = None

    def dealCard(self, card):
        if len(self.card_list) < 2:
            self.card_list.append(card)
            return True
        else:
            return False

    def initializePlayer(self):
        if not self.IsDead:
            self.card_list = []
            self.IsFold = False
            self.IsAllIn = False
            self.curr_bet = ""
            self.IsDealer = False
            self.IsSmallBlind = False
            self.IsBigBlind = False
            self.IsChecked = False

            self.curr_raise_number = 0
            self.round_result = None


'''
code sample testing the creation of a player object and a deck object then 
shuffling and dealing cards
deck = carddeckClass.Deck()
deck.shuffleDeck()

player1 = Player("colin",1)


for i in range(0,10):
    player1.card_list = []
    player1.dealCard(deck.popDeck())
    player1.dealCard(deck.popDeck())
    print(str(player1.card_list[0].getRank()) + " " + str(player1.card_list[0].getSuit()))
    print(str(player1.card_list[1].getRank()) + " " + str(player1.card_list[1].getSuit()))
'''
