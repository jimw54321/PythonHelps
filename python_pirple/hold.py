
####################################################################################

from cardcollection import CardCollection

####################################################################################

class Hold(CardCollection):

    """
    the cards held by a player during the shift to another player. this is done
    so a player does not know what cards they are shifting before their shifting.
    """

    ################################################################################

    def __init__(self):
        super().__init__()

####################################################################################
