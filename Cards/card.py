from suits import Suits

card_values_to_names = {1: "Ace", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight",
                        9: "Nine", 10: "Ten", 11: "Jack", 12: "Queen", 13: "King"}

# ianheguhaougnaiengaipeghiaghiaegnpi
class Card:
    def __init__(self, value: int, suit: Suits):
        if value not in card_values_to_names:
            raise Exception(f"{value} is not a valid value")

        self.value = value
        self.suit = suit

    def get_name(self):
        card_val = card_values_to_names[self.value]
        card_suit = self.suit.value
        card_name = f"{card_val} of {card_suit}"

        return card_name
