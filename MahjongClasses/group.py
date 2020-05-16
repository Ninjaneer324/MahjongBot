from piece import Piece

class Group:
    def __init__(self, pieces = []):
        self.pieces = list(pieces)
        self.groupType = self.updateType()
        self.shown = False

    def updateType(self):
        if len(self.pieces) <= 1 or len(self.pieces) > 4:
            self.groupType = "none"
            return "none"
        if all(piece.name() == self.pieces[0].name() for piece in self.pieces):
            if len(self.pieces) == 2:
                self.groupType = "pair"
                return "pair"
            if len(self.pieces) == 3:
                self.groupType = "triple"
                return "triple"
            if len(self.pieces) == 4:
                self.groupType = "quadruple"
                return "quadruple"
        if len(self.pieces) == 3 and all(piece.suit == self.pieces[0].suit for piece in self.pieces):
            minVal = min(piece.number for piece in self.pieces)
            if max(piece.number for piece in self.pieces) - minVal == 2:
                if any(piece.number == minVal + 1 for piece in self.pieces):
                    self.groupType = "series"
                    return "series"
        self.groupType = "none"
        return "none"

    def addPiece(self, piece):
        self.pieces.append(piece)
        self.updateType()

    # returns None if piece not found
    def removePiece(self, piece):
        removed = next((selfpiece for selfpiece in self.pieces if selfpiece.name() == piece.name()), None)
        if removed is not None:
            self.pieces.remove(removed)
        self.updateType()
        return removed

    def printGroup(self):
        print(self.groupType, "[", ', '.join(piece.name() for piece in self.pieces), "]")