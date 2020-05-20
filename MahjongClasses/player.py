from discord import Member
from discord import User
from piece import Piece

class Player:
    def __init__(self, m):
        self.member = m
        self.name = m.name
        self.id = str(m.id)
        self.hand = []
        self.winner = False

    def getPiece(self, piece):
        return piece.name()

    def getWinStatus(self):
        return self.winner

    def add(self, piece):
        self.hand.append(piece)
        self.hand.sort(key=self.getPiece)

    def discard(self, i):
        return self.hand.pop(i)

    def win(self):
        self.winner = True
        