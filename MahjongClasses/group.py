from piece import Piece

class Group:
    def __init__(self, piece1, piece2, piece3, type):
        self.grouping = [piece1, piece2, piece3]
        self.groupType = type