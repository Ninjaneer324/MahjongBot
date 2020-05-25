import discord
import random
from MahjongClasses.mahjong import Mahjong
from MahjongClasses.mahjong import mahjong_dict
from MahjongClasses.player import Player
from discord.ext import commands
from discord.ext.commands import Bot

mahjongSession = None
TOKEN = ''
bot = commands.Bot(command_prefix=">")
peng_kong = False
chi = False

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
    i = 0

    def checkPlayFirst(m):
            return str(m.author.id) == mahjongSession.players[0].id and m.content.startsWith(">play")
    await mahjongSession.players[0].member.dm_channel.send("Play first tile...")
    await bot.wait_for('message', check=checkPlayFirst)
    i = 1
    while not (mahjongSession.winnerCheck() or mahjongSession.gameDraw()):
        if not (peng_kong or chi):
            pass
        i += 1
        i %= 4
@bot.command()
async def play(ctx, arg):
    if arg.isDigit():
        temp = mahjongSession.findPlayer(str(ctx.author.id))
        if temp is not None:
            mahjongSession.play(temp, int(arg))
bot.run(TOKEN)
