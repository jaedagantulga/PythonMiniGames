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
    'Ace':11
}

import random

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit




class Deck:

    def __init__(self):
        self.whole_deck = []

        for suit in suits:
            for rank in ranks:

                card = Card(suit,rank)
                
                self.whole_deck.append(card)
    
    def shuffle(self):
        random.shuffle(self.whole_deck)

    def deal(self):
        return self.whole_deck.pop()



# - holds chips and can add or minus them
# - holds cards and can add to them
# - if hit (by asking for input) - add a card to their hand
# - returns the value of all cards in their hand


# class Player:

#     def __init__(self,chip_amount):
#         self.chip_amount = chip_amount
#         self.current_cards = []

#     def adding_chips(self,bet):

#         self.chip_amount = self.chip_amount + bet
#         print(f'Current chip count: {self.chip_amount}')

#     def removing_chips(self,bet):

#         self.chip_amount = self.chip_amount - bet
#         print(f'Current chip count: {self.chip_amount}')

#     def adding_cards(self,new_card):

#         if 'Ace' in new_card:
#             one_or_eleven = int(input('Would you like the value of the Ace to be 1 or 11?: '))

#             if one_or_eleven == 1:
#                 self.current_cards.append(values['Ace_1'])
#             else:
#                 self.current_cards.append(values['Ace_11'])

#         else:
#             self.current_cards.append(new_card)

#     def __str__(self):
        
#         for card in self.current_cards:
#             total_value = 0

#             # if type(card) == type([]):
#             #     one_or_eleven = int(input('Would you like the value of the Ace to be 1 or 11?: '))

#             #     if one_or_eleven 

#             # else:
#             total_value += card.value

#         return f'Total value of cards: {total_value}'




class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card (self,new_card):
        self.cards.append(new_card)

    def adjust_for_aces(self):
        ace_choice = int(input('Would you like the value of the Ace to be 1 or 11?: '))

        if ace_choice == 1:
            values['Ace'] = 1


class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total = self.bet + self.total
        print(f'Current chip amount: {self.total}')

    def lose_bet(self):
        self.total = self.total - self.bet
        print(f'Current chip amount: {self.total}')



def take_bet():

    try:
        bet_amount = int(input('How many chips would you like to bet?: '))

    except self.total < bet_amount:
        int(input(f'There was an error. The amount you tried to bet might have exceeded your total chip count. You have {self.total} chips. How much would you like to bet?: '))


def hit(deck,hand):

    hand.add_card(deck.deal())

    if 'Ace' in self.current_cards:
        hand.adjust_for_aces()


def hit_or_stand(deck,hand):
    global playing

    hitting_or_staying = None

    while hitting_or_staying != 'H' or hitting_or_staying != 'S':

        hitting_or_staying = input('Would you like to hit (take another card) or stay? (Please type in H or S): ').upper()

    if hitting_or_staying == 'H':
        hit()
    else:
        playing = False


def show_some_cards(player,dealer):
    print(f'Dealer has 2 cards. One of them is {dealer.cards[1]}')
    print(f"Player's two cards are {player.cards[0]} and {player.cards[1]}")


def show_all_cards(player,dealer):
    if len(dealer.cards) == 2:
        print(f"Dealer's cards were {dealer.cards[0]} and {dealer.cards[1]}")
    elif len(dealer.cards) == 3:
        print(f"Dealer's cards were {dealer.cards[0]},{dealer.cards[1]} and {dealer.cards[2]}")
    else:
        print(f"Dealer's cards were {dealer.cards[0]},{dealer.cards[1]}, {dealer.cards[2]} and {dealer.cards[3]}")



def player_busts():
    print("It's a bust! Your hand value is over 21.")
    player_chips.lose_bet()


def player_wins():
    print("You've won!")
    player_chips.win_bet()


def dealer_busts():
    print("Dealer has busted! Their hand value went over 21.")
    dealer_chips.lose_bet()


def dealer_wins():
    print('Dealer has won!')
    computer_chips.win_bet()

def push():
    pass












