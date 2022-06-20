from random import shuffle
from utils import create_deck


class Deck:
    def __init__(self):
        self.cards = create_deck()
        shuffle(self.cards)

    def get_card(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop(0)
