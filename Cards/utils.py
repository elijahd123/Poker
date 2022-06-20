from suits import Suits
from card import Card

card_value_min = 1
card_value_max = 13


def create_deck():
    deck = []

    for suit in [Suits.Hearts, Suits.Clubs, Suits.Diamonds, Suits.Spades]:
        for value in range(card_value_min, card_value_max + 1):
            deck.append(Card(value, suit))

    return deck
