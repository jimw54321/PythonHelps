
####################################################################################

import random

from card import Card

####################################################################################

class CardCollection:

    """
    generic pile of cards to be subclassed for player hands, the deck, etc.
    """

    ################################################################################

    @staticmethod
    def sortCards(card):

        """
        sort the cards for easier display to the player
        """

        card_str = str(card)
        cv = card_str[0]
        cs = card_str[-1]

        if cv == 'A':
            cc = 14
        elif cv == 'K':
            cc = 13
        elif cv == 'Q':
            cc = 12
        elif cv == 'J':
            cc = 11
        elif cv == '1':
            cc = 10
        else:
            cc = int(cv)

        if cs == 'H':
            cc + 100
        elif cs == 'C':
            cc += 200
        elif cs == 'D':
            cc += 300
        else:
            cc += 400

        return cc

    ################################################################################

    def __init__(self):
        self.cards = []

    ################################################################################

    def __len__(self):
        return len(self.cards)

    ################################################################################

    def addCard(self, card):

        if isinstance(card, str):
            card = Card(card)

        self.cards.append(card)

        return card

    ################################################################################

    def getTopCard(self):
        card = self.cards.pop()
        return card

    ################################################################################

    def removeCard(self, card):

        found = False

        if isinstance(card, int):
            idx = card
            found = True
        else:
            for idx in range(len(self.cards)):
                if str(self.cards[idx]) == str(card):
                    found = True
                    break

        if found:
            return self.cards.pop(idx)

        return found

    ################################################################################

    def __str__(self):

        """
        when printing a collection of cards as a string, sort them and
        pretty print each card.
        """

        outstr = ""

        self.cards.sort(key=CardCollection.sortCards)

        if len(self.cards):
            for idx in range(len(self.cards) - 1):
                outstr += self.cards[idx].displayCard() + " "
            outstr += self.cards[-1].displayCard()

        return outstr

####################################################################################

