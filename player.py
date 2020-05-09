from piece import *

class Player:
    name = ""
    id = ""
    hand = []
    showed = []
    winner = False
    def __init__(self, n="", id = ""):
        self.name = n
        self.id = id
    def getNamePiece(self, elem):
        return elem.name()
    def add(self, piece):
        self.hand.append(piece)
        self.hand.sort(key=self.getNamePiece)

    def discard(self, i):
        return self.hand.pop(i)

    def win(self):
        self.winner = True

    def show(self, i):
        self.showed.append(self.hand.pop(i))

    d