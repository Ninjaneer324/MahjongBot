class Piece:
    number = 0
    suit = ""
    pos = []

    def __init__(self, n=0, s=""):
        self.number = n
        self.suit = s

    def name(self):
        return ("" if not self.number else (str(self.number) + " ")) + self.suit
