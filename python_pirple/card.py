
####################################################################################

from termcolor import colored
import re

####################################################################################

class Card:

    """
    representing an indiviual card
    """

    ################################################################################

    def __init__(self, card_str):

        card_arr = list(card_str)

        self.suit = card_arr.pop()

        if len(card_arr) == 2:
            self.value = '10'
        else:
            self.value = card_arr[0]

        self.apparent_value = -1

    ################################################################################

    def getSuit(self):
        return self.suit

    ################################################################################

    def getValue(self):
        return self.value

    ################################################################################

    def displayCard(self):

        """
        pretty print a card
        """

        suit = self.getSuit().upper()

        if suit == 'S':
            suit_uu = '\u2664'
        elif suit == 'C':
            suit_uu = '\u2667'
        elif suit == 'H':
            suit_uu = '\u2661'
        else:
            suit_uu = '\u2662'

        card_str = self.getValue().rjust(2) + suit_uu
        if suit == 'S' or suit == 'C':
            card_str = colored(card_str, 'white', attrs=['bold', 'reverse'])
        else:
            card_str = colored(card_str, 'red', attrs=['bold', 'reverse'])

        return card_str

    ################################################################################

    def __str__(self):
        return self.getValue() + self.getSuit()

    ################################################################################

    def translateValueToNum(self):

        str_value = self.getValue()

        if str_value == 'A':
            return 14

        if str_value == 'K':
            return 13

        if str_value == 'Q':
            return 12

        if str_value == 'J':
            return 11

        return int(str_value)

    ################################################################################

    def __gt__(self, thatCard):

        """
        the card to the right is only greater if the same suit and higher value.
        otherwise the card to the left is greater
        """

        this_suit = self.getSuit()
        this_value = self.translateValueToNum()
        that_suit = thatCard.getSuit()
        that_value = thatCard.translateValueToNum()

        if this_suit != that_suit:
            return False

        if this_value > that_value:
            return True

        return False
    ################################################################################

    pattern = re.compile('(?:a|k|q|j|10|[2-9])[cdhs]')

    @staticmethod
    def isValidCard(card_str):
        matched = pattern.fullmatch(card_str.lower())
        return isinstance(matched, Match)

####################################################################################

