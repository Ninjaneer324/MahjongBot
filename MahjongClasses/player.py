from piece import Piece

class Player:
    def __init__(self, name="", id=0):
        self.name = name
        self.id = id
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

