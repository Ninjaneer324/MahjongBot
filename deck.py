from piece import *
from random import shuffle

class Deck:
    type = ""
    d = []

    def __init__(self, t="standard"):
        self.type = t
        self.reset()

    def reset(self):
        if self.d:
            self.clear()
        for i in range(1, 10):
            t = Piece(i, "Bamboo")
            self.d.append(t)
            self.d.append(t)
            self.d.append(t)
            self.d.append(t)
        for i in range(1, 10):
            t = Piece(i, "Dot")
            self.d.append(t)
            self.d.append(t)
            self.d.append(t)
            self.d.append(t)
        for i in range(1, 10):
            t = Piece(i, "Wan")
            self.d.append(t)
            self.d.append(t)
            self.d.append(t)
            self.d.append(t)
        if self.type == "honor":
            for i in range(4):
                t = Piece(0, "North")
                self.d.append(t)

            for i in range(4):
                t = Piece(0, "South")
                self.d.append(t)

            for i in range(4):
                t = Piece(0, "East")
                self.d.append(t)

            for i in range(4):
                t = Piece(0, "West")
                self.d.append(t)

            for i in range(4):
                t = Piece(0, "Center")
                self.d.append(t)

            for i in range(4):
                t = Piece(0, "Fortune")
                self.d.append(t)

            for i in range(4):
                t = Piece(0, "TV")
                self.d.append(t)
        self.shuffle()

    def clear(self):
        self.d.clear()

    def shuffle(self):
        shuffle(self.d)

    def size(self):
        return len(self.d)

    def print(self):
        for p in self.d:
            print(p.name())

    def draw(self):
        return self.d.pop(0)

    def back(self):
        return self.d.pop()