
####################################################################################

from cardcollection import CardCollection

####################################################################################

class Trick(CardCollection):

    TRICK_NUM = 0

    ################################################################################

    def __init__(self):
        super().__init__()
        self.high_card = ""
        self.high_card_player = ""
        self.narrative = []
        Trick.TRICK_NUM += 1

    ################################################################################

    def setHighCard(self, player, card):
        self.high_card = card
        self.high_card_player = player
        return

    ################################################################################

    def addCard(self, player, card):
        message = player.getName() + " " + card.displayCard()
        self.narrative.append(message)
        super().addCard(card)
        return

    ################################################################################

    def highCard(self):
        return self.high_card

    ################################################################################

    def highCardPlayer(self):
        return self.high_card_player

    ################################################################################

    def displayNarrative(self):

        """
        form the message of what has been played so far
        """

        message = "\n".join(self.narrative)
        return message

    ################################################################################

    def computeScore(self, players):

        high_card_player = self.highCardPlayer()

        for c in self.cards:
            suit = c.getSuit()
            if suit == 'H':
                high_card_player.score_for_hand += 1
            elif str(c) == 'QS':
                high_card_player.score_for_hand += 13

        if Trick.TRICK_NUM % 13 == 0 and high_card_player.score_for_hand == 26:
            print(high_card_player.name + " SHOT THE MOON!")
            for p in players:
                if p.name == high_card_player.name:
                    p.score_for_hand = 0
                else:
                    p.score_for_hand = 26

        return

####################################################################################
