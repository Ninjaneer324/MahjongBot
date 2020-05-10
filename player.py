from piece import *

class Player:
    showed = []
    def __init__(self, name="", id=""):
        self.name = name
        self.id = id
        self.hand = []
        self.showed = []
        self.winner = False

    def getPiece(self, piece):
        return piece.name()

    def getWinStatus(self):
        return self.winner

    def add(self, piece):
        self.hand.append(piece)
        self.hand.sort(key=self.getNamePiece)

    def discard(self, i):
        return self.hand.pop(i)

    def win(self):
        self.winner = True

    def show(self, i): # possibly should change
        self.showed.append(self.hand.pop(i))