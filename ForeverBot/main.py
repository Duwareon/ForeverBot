#!/usr/bin/env python3
import discord
import typing
from discord.ext import commands
import os
import random
import db
from dotenv import load_dotenv

load_dotenv()


bot = commands.Bot(command_prefix='!')

incorrectPingErrMsg = "ping a user ya donkass"
man = db.GifManager()


async def act(ctx, action, pasttense, gender, arg1):
    await ctx.send("<@!{0}> {1} {2}".format(ctx.author.id, pasttense, arg1))
    x = random.choice(man.get_gifs(action, gender))[0]
    await ctx.send(x)


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command()
async def hug(ctx, arg1, gif: typing.Optional[str] = "*"):

    if arg1.startswith("<@!") and arg1.endswith(">"):
        await act(ctx, "hug", "hugged", gif, arg1)

    elif "<@!" in ctx.message.content and ">" in ctx.message.content:
        await ctx.send("the command format is \"{}hug [user] [mm/mf/ff]\"".format(bot.command_prefix))
    else:
        await ctx.send(incorrectPingErrMsg)


@bot.command()
async def kiss(ctx, arg1, gif: typing.Optional[str] = "*"):

    if arg1.startswith("<@!") and arg1.endswith(">"):
        await act(ctx, "kiss", "kissed", gif, arg1)

    elif "<@!" in ctx.message.content and ">" in ctx.message.content:
        await ctx.send("the command format is \"{}kiss [user] [mm/mf/ff]\"".format(bot.command_prefix))
    else:
        await ctx.send(incorrectPingErrMsg)


@bot.command()
async def cuddle(ctx, arg1, gif: typing.Optional[str] = "*"):

    if arg1.startswith("<@!") and arg1.endswith(">"):
        await act(ctx, "cuddle", "cuddled", gif, arg1)

    elif "<@!" in ctx.message.content and ">" in ctx.message.content:
        await ctx.send("the command format is \"{}cuddle [user] [mm/mf/ff]\"".format(bot.command_prefix))
    else:
        await ctx.send(incorrectPingErrMsg)

bot.run(os.getenv("TOKEN"))
