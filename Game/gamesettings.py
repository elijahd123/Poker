from Game.buyin import BuyIn


class GameSettings:
    def __init__(self, max_players, buy_in: BuyIn):
        self.max_players = max_players
        self.buy_in = buy_in
