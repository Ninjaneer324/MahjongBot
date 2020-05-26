from deck import Deck
from piece import Piece
from group import Group
import random
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from bot import bot

mahjong_dict = {}
mahjong_dict["1 Bamboo"] = "🀐"
mahjong_dict["2 Bamboo"] = "🀑"
mahjong_dict["3 Bamboo"] = "🀒"
mahjong_dict["4 Bamboo"] = "🀓"
mahjong_dict["5 Bamboo"] = "🀔"
mahjong_dict["6 Bamboo"] = "🀕"
mahjong_dict["7 Bamboo"] = "🀖"
mahjong_dict["8 Bamboo"] = "🀗"
mahjong_dict["9 Bamboo"] = "🀘"
mahjong_dict["1 Dot"] = "🀙"
mahjong_dict["2 Dot"] = "🀚"
mahjong_dict["3 Dot"] = "🀛"
mahjong_dict["4 Dot"] = "🀜"
mahjong_dict["5 Dot"] = "🀝"
mahjong_dict["6 Dot"] = "🀞"
mahjong_dict["7 Dot"] = "🀟"
mahjong_dict["8 Dot"] = "🀠"
mahjong_dict["9 Dot"] = "🀡"
mahjong_dict["1 Wan"] = "🀇"
mahjong_dict["2 Wan"] = "🀈"
mahjong_dict["3 Wan"] = "🀉"
mahjong_dict["4 Wan"] = "🀊"
mahjong_dict["5 Wan"] = "🀋"
mahjong_dict["6 Wan"] = "🀌"
mahjong_dict["7 Wan"] = "🀍"
mahjong_dict["8 Wan"] = "🀎"
mahjong_dict["9 Wan"] = "🀏"
mahjong_dict["East"] = "🀀"
mahjong_dict["West"] = "🀂"
mahjong_dict["North"] = "🀃"
mahjong_dict["South"] = "🀁"
mahjong_dict["Center"] = "🀄"
mahjong_dict["Fortune"] = "🀅"
mahjong_dict["TV"] = "🀆"

# created to provide an abstracted interface to interact with
class Mahjong:
    def __init__(self, type='standard'):
        self.deck = Deck(type)
        self.players = []
        self.pile = {}

    def addPlayer(self, player):
        '''Adds players to the game and returns False when the max number of 4 players have already been reached'''
        if len(self.players) >= 4:
            return False
        self.players.append(player)
        return True

    def atFullCapacity(self):
        return len(self.players) == 4

    def deal(self):
        '''dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        wall = (dice_1 + dice_2) % 4
        wall_size = 0
        if deck.type.lower() == "standard":
            wall_size = 27
        else:
            wall_size = 34
        start = wall * wall_size + min(dice_1, dice_2)
        deck.moveBack(start)'''
        random.shuffle(self.players)
        self.dealToPlayers()

    def _playersHave12(self):
        for p in self.players:
            if len(p.hand) != 12:
                return False
        return True

    def dealToPlayers(self):
        '''Assuming playerOrder is a list of players, deal 13 tiles to each player and 14 tiles to starting player'''
        while not self._playersHave12():
            for p in self.players:
                p.add(self.deck.drawFront())
                p.add(self.deck.drawFront())
                p.add(self.deck.drawFront())
                p.add(self.deck.drawFront())
        for p in self.players:
            p.add(self.deck.drawFront())
        self.players[0].add(self.deck.drawFront())
    
    def winnerCheck(self):
        for i in self.players:
            if i.winner:
                return True
        return False
    
    def gameDraw(self):
        for i in self.players:
            if i.winner:
                return False
        return self.deck.isEmpty()
    
    def possibleChiCombos(self, piece):
        num = piece.number
        suit = piece.suit
        temp = []
        if num - 1 >= 1 and num - 2 >= 1:
            t = Group()
            t.add(Piece(suit, num - 2))
            t.add(Piece(suit, num - 1))
            t.add(Piece(suit, num))
            temp.append(t)
        if num - 1 >= 1 and num + 1 <= 9:
            t = Group()
            t.add(Piece(suit, num - 1))
            t.add(Piece(suit, num))
            t.add(Piece(suit, num + 1))
            temp.append(t)
        if num + 1 <= 9 and num + 2 <= 9:
            t = Group()
            t.add(Piece(suit, num))
            t.add(Piece(suit, num + 1))
            t.add(Piece(suit, num + 2))
            temp.append(t)
        return temp
    
    def findPlayer(self, discord_id):
        for i in range(len(self.players)):
            if self.players[i].id == discord_id:
                return i
        return None

    def play(self, player_index, i):
        p = self.players[player_index].discard(i)
        if p.name() in self.pile:
            self.pile[p.name()] += 1
        else:
            self.pile[p.name()] = 1
        return p
    
    def chi(self, player_index, piece):
        possible = self.possibleChiCombos(piece)
        options = []
        #right now i'm working under the pretext that the remove function for Group is working properly
        for i in possible:
            i.remove(piece)
            if self.players[player_index].find(i.pieces[0]) is not None and self.players[player_index].find(i.pieces[1]) is not None:
                i.add(piece)
                options.append(i)
        
        def checkValid(m):
            return str(m.author.id) == self.players[player_index].id and m.content.isDigit() and 1 <= int(m.content) <= len(options)

        if len(options) == 0:
            return None
        elif len(options) == 1:
            options[0].remove(piece)
            first = self.players[player_index].find(options[0].pieces[0])
            second = self.players[player_index].find(options[0].pieces[1])
            self.players[player_index].discard(first)
            self.players[player_index].discard(second)
            options[0].showGroup()
            self.players[player_index].hand.append(options[0])
        else:
            await self.players[player_index].member.dm_channel.send("Which chi?")
            for i in range(len(options)):
                msg = str(i + 1) + ": "
                for p in options[i].pieces:
                    msg += mahjong_dict[p.name()]
                channel = await self.players[player_index].member.create_dm()
                await channel.send(msg)
            message = await bot.wait_for('message', check=checkValid)
            num = int(message.content) - 1
            options[num].remove(piece)
            first = self.players[player_index].find(options[num].pieces[0])
            second = self.players[player_index].find(options[num].pieces[1])
            self.players[player_index].discard(first)
            self.players[player_index].discard(second)
            options[num].showGroup()
            self.players[player_index].hand.append(options[num])
    def peng(self, player_index, piece):
        first = self.players[player_index].find(piece)
        self.players[player_index].discard(first)
        second = self.players[player_index].find(piece)
        self.players[player_index].discard(second)
        t = Group()
        t.add(piece)
        t.add(piece)
        t.add(piece)
        t.showGroup()
        self.players[player_index].hand.append(t)
        return None
    
    def kong(self, player_index, piece):
        first = self.players[player_index].find(piece)
        self.players[player_index].discard(first)
        second = self.players[player_index].find(piece)
        self.players[player_index].discard(second)
        t = Group()
        t.add(piece)
        t.add(piece)
        t.add(piece)
        t.add(piece)
        t.showGroup()
        self.players[player_index].hand.append(t)
        self.players[player_index].add(self.deck.drawBack())
        return None