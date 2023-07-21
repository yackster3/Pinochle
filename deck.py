import numpy as np
import random

"""
Generates cards and assigns values to them. 1 is typically ace, and I just put king then queen rolling over the modulous 12
"""
def generateCard(suit, value):

    if suit == 0:
        suit = "Spade"
    if suit == 1:
        suit = "Diamond"
    if suit == 2:
        suit = "Heart"
    if suit == 3:
        suit = "Club"

    if value == 1:
        value = "Ace"
    elif value == 0:
        value == "King"
    elif value == 11:
        value = "Queen"
    elif value == 12:
        value = "Jack"

    return (suit, value)

"""
Generates a standard or Pinochle deck of cards
"""
def createDeck(type = "Standard", count = 1):
    myDeck = []

    for i in range(0,13):
        for j in range(0, 4):
            if type == "Pinochle":
                if i > 8 or i < 2:
                    for k in range(0, count * 2):
                        myDeck.append(generateCard(j,i))
            elif type == "Standard":
                for k in range(0, count):
                    myDeck.append(generateCard(j,i))
            else:
                raise ValueError("Invalid deck type input")

    return myDeck

def shuffle(deck = None, type = "Standard", count = 1):
    if deck == None:
        deck = createDeck(type = type, count = count)

    random.shuffle(deck)
    return deck
