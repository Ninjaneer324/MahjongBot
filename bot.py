import discord
import random
from mahjong import Mahjong
from player import Player
from discord.ext import commands
from discord.ext.commands import Bot

mahjongSession = Mahjong()
TOKEN = ''
bot = commands.Bot(command_prefix=">")

@bot.command()
async def start(ctx):
    await ctx.send("Waiting for players...")

@bot.command()
async def join(ctx):
    player = Player(ctx.author.name, str(ctx.author.id))
    if(not mahjongSession.addPlayer(player)):
        await ctx.send("4 players already added.")
    else:
        await ctx.send(ctx.author.name + " has joined!")
        if mahjongSession.atFullCapacity():
            mahjongSession.deal()

bot.run(TOKEN)
