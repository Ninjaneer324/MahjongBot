import discord
import random
from deck import Deck
from discord.ext import commands
from discord.ext.commands import Bot

turns = []
deck = Deck()
TOKEN = ''
bot = commands.Bot(command_prefix=">")

def deal():
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    wall = (dice_1 + dice_2) % 4
    wall_size = 0
    if deck.type.lower() == "standard":
        wall_size = 27
    else:
        wall_size = 34
    start = wall * wall_size + min(dice_1, dice_2)
    deck.moveBack(start)
    if wall != 0:
        for i in range(0, wall):
            last = turns.pop(0)
            turns.append(last)
    deck.dealToPlayers(turns)

@bot.command()
async def start(ctx):
    await ctx.send("Waiting for players...")

@bot.command()
async def join(ctx):
    if(len(turns) >= 4):
        await ctx.send("4 players already added.")
    else:
        turns.append(ctx.author)
        await ctx.send(ctx.author.name + " has joined!")
        if len(turns) == 4:
            deal()

bot.run(TOKEN)
