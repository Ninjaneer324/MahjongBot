import discord
import random
from MahjongClasses.mahjong import Mahjong
from MahjongClasses.player import Player
from discord.ext import commands
from discord.ext.commands import Bot

mahjongSession = None
TOKEN = ''
bot = commands.Bot(command_prefix=">")

@bot.command()
async def start(ctx):
    await ctx.send("Waiting for players...")
    mahjongSession = Mahjong()

@bot.command()
async def join(ctx):
    if mahjongSession is not None:
        player = Player(ctx.author.name, ctx.author.id)
        if(not mahjongSession.addPlayer(player)):
            await ctx.send("4 players already added.")
        else:
            await ctx.send(ctx.author.name + " has joined!")
            if mahjongSession.atFullCapacity():
                mahjongSession.deal()
    else:
        await ctx.send("No mahjong session has started")

bot.run(TOKEN)
