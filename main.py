#!/usr/bin/env python3
import discord
from discord.ext import commands
import os
import random
import gifs
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command()
async def hug(ctx, arg1, gif):
    await ctx.send("{0.author} hugged {1}".format(ctx, arg1))
    await sendGif(ctx, gif)


async def sendGif(ctx, gif):
    if gif == "mm":
        await ctx.send(random.choice(gifs.hugmf))

    if gif == "mf":
        await ctx.send(random.choice(gifs.hugmf))

    if gif == "ff":
        await ctx.send(random.choice(gifs.hugff))

bot.run(os.getenv("TOKEN"))
