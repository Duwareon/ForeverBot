#!/usr/bin/env python3
import discord
import typing
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
async def hug(ctx, arg1, gif: typing.Optional[str] = "mf"):
    await ctx.send("{0.author} hugged {1}".format(ctx, arg1))

    if gif == "mm":
        await ctx.send(random.choice(gifs.hugmm))

    elif gif == "mf":
        await ctx.send(random.choice(gifs.hugmf))

    elif gif == "ff":
        await ctx.send(random.choice(gifs.hugff))

    else:
        await ctx.send(random.choice(gifs.hugmf))


@bot.command()
async def kiss(ctx, arg1, gif: typing.Optional[str] = "mf"):
    await ctx.send("{0.author} kissed {1}".format(ctx, arg1))

    if gif == "mm":
        await ctx.send(random.choice(gifs.kissmm))

    elif gif == "mf":
        await ctx.send(random.choice(gifs.kissmf))

    elif gif == "ff":
        await ctx.send(random.choice(gifs.kissff))

    else:
        await ctx.send(random.choice(gifs.kissmf))


@bot.command()
async def cuddle(ctx, arg1, gif: typing.Optional[str] = "mf"):
    await ctx.send("{0.author} cuddled {1}".format(ctx, arg1))

    if gif == "mm":
        await ctx.send(random.choice(gifs.cuddlemm))

    elif gif == "mf":
        await ctx.send(random.choice(gifs.cuddlemf))

    elif gif == "ff":
        await ctx.send(random.choice(gifs.cuddleff))

    else:
        await ctx.send(random.choice(gifs.cuddlemf))

bot.run(os.getenv("TOKEN"))
