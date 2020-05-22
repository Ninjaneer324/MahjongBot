from deck import Deck
from piece import Piece
from group import Group
import random

# created to provide an abstracted interface to interact with
class Mahjong:
    def __init__(self, type='standard'):
        self.deck = Deck(type)
        self.players = []
        self.pile = []

    def addPlayer(self, player):
        '''Adds players to the game and returns False when the max number of 4 players have already been reached'''
        if len(self.players) >= 4:
            return False
        self.players.append(player)
        return True

    def atFullCapacity(self):
        return len(self.players) == 4

    def deal(self):
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
        self.dealToPlayers()

    def _playersHave12(self):
        for p in self.players:
            if len(p.hand) != 12:
                return False
        return True

    def dealToPlayers(self):
        '''Assuming playerOrder is a list of players, deal 13 tiles to each player and 14 tiles to starting player'''
        while not self._playersHave12():
            for p in self.players:
                p.add(self.deck.drawFront())
                p.add(self.deck.drawFront())
                p.add(self.deck.drawFront())
                p.add(self.deck.drawFront())
        for p in self.players:
            p.add(self.deck.drawFront())
        self.players[0].add(self.deck.drawFront())
    
    def winnerCheck(self):
        for i in self.players:
            if i.winner:
                return True
        return False
    
    def gameDraw(self):
        for i in self.players:
            if i.winner:
                return False
        return self.deck.isEmpty()
    
    def possibleCombos(self, num = 0, suit = ""):
        temp = []
        if num == 1:
            temp.append(Group())
            temp[0].add(Piece(suit, 1))
            temp[0].add(Piece(suit, 2))
            temp[0].add(Piece(suit, 3))
        elif num == 9:
            temp.append(Group())
            temp[0].add(Piece(suit, 1))
            temp[0].add(Piece(suit, 2))
            temp[0].add(Piece(suit, 3))
        elif num == 2:
            temp.append(Group())
            temp[0].add(Piece(suit, 1))
            temp[0].add(Piece(suit, 2))
            temp[0].add(Piece(suit, 3))
            temp.append(Group())
            temp[1].add(Piece(suit, 2))
            temp[1].add(Piece(suit, 3))
            temp[1].add(Piece(suit, 4))
        elif num == 8:
            temp.append(Group())
            temp[0].add(Piece(suit, 7))
            temp[0].add(Piece(suit, 8))
            temp[0].add(Piece(suit, 9))
            temp.append(Group())
            temp[1].add(Piece(suit, 6))
            temp[1].add(Piece(suit, 7))
            temp[1].add(Piece(suit, 8))
        elif 3 <= num <= 7:
            temp.append(Group())
            temp[0].add(Piece(suit, num - 2))
            temp[0].add(Piece(suit, num - 1))
            temp[0].add(Piece(suit, num))
            temp.append(Group())
            temp[1].add(Piece(suit, num - 1))
            temp[1].add(Piece(suit, num))
            temp[1].add(Piece(suit, num + 1))
            temp.append(Group())
            temp[2].add(Piece(suit, num))
            temp[2].add(Piece(suit, num + 1))
            temp[2].add(Piece(suit, num + 2))
        return temp