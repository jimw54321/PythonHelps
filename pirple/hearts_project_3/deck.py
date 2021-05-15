
####################################################################################

import random

from cardcollection import CardCollection
from card import Card

####################################################################################

class Deck(CardCollection):

    """
    deck of cards
    """

    ################################################################################

    def __init__(self, new_deck='yes'):

        """
        if the seconds param has value other than "yes", then assume its an
        empty deck. useful for creating the shuffled deck from an unshuffled
        deck.
        """

        self.cards = []

        if new_deck == 'yes':
            for suit in ['D', 'H', 'C', 'S']:
                for value in ['2', '3', '4', '5', '6', '7', '8', \
                              '9', '10', 'J', 'Q', 'K', 'A']:
                    self.addCard(value + suit)


    ################################################################################

    def getRandomCard(self):

        idx = random.randint(0, len(self.cards)-1)
        card = self.cards[idx]
        self.removeCard(idx)
        return card

####################################################################################
