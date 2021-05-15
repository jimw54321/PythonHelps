
####################################################################################

from hand import Hand
from hold import Hold

class Player:

    ################################################################################

    Players = []

    def __init__(self, name):

        self.name = name
        self.hand = Hand()
        self.hold = Hold()
        self.total_score = 0
        self.score_for_hand = 0
        Player.Players.append(self)

    ################################################################################

    @classmethod
    def aPlayerReached100(cls):

        for p in cls.Players:
            if p.total_score >= 100:
                return True

        return False

    ################################################################################

    @classmethod
    def playerLowestScore(cls):

        lowest_score_player = cls.Players[0]
        for p in range(1,4):
            if lowest_score_player.total_score > p.total_score:
                lowest_score_player = p

        return lowest_score_player

    ################################################################################

    def __str__(self):
        return self.name + ' ' \
             + str(self.total_score) \
             + '(' \
             + str(self.score_for_hand) \
             + ') ' \
             + str(self.hand)

    ################################################################################

    def has2Clubs(self):
        found = self.hand.has2Clubs()
        return found

    ################################################################################

    def addToHand(self, card):
        self.hand.addCard(card)
        return

    ################################################################################

    def removeFromHand(self, discard):
        return self.hand.removeCard(discard)

    ################################################################################

    def getName(self):
        return self.name

####################################################################################
