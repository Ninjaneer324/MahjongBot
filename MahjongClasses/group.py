from piece import Piece

class Group:
    def __init__(self, pieces = []):
        self.pieces = list(pieces)
        self.shown = False
        self.pieces.sort(key=lambda piece: piece.name())
        self.groupType = ""
        self.updateType()

    def updateType(self):
        if len(self.pieces) <= 1 or len(self.pieces) > 4:
            self.groupType = "none"
        elif all(piece.name() == self.pieces[0].name() for piece in self.pieces):
            if len(self.pieces) == 2:
                self.groupType = "pair"
            elif len(self.pieces) == 3:
                self.groupType = "triple"
            elif len(self.pieces) == 4:
                self.shown = True
                self.groupType = "quadruple"
        elif len(self.pieces) == 3 and all(piece.suit == self.pieces[0].suit for piece in self.pieces):
            if self.pieces[0].number + 2 == self.pieces[1].number + 1 == self.pieces[2].number:
                self.groupType = "series"
        else:
            self.groupType = "none"
        if self.shown:
            self.groupType = self.groupType.capitalize()

    def showGroup(self):
        self.shown = True
        self.groupType = self.groupType.capitalize()
    
    # returns None if unable to modify group
    def add(self, piece):
        if self.shown:
            if self.groupType != "Triple":
                return None
            elif piece.name() != self.pieces[0].name():
                return None
        self.pieces.append(piece)
        self.pieces.sort(key=lambda piece: piece.name())
        self.updateType()
        return piece

    # returns None if piece not found or unable to modify group
    def remove(self, piece):
        if self.shown or piece not in self.pieces:
            return None
        self.pieces.remove(piece)
        self.pieces.sort(key=lambda piece: piece.name())
        self.updateType()
        return piece

    # for debugging
    def printGroup(self):
        print(self.groupType, "[", ', '.join(piece.name() for piece in self.pieces), "]")