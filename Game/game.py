from Player.player import Player
from Game.gamesettings import GameSettings
# to do: game, calculate winner, currency, pot, blinds, player actions, dealing


class Game:
    def __init__(self, settings: GameSettings):
        self.settings = settings
        self.players = []
        self.new_players = []
        self.players_in_round = []
        self.dealer_index = 0
        self.pot = 0

    def add_player(self, player: Player):
        if len(self.players) >= self.settings.max_players:
            return
        self.new_players.append(player)
        self.players.append(player)

    def remove_player(self, player: Player):
        self.players.pop(self.players.index(player))
        self.players_in_round.pop(self.players_in_round.index(player))

    def play_round(self):
        self.players_in_round = list(filter(lambda player: player.cash >= self.settings.buy_in.big_blind, self.players.copy()))
        small_blind_player = self.players_in_round[self.dealer_index - 1]
        big_blind_player = self.players_in_round[self.dealer_index - 2]


