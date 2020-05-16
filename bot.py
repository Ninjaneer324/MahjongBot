import discord
import random
from MahjongClasses.mahjong import Mahjong
from MahjongClasses.player import Player
from discord.ext import commands
from discord.ext.commands import Bot

mahjongSession = None
TOKEN = ''
bot = commands.Bot(command_prefix=">")

mahjong_dict = {}
mahjong_dict["1 Bamboo"] = "693115556454334592"
mahjong_dict["2 Bamboo"] = "693115555829514260"
mahjong_dict["3 Bamboo"] = "693115553409269780"
mahjong_dict["4 Bamboo"] = "693115553644281948"
mahjong_dict["5 Bamboo"] = "693115553283309609"
mahjong_dict["6 Bamboo"] = "693115553572847616"
mahjong_dict["7 Bamboo"] = "693115555733045319"
mahjong_dict["8 Bamboo"] = "693115544940970087"
mahjong_dict["9 Bamboo"] = "693115555590438914"
mahjong_dict["1 Dot"] = "693115559805452359"
mahjong_dict["2 Dot"] = "693115560103510106"
mahjong_dict["3 Dot"] = "693115559843201034"
mahjong_dict["4 Dot"] = "693115559872823317"
mahjong_dict["5 Dot"] = "693115560321613824"
mahjong_dict["6 Dot"] = "693115560568946758"
mahjong_dict["7 Dot"] = "693115560329740308"
mahjong_dict["8 Dot"] = "693115556404002846"
mahjong_dict["9 Dot"] = "693115560212561980"
mahjong_dict["1 Wan"] = "693115553635893329"
mahjong_dict["2 Wan"] = "693115555682713633"
mahjong_dict["3 Wan"] = "693115555590438914"
mahjong_dict["4 Wan"] = "693115555858874388"
mahjong_dict["5 Wan"] = "693115555132997654"
mahjong_dict["6 Wan"] = "693115555745628290"
mahjong_dict["7 Wan"] = "693115555753754644"
mahjong_dict["8 Wan"] = "693115545255542844"
mahjong_dict["9 Wan"] = "693115555640639489"
mahjong_dict["East"] = "693115485876650054"
mahjong_dict["West"] = "693115556290625626"
mahjong_dict["North"] = "693115553744945232"
mahjong_dict["South"] = "693115553572847657"
mahjong_dict["Center"] = "693115551106727997"
mahjong_dict["Fortune"] = "693115555930177576"
mahjong_dict["TV"] = "693115556236361819"

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
