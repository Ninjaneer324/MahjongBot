import discord
from discord.ext import commands
from discord.ext.commands import Bot

turns = []

TOKEN = ''
bot = commands.Bot(command_prefix=">")

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

bot.run(TOKEN)
