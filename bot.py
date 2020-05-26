import discord
import random
from MahjongClasses.mahjong import Mahjong
from MahjongClasses.mahjong import mahjong_dict
from MahjongClasses.player import Player
from MahjongClasses.piece import Piece
from discord.ext import commands
from discord.ext.commands import Bot

mahjongSession = None
TOKEN = ''
bot = commands.Bot(command_prefix=">")
peng_kong_asked = False
chi_asked = False
current_player = 0
last_piece = Piece("")

@bot.command()
async def start(ctx):
    if mahjongSession == None:
        await ctx.send("Waiting for players...")
        mahjongSession = Mahjong()
    else:
        await ctx.send("Game Already Started")

@bot.command()
async def join(ctx):
    if mahjongSession is not None:
        player = Player(ctx.author)
        if(not mahjongSession.addPlayer(player)):
            await ctx.send("4 players already added.")
        else:
            await ctx.send(ctx.author.name + " has joined!")
            if mahjongSession.atFullCapacity():
                await ctx.send("Please call the command 'game' to begin!")
    else:
        await ctx.send("No mahjong session has started")

@bot.command()
async def game(ctx):
    mahjongSession.Session.deal()
    for p in mahjongSession.players:
        message = "Hand: "
        for h in p.hand:
            message += mahjong_dict[h.name()]
        channel = await p.member.create_dm()
        await channel.send(message)
    global current_player
    current_player = 0

    def checkPlayFirst(m):
            return str(m.author.id) == mahjongSession.players[0].id and m.content.startsWith(">play")
    await mahjongSession.players[0].member.dm_channel.send("Play first tile...")
    await bot.wait_for('message', check=checkPlayFirst)
    current_player = 1
    while not (mahjongSession.winnerCheck() or mahjongSession.gameDraw()):
        if not (peng_kong_asked or chi_asked):
            pass
        current_player += 1
        current_player %= 4

@bot.command()
async def play(ctx, arg):
    if arg.isDigit():
        temp = mahjongSession.findPlayer(str(ctx.author.id))
        if temp is not None:
            global last_piece
            last_piece = mahjongSession.play(temp, int(arg))

@bot.command()
async def chi(ctx):
    global current_player
    current_player += 1
    current_player %= 4
    if str(ctx.author.id) == mahjongSession.players[current_player].id: 
        mahjongSession.pile[last_piece.name()] -= 1
        mahjongSession.chi(current_player, last_piece)
        def checkPlay(m):
            return m.content.startsWith(">play")
        await mahjongSession.players[current_player].member.dm_channel.send("Play a piece...")
        await bot.wait_for('message', check=checkPlay)

@bot.command()
async def peng(ctx):
    global current_player
    current_player = mahjongSession.findPlayer(str(ctx.author.id))
    if mahjongSession.players[current_player].canPengOrKong(last_piece) >= 2:
        mahjongSession.pile[last_piece.name()] -= 1
        mahjongSession.peng(current_player, last_piece)
        def checkPlay(m):
            return m.content.startsWith(">play")
        await mahjongSession.players[current_player].member.dm_channel.send("Play a piece...")
        await bot.wait_for('message', check=checkPlay)

@bot.command()
async def kong(ctx):
    global current_player
    current_player = mahjongSession.findPlayer(str(ctx.author.id))
    if mahjongSession.players[current_player].canPengOrKong(last_piece) == 3:
        mahjongSession.pile[last_piece.name()] -= 1
        mahjongSession.kong(current_player, last_piece)
        def checkPlay(m):
            return m.content.startsWith(">play")
        await mahjongSession.players[current_player].member.dm_channel.send("Play a piece...")
        await bot.wait_for('message', check=checkPlay)
bot.run(TOKEN)
