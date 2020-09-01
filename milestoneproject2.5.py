##### MILESTONE PROJECT 2.5 #####

# making a blackjack game using OOP

# game basics

# have a computer dealer and a human player
# start with a normal deck of cards (create a representation of a deck with python)

# human player has a bank roll (think attribute)
# will place a bet
 
# dealer starts with 1 card face up, 1 card face down
# player starts with 2 cards face up

# player goes first in gameplay

# possible actions to get close to 21
# - hit (receive another card)
# - stay (stop receiving cards)

# after player turn, if the player is under 21 dealer then hits until they either beat the player or the dealer busts

# 3 possible situations
# - before it's even dealer's turn, player busts
# - dealer took turn and is higher than player's cards and under 21, they win
# - after dealer take turns, player has closer value to 21 or dealer busts, player wins

# special rules
# face cards (jack,queen,king) count as value of 10
# aces can count as either 1 or 11, whichever the player chooses


# player class
# - holds chips and can add or minus them
# - holds cards and can add to them
# - if hit (by asking for input) - add a card to their hand
# - returns the value of all cards in their hand


# deck class
# - create whole deck (52 cards)
# - shuffle deck
# - deal two


suits = ('Hearts','Diamonds','Spades','Clubs')

ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')

values = {
    'Two':2,
    'Three':3,
    'Four':4,
    'Five':5,
    'Six':6,
    'Seven':7,
    'Eight':8,
    'Nine':9,
    'Ten':10,
    'Jack':10,
    'Queen':10,
    'King':10,
    'Ace':1,11
}


class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):
        self.whole_deck = []

        for suit in suits:
            for rank in ranks:

                card = Card(suit,rank)
                
                self.whole_deck.append(card)


print(len(Deck())











