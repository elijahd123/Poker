import guid


class Player:
    def __init__(self, name: str, cash: float):
        self.id = guid.guid.uuid4()
        self.name = name
        self.cards = None
        self.cash = cash


player = Player("Bob", 53.1)
print(player.id)
