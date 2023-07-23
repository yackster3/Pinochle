import deck
import numpy as np

class Pinochle(object):
    """
    For Pinochle.
        3 or 4 players with hands delt from a stack of cards of a certain number of decks (generally 1 or 2).
        currently this program only will work for a 4 handed Pinochle, but it should be made for extension to
        3 handed versions.
    """

    def __init__(self, decks = 2, players = 4):
        self.decks = decks
        self.players = []
        self.kitty = []
        for i in range(0, players):
            self.players.append(Player(seat = i))

    def deal(self):
        dealing = deck.shuffle(type = "Pinochle", count = self.decks)

        while len(dealing) > 4:

            card = dealing.pop()

            #The +1 here is to deal to the left of the dealer.
            self.players[(len(dealing)+1)%len(self.players)]

        self.kitty = []

    



class Player(object):
    """
        A player has a position (seat) that determines the order in which the game proceeds (and which team)
        a hand that gives them meld (points in the game) and plays for tricks (another type of points)
        A player may also take the bid, and in taking the bid they and their partners meld/trick total
        must meet the value of their bid to avoid going "set" and losing points. If a player takes the
        bid they also may determine trump for the game, and as an additional reward for taking the bid
        when a kittie is found they get 4 additional cards in their hand and may take 4 of the cards as
        tricks.
    """

    def __init__(self, seat, hand = [], meld = 0, tricks = 0, bid = 0):
        self.seat = seat
        self.hand = hand
        self.meld = meld
        self.tricks = tricks
        self.bid = bid
