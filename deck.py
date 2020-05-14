from piece import Piece
from random import shuffle

class Deck:
    standard_deckSuits = ["Bamboo", "Dot", "Wan"]
    honor_deckSuits = ["North", "South", "East", "West", "Center", "Fortune", "TV"]

    def __init__(self, type="standard"):
        self.type = type
        self.deck = []
        self.reset()

    def reset(self):
        '''Shuffles the deck'''
        if self.deck:
           self.deck.clear()
        for suit in Deck.standard_deckSuits:
            for i in range(1, 10):
                t = Piece(suit, i)
                for j in range(4):
                    self.deck.append(t)
        if self.type.lower == "honor":
            for suit in Deck.honor_deckSuits:
                t = Piece(suit)
                for i in range(4):
                    self.deck.append(t)
        self.shuffle()

    def shuffle(self):
        shuffle(self.deck)

    def size(self):
        return len(self.deck)

    def printDeck(self):
        for p in self.deck:
            print(p.name())

    def drawFront(self):
        return self.deck.pop(0)

    def drawBack(self):
        return self.deck.pop()

    '''def moveBack(self, firstCards):
        poppedCards = 0
        while poppedCards < firstCards:
            pop = self.deck.pop(0)
            self.deck.append(pop)
            poppedCards += 1'''