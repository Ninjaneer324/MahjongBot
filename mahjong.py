from deck import Deck
import random

# created to provide an abstracted interface to interact with
class Mahjong:
    def __init__(self, type='standard'):
        self.deck = Deck()
        self.players = []

    def addPlayer(self, player):
        '''Adds players to the game and returns False when the max number of 4 players have already been reached'''
        if len(players) >= 4:
            return False
        players.append(player)
        return True

    def atFullCapacity(self):
        return len(self.players) == 4

    def deal():
        '''dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        wall = (dice_1 + dice_2) % 4
        wall_size = 0
        if deck.type.lower() == "standard":
            wall_size = 27
        else:
            wall_size = 34
        start = wall * wall_size + min(dice_1, dice_2)
        deck.moveBack(start)'''
        random.shuffle(self.players)
        self.dealToPlayers(self.players)

    def _playersHave12(self, players):
        for p in players:
            if len(p.hand) != 12:
                return False
        return True

    def dealToPlayers(self, playerOrder):
        '''Assuming playerOrder is a list of players, deal 13 tiles to each player and 14 tiles to starting player'''
        while not self._playersHave12(playerOrder):
            for p in playerOrder:
                for i in range(4):
                    p.add(self.deck.drawFront())
        for p in playerOrder:
            p.add(self.deck.drawFront())
        playerOrder[0].add(self.deck.drawFront())