class Piece:
    def __init__(self, suit, number=0):
        self.number = number
        self.suit = suit

    def name(self):
        return ("" if self.number == 0 else (str(self.number) + " ")) + self.suit