import discord
from discord.ext import commands
from discord.ext.commands import Bot

turns = []

TOKEN = ''
bot = commands.Bot(command_prefix=">")

#So I was thinking: the command could be like >mahjong username1 username2 username3 username4
# to start a game



@bot.command()
async def start(ctx):
    await ctx.send("Waiting for players...")

@bot.command()
async def join(ctx):
    if(len(turns) >= 4):
        await ctx.send("4 players already added.")
    else:
        await ctx.send(ctx.author.name + " has joined!")

bot.run(TOKEN)
