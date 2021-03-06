from discord import Member
from discord import User
from piece import Piece
from group import Group

class Player:
    def __init__(self, m):
        self.member = m
        self.name = m.name
        self.id = str(m.id)
        self.hand = []
        self.winner = False
        self.lastShown = -1
        self.lastHidden = -1

    def getPiece(self, piece):
        return piece.name()

    def getWinStatus(self):
        return self.winner

    def add(self, piece):
        self.hand.append(piece)
        self.sortHand()
    
    def canPengOrKong(self, piece = Piece("")):
        cnt = 0
        if piece.suit != "":
            for p in range(len(self.hand)):
                if isinstance(self.hand[p], Piece) and self.hand[p].name() == piece.name():
                    cnt += 1
            for p in range(len(self.hand)):
                if isinstance(self.hand[p], Group) and self.hand[p].find(piece) is not None:
                    cnt += 1
        return cnt

    # hand is sorted: shown groups alphabetically, hidden groups alphabetically, all pieces alphabetically
    def sortHand(self):
        self.hand.sort(key=lambda x: (str(type(x)), x.groupType if isinstance(x, Group) else x.name()))
        self.lastShown = -1
        self.lastHidden = -1
        for i in range(len(self.hand)):
            if isinstance(self.hand[i], Group):
                if self.hand[i].shown:
                    self.lastShown = i
                else:
                    self.lastHidden = i
            else:
                break

    ''' treats Groups as part of a flattened list
        returns None if unable to discard piece '''
    def discard(self, i):
        indexCount = 0
        indexActual = 0
        while(indexCount < i):
            if isinstance(self.hand[indexActual], Group):
                indexCount += len(self.hand[indexActual].pieces)
            else:
                indexCount += 1
            if indexCount <= i:
                indexActual += 1
        if isinstance(self.hand[indexActual], Group):
            group = self.hand[indexActual]
            if indexCount == i:
                return group.remove(group.pieces[0])
            else:
                return group.remove(group.pieces[i-indexCount+len(group.pieces)])
        else:
            return self.hand.pop(indexActual)

    ''' Old discard function, does not discard from groups
    # returns None if selected index is a group
    def discard(self, i):
        if isinstance(self.hand[i], Group):
            return None
        else:
            return self.hand.pop(i)'''

    def win(self):
        self.winner = True

    def checkWin(self):
        if all((isinstance(item, Group) and item.groupType != "none") for item in self.hand):
            pairs = 0
            for item in self.hand:
                if item.groupType == "pair":
                    pairs += 1
            if pairs < 2:
                self.win()

    # returns None if unable to form group
    def formGroup(self, pieces = []):
        if len(pieces) == 0:
            return None
        if any((piece not in self.hand) for piece in pieces):
            return None
        for piece in pieces:
            self.hand.remove(piece)
        self.hand.append(Group(pieces))
        self.sortHand()
        return Group

    # returns None if unable to add to group
    def addToGroup(self, piece, group):
        if piece in self.hand and group.add(piece) is not None:
            self.hand.remove(piece)
            self.sortHand()
            return group
        else:
            return None

    # returns None if unable to remove from group
    def removeFromGroup(self, piece, group):
        if group.remove(piece) is not None:
            self.hand.append(piece)
            if group.isEmpty():
                self.hand.remove(group)
            self.sortHand()
            return piece
        else:
            return None

    def find(self, piece = Piece("")):
        if piece.suit != "":
            for p in range(len(self.hand)):
                if isinstance(self.hand[p], Piece) and self.hand[p].name() == piece.name():
                    return p
            for p in range(len(self.hand)):
                if isinstance(self.hand[p], Group) and self.hand[p].find(piece) is not None:
                    return p + self.hand[p].find(piece)
        return None

    # for debugging
    def printHand(self):
        print(self.name, "\b's Hand")
        for item in self.hand:
            if isinstance(item, Piece):
                print("Piece:", item.name())
            elif isinstance(item, Group):
                print("Group: ", end ="")
                item.printGroup()
            else:
                print("Error: Unknown object in hand:", item)