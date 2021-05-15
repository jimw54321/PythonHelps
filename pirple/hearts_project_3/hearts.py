
"""
Title:      Hearts Card Game
Programmer: Jim Woodworth
Date:       15-May-2021
"""

####################################################################################

import random

from deck import Deck
from player import Player
from trick import Trick
from card import Card

####################################################################################

def printHelp():

    help_file = 'how_to_play_hearts.txt'
    with open(help_file, 'r') as f:
        lines = f.readlines()

    for line in lines:
        print(line, end="")
    print()

    getInput(1, "(type '--resume')")

####################################################################################

def clearScreen():
    print(chr(27) + "[2J")
    return

####################################################################################

def shift3Cards(hand_num, players):

    """
    Shift 3 cards to another player. Alternates among left, right, then across.
    Then no shifting is done next before starting over with shifting left.
    """

    hand_num += 1

    rem = hand_num % 4
    if rem == 0:
        direction = 'left'
        displace = 1
    elif rem == 1:
        direction = 'right'
        displace = 3
    elif rem == 2:
        direction = 'across'
        displace = 2
    else:
        return hand_num

    for shift_giver in range(4):
        print(players[shift_giver])

        cards = getInput(3, "Choose 3 cards to shift " + direction + " ")

        for c in cards:
            players[shift_giver].hand.removeCard(c)

        shift_recvr = (shift_giver + displace) % 4
        for c in cards:
            players[shift_recvr].hold.addCard(c)

        clearScreen()

    for p in players:
        for card in list(p.hold.cards):
            p.hold.removeCard(card)
            p.hand.addCard(card)

    return hand_num

####################################################################################

def find2Clubs(players):

    """
    Find which player holds the 2 of Clubs.
    """

    for p in range(len(players)):
        if players[p].has2Clubs():
            break

    return p

####################################################################################

def getPlayerName(player_num):

    """
    Get the player's name
    """

    input_str = "What is player" + str(player_num+1) + "'s name? "
    return getInput(1, input_str)[0]

####################################################################################

def checkPlayersForWin(players):

    """
    Detect if a player has reached 100 points.
    """

    for p in players:
        if p.total_score >= 100:
            return True

    return False

####################################################################################

def getInput(num_inputs, input_prompt):

    """
    Generic routine to handle user input.
    """

    while True:
        try:
            choices = []

            inputs = input(input_prompt)

            if isinstance(inputs, str) and inputs == '--help':
                printHelp()
                continue

            for input_str in inputs.split(","):
                input_str = input_str.strip()
                if input_str != "":
                    choices.append(input_str.upper())

            if len(choices) == num_inputs:
                break
            else:
                raise ValueError

        except ValueError:
            print("Incorrect number of inputs")

    return choices

####################################################################################

def deal(deck, players):

    """
    Deal the deck to the four players
    """

    player_num = 0

    for n in range(52):
        card = deck.getTopCard()
        players[player_num].addToHand(card)
        if player_num == 3:
            player_num = 0
        else:
            player_num += 1

####################################################################################

def getNextPlayer(next_player):

    """
    Determine which player is next.
    """

    if next_player == 3:
        next_player = 0
    else:
        next_player += 1

    return next_player

####################################################################################

def getInputCard(cards_can_play):

    """
    Get input from a player of a card
    """

    good_card = False
    while not good_card:
        card_str = getInput(1, "Choose a card to play: ")[0]
        for c in cards_can_play:
            if str(c) == card_str:
                good_card = True
                break

        if not good_card:
            print("Cannot play " + card_str)

    return card_str

####################################################################################

def playNextThree(hearts_broken, trick, players, next_player, suit_lead):

    """
    Loop through the next 3 players getting their cards to play
    """

    for p in range(3):
        clearScreen()

        print(trick.displayNarrative())
        print(players[next_player])

        print("allowed cards to play: ", end="")
        cards_can_play = []
        # for the first trick (where the 2 of clubs was played), must follow
        # suit as usual. if player has no clubs, then the player is allowed
        # to play the Queen of Spades. otherwise if the player has only hearts
        # can a heart be played on the first trick.
        if str(trick.cards[0]) == '2C':
            for c in players[next_player].hand.cards:
                if c.getSuit() == suit_lead:
                    cards_can_play.append(c)

            if len(cards_can_play) == 0:
                for c in players[next_player].hand.cards:
                    if c.getSuit() != 'H' and str(c) != 'QS':
                        cards_can_play.append(c)

            if len(cards_can_play) == 0:
                for c in players[next_player].hand.cards:
                    if c.getSuit() != 'H':
                        cards_can_play.append(c)

            if len(cards_can_play) == 0:
                cards_can_play.append(c)

        # after the first trick, suit must still be followed,
        # but otherwise any other suit may be played.
        else:
            for c in players[next_player].hand.cards:
                if c.getSuit() == suit_lead:
                    cards_can_play.append(c)

            if len(cards_can_play) == 0:
                cards_can_play = players[next_player].hand.cards

        for c in cards_can_play:
            print(" " + c.displayCard(), end="")
        print()

        card_str = getInputCard(cards_can_play)

        card = players[next_player].removeFromHand(card_str)

        trick.addCard(players[next_player], card)
        if card > trick.highCard():
            trick.setHighCard(players[next_player], card)

        next_player = getNextPlayer(next_player)

    # update everyone's score so far for the hand
    trick.computeScore(players)

    if not hearts_broken:
        for c in trick.cards:
            suit = c.getSuit()
            if suit == 'H':
                hearts_broken = True
                break

    return hearts_broken

####################################################################################

def playTrick(trick, hearts_broken, players, next_player):

    """
    handle the first card of a trick for second and subsequent tricks of the hand
    """

    clearScreen()
    print(players[next_player])
    print("allowed cards to play: ", end="")
    cards_can_play = []
    for c in players[next_player].hand.cards:
        if hearts_broken:
            cards_can_play.append(c)
        elif c.getSuit() != 'H':
            cards_can_play.append(c)

    if len(cards_can_play) == 0:
        cards_can_play = players[next_player].hand.cards

    for c in cards_can_play:
        print(" " + c.displayCard(), end="")
    print()

    card_str = getInputCard(cards_can_play)
    card = players[next_player].removeFromHand(card_str)
    trick.addCard(players[next_player], card)
    trick.setHighCard(players[next_player], card)

    next_player = getNextPlayer(next_player)
    suit_lead = card.getSuit()
    hearts_broken = playNextThree(hearts_broken, trick, players, next_player, suit_lead)

    return hearts_broken

####################################################################################

def playTrick2Clubs(trick, players, first_player):

    """
    play the initial card of the hand (2 of clubs)
    """

    clearScreen()

    card = players[first_player].removeFromHand('2C')
    print(players[first_player])
    print("allowed card to play: " + card.displayCard())
    getInput(0, "(press return)")
    trick.addCard(players[first_player], card)
    trick.setHighCard(players[first_player], card)

    next_player = getNextPlayer(first_player)
    hearts_broken = playNextThree(False, trick, players, next_player, 'C')

    print(trick.highCard(), trick.highCardPlayer().getName())

    return hearts_broken

####################################################################################

### MAIN ###

players = []

hearts_broken = False

hand_num = -1

# get players' names
for i in range(4):
    name = getPlayerName(i)
    player = Player(name)
    players.append(player)

# keep looping until someone gets a 100 or more
while not Player.aPlayerReached100():

    deck_unsh = Deck()
    deck_shuf = Deck('no')

    for x in range(52):
        card = deck_unsh.getRandomCard()
        deck_shuf.addCard(card)

    deal(deck_shuf, players)

    hand_num = shift3Cards(hand_num, players)

    first_player = find2Clubs(players)
    trick = Trick()
    hearts_broken = playTrick2Clubs(trick, players, first_player)

    # figure out which player had the high card
    name = trick.highCardPlayer().getName()
    for p in range(len(players)):
        if players[p].getName() == name:
            next_player = p
            break

    # the player with high card each trick leads the next trick
    for i in range(12):
        trick = Trick()
        hearts_broken = playTrick(trick, hearts_broken, players, next_player)
        name = trick.highCardPlayer().getName()
        for p in range(len(players)):
            if players[p].getName() == name:
                next_player = p
                break

    # re-init each player
    for p in players:
        p.hand.cards = []
        p.hold.cards = []
        p.total_score += p.score_for_hand
        p.score_for_hand = 0

name_won = Player.playerLowestScore()
print(name_won + " WON THE GAME!")

####################################################################################

